# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/23 22:31
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

a = [1, 2]
b = [4, 5, 6]
c = [7, 8, 9, 10]

z = zip(a, b, c)
print(z)

print(list(z))

m, n, k = zip(*zip(a, b, c))
print(m, n, k)
