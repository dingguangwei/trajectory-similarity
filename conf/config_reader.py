# encoding = utf-8
import configparser


def init():
    config = configparser.ConfigParser()
    config.read("../conf.cfg")
    return config


def get_root_path():
    config = init()
    return config.get("data", "root_path")


def get_debug_model():
    config = init()
    return bool(config.get("run", "debug_model"))


def get_algorithm_code():
    config = init()
    return int(config.get("run", "algorithm_code"))


if __name__ == "__main__":
    print(get_root_path())
    print(get_debug_model())
    print(get_algorithm_code())

