# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/7/5 18:35
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

# 12 18
'''
12 % 12   18 % 12
11
10
9
8
7
6
'''

def gcd(a, b):

    minv = min(a, b)

    for i in range(minv, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

a, b = [int(i) for i in input().split()]

print(gcd(a, b))
