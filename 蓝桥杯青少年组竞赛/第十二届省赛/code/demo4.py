# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/9 9:44
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

# 3,2,4,6,7
li = [int(i) for i in input().split(',')]
li.sort()
# print(li)

for i in range(len(li) - 1):
    if li[i] + 1 != li[i + 1]:
        print(li[i] + 1)