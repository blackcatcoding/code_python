# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/7/5 17:18
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

# 1 2 3 4 5 6

li = [int(i) for i in input().split()]

odds, evens = [], []

[odds.append(i) for i in li if i % 2 == 1]
[evens.append(i) for i in li if i % 2 == 0]

odds.sort(reverse=True)
evens.sort()

res = odds + evens

for i in res:
    print(i, end=' ')
