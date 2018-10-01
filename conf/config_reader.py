# encoding = utf-8
import configparser


def get_root_path():
    config = configparser.ConfigParser()
    config.read("../conf.cfg")
    return config.get("data", "root_path")


if __name__ == "__main__":
    print(get_root_path())
