# -*- coding: utf-8 -*-
import webbrowser


def open_url():
    webbrowser.open('http://www.yahoo.com.tw', 1)


def google_map_lookup(location):
    webbrowser.open("http://www.google.com.tw/maps/place/" + location)


if __name__ == '__main__':
    # open_url()
    google_map_lookup("漢神百貨")