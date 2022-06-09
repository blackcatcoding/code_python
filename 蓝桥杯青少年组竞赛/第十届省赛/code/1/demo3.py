# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/24 23:17
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

# 9,12,15,22,5,21,214

bak = [int(i) for i in input().split(',')]
li = sorted(bak, reverse=True)
# print(bak)
# print(li)
print(len(li))
print(min(li))

for i in li:
    print(i, end=',')
print()

for i in bak:
    if i >= 1 and i <= 26:
        print(chr(65 + i - 1), end='')
    else:
        print('[bad]', end='')