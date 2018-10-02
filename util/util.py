# coding=utf-8

m_rate = 3
def print_rate(str, i, n):
    if i%(int(n/m_rate))==0:
        print(str, i, '/', n)

def print_complete(str):
    print(str)