# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/25 23:27
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : http://www.blackcat1995.com/

for num in range(2, 10, 2):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)