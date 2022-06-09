# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/26 10:53
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

def is_ws(x):

    s = 0

    for i in range(1, x):
        if  x % i == 0:
            s += i

    return s == x

n = int(input())

cnt = 0

for i in range(1, n):
    if is_ws(i):
        cnt += 1
        print(i)

print('*' + str(cnt))