# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/14 11:26
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

# abc123b45efg
# abcbefg

s = input()

for i in s:
    if not ('0' <= i <= '9'):
        print(i, end='')