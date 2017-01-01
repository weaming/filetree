Easier file tree for human.
===========================

Examples::

    >>> from filetree import File
    >>> f = File('.')
    >>> f.files
    [<file: .gitignore>, <file: LICENSE>, <file: Makefile>, <file: README.rst>, <file: setup.py>]
    >>> f.dirs
    [<dir: .git>, <dir: build>, <dir: dist>, <dir: docs>, <dir: filetree>]
    >>> f.images
    [<file: python-logo.png>, <file: favicon.jpg>]

API::

   __call__ 
   __iter__ 
   __eq__

   files 
   dirs 
   images 
   listdir 

   exists 
   type 

   is_blank 
   is_dir 
   is_file 
   is_hidden 

   info 
   atime 
   ctime 
   mtime 

   move_to 
   remove 
   remove_blank_dirs 
   remove_blank_subdir 

   size 
   walk 
