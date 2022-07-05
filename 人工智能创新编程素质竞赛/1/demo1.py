# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/7/5 16:28
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import random

r1 = random.randint(0, 3)
r2 = random.randint(0, 3)
r3 = random.randint(0, 3)

print(r1, r2, r3)

while True:

    a = int(input('1:'))
    if a == r1:
        print('1  ok')
        b = int(input('2:'))
        if b == r2:
            print('2 ok')
            c = int(input('3:'))
            if c == r3:
                print('success')
                break
