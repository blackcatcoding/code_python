# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/7/5 16:31
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            if i != j and i != k and j != k:
                print(i, j, k)
