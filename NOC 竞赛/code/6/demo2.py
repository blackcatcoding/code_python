# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/26 15:58
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : http://www.blackcat1995.com/

for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%d" % (j, i, j * i), end=' ')
    print()