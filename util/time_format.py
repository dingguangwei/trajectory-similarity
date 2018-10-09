# coding=utf-8
import time, datetime


# second = 1539068639
def get_date_by_second(second):
    time_array = time.localtime(second)
    time_style = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    date = datetime.datetime.strptime(time_style, "%Y-%m-%d %H:%M:%S")
    return date


# date_str = "2014-07-29 00:00:00"
def get_second_by_date(date_str):
    m_time = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    second = int(time.mktime(m_time.timetuple()))
    return second


if __name__ == '__main__':
    print(get_date_by_second(1539068639))
    print(get_second_by_date('2018-10-09 15:03:59'))