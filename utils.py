# coding:utf-8
import os


def is_folder(path):
    return os.path.isdir(path)


class Ofile(object):
    def __init__(self, father_path, relative_path, name,):
        self.father_path = father_path
        self.relative_path = relative_path
        self.name = name

    @property
    def full_path(self):
        return os.path.join(self.father_path, self.relative_path, self.name)

    @property
    def path_to_father(self):
        return os.path.join(self.relative_path, self.name)