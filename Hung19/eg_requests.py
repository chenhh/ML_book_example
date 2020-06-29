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


def get_url_with_exception(url):
    html = requests.get(url)
    try:
        html.raise_for_status()
    except Exception as err:
        print("html get url: {}".format(url))


if __name__ == '__main__':
    get_url("http://www.yahoo.com.tw")
