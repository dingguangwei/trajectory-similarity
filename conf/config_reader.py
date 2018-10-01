# encoding = utf-8
import configparser


def get_root_path():
    config = configparser.ConfigParser()
    config.read('conf.cfg')
    return config.get('data', 'root_path')

