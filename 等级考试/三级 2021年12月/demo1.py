# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/15 14:36
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import csv

with open('score.csv') as f:
    rows = list(csv.reader(f))
    sum1 = 0
    sum2 = 0
    for row in rows[1:]:
        if int(row[0]) == 1:
            sum1 += int(row[1])
        else:
            sum2 += int(row[1])

    print(sum1, sum2)
