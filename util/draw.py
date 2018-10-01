# coding=utf-8
from util.file_reader import file_reader
from conf.config_reader import get_root_path


def draw(index_list):
    root_path = get_root_path()
    reader = file_reader(root_path=root_path)
    reader.get_some_trajectory(index_list=index_list)



