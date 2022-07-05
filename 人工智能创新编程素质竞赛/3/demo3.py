# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/7/5 18:38
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

'''
辗转相除
18 12
18 % 12 = 6
12 % 6 = 0
6 % 0
'''

def gcd(a, b):

    if b == 0:
        return a

    return gcd(b, a % b)

a, b = [int(i) for i in input().split()]

print(gcd(a, b))