# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/24 23:09
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

li = [1, 3, 5, 8]

cnt = 0

for i in li:
    for j in li:
        for k in li:
            if i != j and i != k and j != k:
                print(str(i) + str(j) + str(k))
                cnt += 1

print(cnt)