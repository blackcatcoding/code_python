# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/8 18:34
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

d = {}
for i in range(1, 27):
    if i < 10:
        d[chr(97 + i - 1)] = '0' + str(i)
    else:
        d[chr(97 + i - 1)] = str(i)

s = input()

s1 = ''
for i in s:
    if i == ' ':
        s1 += i
    else:
        s1 += d[i]

# print(s1)

s2 = ''
for i in s1:
    if i == ' ':
        s2 += '00'
    else:
        s2 += str(int(i) + 27)

print(s2)