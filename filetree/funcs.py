# coding=utf-8

import os
import errno

def is_image(name, exts=None):
    """return True if the name or path is endswith {jpg|png|gif|jpeg}"""

    default = ['jpg', 'png', 'gif', 'jpeg']
    if exts:
        default += exts

    flag = False
    for ext in default:
        if name.lower().endswith(ext):
            flag = True
            break
    return flag


def iterable(iterator):
    flag = True
    try:
        for _ in iterator:
            pass
    except TypeError:
        flag = False
    return flag


def remove_empty_dir(path):
    """ Function to remove empty folders """
    try:
        if not os.path.isdir(path):
            return

        files = os.listdir(path)

        # if folder empty, delete it
        if len(files) == 0:
            os.rmdir(path)

        # remove empty subdirectory
        elif len(files) > 0:
            for f in files:
                abspath = os.path.join(path, f)
                if os.path.isdir(abspath):
                    remove_empty_dir(abspath)
    except OSError as e:
        if e.errno == errno.ENOTEMPTY:
            pass


def remove_empty_subdir(path):
    if not os.path.isdir(path):
        return
    for p in os.listdir(path):
        abspath = os.path.join(path, p)
        if os.path.isdir(abspath):
            remove_empty_dir(abspath)

def human_size(s, factor):
    """
    :s: size
    :factor: 1000 or 1024
    """
    unit = 'B'
    if s > factor:
        s /= factor
        unit = 'KB'
    if s > factor:
        s /= factor
        unit = 'MB'
    if s > factor:
        s /= factor
        unit = 'GB'
    if s > factor:
        s /= factor
        unit = 'TB'
    return '%.2f %s' % (s, unit)
