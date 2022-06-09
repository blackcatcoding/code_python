# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/8 23:26
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

data = [ [1, 5, "XH"],  [1, 20, "DH"],  [2, 4, "LC"],  [2, 19, "YS"],  [3, 5, "JZ"],  [3, 20, "CF"],
		 [4, 4, "QM"],  [4, 19, "GY"],  [5, 5, "LX"],  [5, 20, "XM"],  [6, 5, "MZ"],  [6, 21, "XZ"],
		 [7, 6, "XS"],  [7, 22, "DS"],  [8, 7, "LQ"],  [8, 22, "CS"],  [9, 7, "BL"],  [9, 22, "QF"],
		 [10, 8, "HL"], [10, 23, "SJ"], [11, 7, "LD"], [11, 22, "XX"], [12, 7, "DX"], [12, 21, "DZ"] ]

year, month, date = [int(i) for i in input().split('*')]
# print(year, month, date)

if month == 12 and date > 21:
    print("XH")
else:
    for i in data:
        if i[0] > month or i[0] == month and i[1] >= date:
            print(i[2])
            break

# 2020*06*21

