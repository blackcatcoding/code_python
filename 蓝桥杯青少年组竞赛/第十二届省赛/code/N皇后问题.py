# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/10 10:41
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

cnt = 0
def dfs(u):
    global cnt
    if u == n:
        # for i in range(n):
        #     print(''.join(g[i]))
        # print()
        cnt += 1
        return

    for i in range(n):
        if not col[i] and not dg[n + i - u] and not udg[u + i]:
            g[u][i] = 'Q'
            col[i] = dg[n + i - u] = udg[u + i] = True
            dfs(u + 1)
            col[i] = dg[n + i - u] = udg[u + i] = False
            g[u][i] = '.'

n = int(input())

g = [['.' for i in range(n)] for i in range(n)]

col = [False] * n
dg = [False] * 2 * n
udg = [False] * 2 * n

dfs(0)

print(cnt)