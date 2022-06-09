# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/23 22:42
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

from functools import reduce

print(reduce(lambda m, n : m + n, list(range(1, 6))))