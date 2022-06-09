# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/8 22:17
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

V = int(input())
n = int(input())

'''
f[i][j] 前i个物品可以选，容量不超过j，最大体积
'''

f = [[0 for i in range(V + 1)] for i in range(n + 1)]

for i in range(1, n + 1):
    v = int(input())
    for j in range(1, V + 1):
        if j >= v:
            f[i][j] = max(f[i - 1][j], v + f[i - 1][j - v])
        else:
            f[i][j] = f[i - 1][j]

print(V - f[-1][-1])