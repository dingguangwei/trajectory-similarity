# coding=utf-8

m_rate = 3


def print_rate(str, i, n):
    if i % (int(n / m_rate)) == 0:
        print(str, i, "/", n)


def print_complete(str, using_time=None):
    if using_time is None:
        print(str)
    else:
        print(str, "Using ", using_time, "s")


def print_error(str):
    print("error:", str)
