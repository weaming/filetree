# coding=utf-8
"""
Easier file operation.
"""
import os
import datetime
import shutil

from .funcs import is_image, iterable
from .funcs import remove_empty_dir


def tree(path, depth=2, topdown=True, followlinks=False, showhidden=False):
    """A generator return a tuple with three elements (root, dirs, files)."""
    rt = []
    for root, dirs, files in os.walk(path, topdown=topdown, followlinks=followlinks):
        if not showhidden and File.is_hidden(root):
            continue

        current_depth = len(os.path.relpath(root, path).split(os.sep))
        if current_depth > depth:
            continue

        if showhidden:
            _tuple = (
                root,
                [File(os.path.join(root, _dir)) for _dir in dirs],
                [File(os.path.join(root, _file)) for _file in files]
            )
        else:
            _tuple = (
                root,
                [File(os.path.join(root, _dir)) for _dir in dirs if _dir[0] != '.'],
                [File(os.path.join(root, _file)) for _file in files if _file[0] != '.']
            )

        rt.append(_tuple)
    return rt


class File(object):
    def __init__(self, path, root=None):
        _root = root or '.'
        if type(path) != str:
            raise TypeError("path isn't string!")
        self._path = path
        self._root = root
        self.path = os.path.abspath(path)
        self.isabs = os.path.isabs(path)

        # 这里有顺序依赖
        self.dirname, self.basename = os.path.split(self.path)
        self.root = root or (self.dirname if self.isabs else _root)
        self.relpath = os.path.relpath(path, self.root)
        self.namewoext, self.ext = os.path.splitext(self.basename)
        self.ext = self.ext[1:]
        self.hidden = self.is_hidden(path)

        if self.type == 'dir':
            self.namewoext = self.ext = None

    def exists(self):
        return os.path.exists(self.path)

    def is_blank(self):
        if self.is_dir():
            return len(os.listdir(self.path)) == 0
        return False

    def remove(self):
        if self.is_file():
            os.remove(self.path)
        elif self.is_dir():
            os.rmdir(self.path)

    def remove_blank_dirs(self):
        """Remove blank dir and all blank subdirectories"""
        if self.is_blank():
            try:
                os.rmdir(self.path)
            except OSError:
                pass
        else:
            remove_empty_dir(self.path)

    def remove_blank_subdir(self):
        for i in self.dirs:
            i.remove_blank_dirs()

    def move_to(self, target):
        shutil.move(self.path, target)

    def is_dir(self):
        return os.path.isdir(self.path)

    def is_file(self):
        return os.path.isfile(self.path)

    @property
    def type(self):
        if self.is_dir():
            return 'dir'
        if self.is_file():
            return 'file'

    @property
    def dirs(self):
        rv = []
        if self.type == 'dir':
            paths = os.listdir(self.path)
            paths.sort()
            for p in paths:
                abs_p = os.path.join(self.path, p)
                if os.path.isdir(abs_p):
                    rv.append(File(abs_p))
        return rv

    @property
    def files(self):
        rv = []
        if self.type == 'dir':
            paths = os.listdir(self.path)
            paths.sort()
            for p in paths:
                abs_p = os.path.join(self.path, p)
                if os.path.isfile(abs_p):
                    rv.append(File(abs_p))
        return rv

    def listdir(self):
        rv = []
        if self.type == 'dir':
            paths = os.listdir(self.path)
            paths.sort()
            for p in paths:
                abs_p = os.path.join(self.path, p)
                rv.append(File(abs_p))
        return rv

    def __iter__(self):
        if self.type == 'dir':
            paths = os.listdir(self.path)
            paths.sort()
            for p in paths:
                abs_p = os.path.join(self.path, p)
                yield File(abs_p)

    @property
    def images(self):
        return [x for x in self.files if is_image(x.basename)]

    @property
    def info(self):
        return os.stat(self.path)

    def size(self, factor=1000):
        factor = float(factor)
        s = self.info.st_size
        unit = 'B'
        if s > factor:
            s /= factor
            unit = 'kB'
        if s > factor:
            s /= factor
            unit = 'M'
        if s > factor:
            s /= factor
            unit = 'G'
        if s > factor:
            s /= factor
            unit = 'T'
        return '%s %s' % (s, unit)

    @property
    def ctime(self, tz=None):
        return self.__parse_time(self.info.st_ctime, tz=tz)

    @property
    def mtime(self, tz=None):
        return self.__parse_time(self.info.st_mtime, tz=tz)

    @property
    def atime(self, tz=None):
        return self.__parse_time(self.info.st_atime, tz=tz)

    @staticmethod
    def __parse_time(timestamp, tz=None):
        if tz is None or issubclass(tz, datetime.tzinfo):
            rt = datetime.datetime.fromtimestamp(timestamp, tz=tz)
        else:
            rt = datetime.datetime.utcfromtimestamp(timestamp)
        return rt

    @staticmethod
    def is_hidden(path):
        length = len(path)
        if length == 0:
            raise AttributeError('path is null')
        else:
            abs_path = os.path.abspath(path)
            paths = abs_path.split(os.sep)
            for p in paths:
                if p.startswith('.'):
                    return True
            return False

    def tree(self, showhidden=False):
        return tree(self.path, showhidden=showhidden)

    def walk(self, **kw):
        """Call os.walk() without providing the first path argument."""
        return os.walk(self.path, **kw)

    def __repr__(self):
        return '<{0}: {1}>'.format(self.type, self.basename)

    def __str__(self):
        return self.__repr__()

    def __call__(self):
        """Refresh current File object"""
        return File(self._path, self.root)

    def __eq__(self, file):
        """Return True if the absolute path is same"""
        if isinstance(file, File):
            return self.path == file.path
        else:
            return self.path == os.path.abspath(file)

