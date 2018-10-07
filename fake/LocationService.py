# coding=utf-8

from urllib import parse
import hashlib

def get_urt(address):
    # 以get请求为例http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=你的ak
    queryStr = '/geocoder/v2/?address=%s&output=json&ak=vQQKy2g0x178PeWq0GLY8lj8H6UP9Gml' % address

    # 对queryStr进行转码，safe内的保留字符不转换
    encodedStr = parse.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")

    # 在最后直接追加上yoursk
    rawStr = encodedStr + 'YqUPUOpPWpbwbCrbM88Ya0NFNuFEcgCM'

    # 计算sn
    sn = (hashlib.md5(parse.quote_plus(rawStr).encode("utf8")).hexdigest())

    # 由于URL里面含有中文，所以需要用parse.quote进行处理，然后返回最终可调用的url
    url = parse.quote("http://api.map.baidu.com" + queryStr + "&sn=" + sn, safe="/:=&?#+!$,;'@()*[]")

    return url

print(get_urt('天安门'))