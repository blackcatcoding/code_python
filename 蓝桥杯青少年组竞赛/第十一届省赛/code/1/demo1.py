# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/26 10:48
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

s = input()

if s[-2:] == 'er' or s[-2:] == 'ly':
    print(s[:-2])
elif s[-3:] == 'ing':
    print(s[:-3])
else:
    print(s)
