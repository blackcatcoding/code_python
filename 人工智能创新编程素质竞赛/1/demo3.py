# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/7/5 16:32
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

def dfs(u):

    if u == n + 1:
        for i in range(1, n + 1):
            print(path[i], end=' ')
        print()
        return

    for i in range(1, n + 1):
        if not book[i]:
            path[u] = i
            book[i] = True
            dfs(u + 1)
            book[i] = False

path = [0] * 20
book = [False] * 20

n = int(input())
dfs(1)