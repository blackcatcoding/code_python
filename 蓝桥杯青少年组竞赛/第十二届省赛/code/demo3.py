# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/9 9:40
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

n = int(input())

cnt = 0

for i in range(100, n + 1):
    s = str(i)
    if i == int(s[0]) ** 3 + int(s[1]) ** 3 + int(s[2]) ** 3:
        cnt += 1

print(cnt)