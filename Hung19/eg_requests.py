# -*- coding: utf-8 -*-
import requests


def get_url(url):
    html = requests.get(url)
    # <class 'requests.models.Response'>

    # code 200
    if html.status_code == requests.codes.ok:
        print(type(html))
        # < Response[200] >
        print(html)
    else:
        print("{} get file error".format(url))


if __name__ == '__main__':
    get_url("http://www.yahoo.com.tw")
