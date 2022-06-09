# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/23 22:21
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

def get_data():

    for i in range(1, 10000):
        yield i

d = get_data()

for i in range(1, 10):
    print(next(d), end=' ')

print()

for i in range(30, 40):
    print(next(d), end=' ')
