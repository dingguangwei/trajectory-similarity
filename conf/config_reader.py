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
    debug_model = config.get("run", "debug_model")
    if debug_model == 'True' or debug_model == 'true':
        return True
    else:
        return False


def get_algorithm_code():
    config = init()
    return int(config.get("run", "algorithm_code"))


if __name__ == "__main__":
    print(get_root_path())
    print(get_debug_model())
    print(get_algorithm_code())

