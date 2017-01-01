# coding=utf-8

from pprint import pprint

from filetree.tree import File, tree
from filetree.funcs import iterable


class TestTree():
    def test_file(self):
        f1 = File('notExists.txt')
        f2 = File('LICENSE')
        f3 = File('.')
        f4 = File('.git')
        li = (f1, f2, f3, f4)

        assert f1.type == None

        for f in li:
            print(f)
            pprint(f.__dict__)
            print('=' * 100)

    def test_tree(self):
        t1 = tree('.', showhidden=True)
        t2 = tree('.', showhidden=False)

        flag = False
        for node in t1:
            dirs = [x.basename for x in node[1]]
            files = [x.basename for x in node[2]]
            if any(map(lambda x: x.startswith('.'), dirs + files)):
                flag = True
                break
        assert flag

        for node in t2:
            dirs = [x.basename for x in node[1]]
            files = [x.basename for x in node[2]]
            assert all(map(lambda x: not x.startswith('.'), dirs + files))

    def test_iterable(self):
        assert iterable('abc') is True
        assert iterable(None) is False
