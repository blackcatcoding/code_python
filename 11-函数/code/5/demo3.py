# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/23 22:24
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

# send

def f():

    a = yield 1
    print('a =', a)

    b = yield a
    print('b =', b)

    c = yield b

ret = f()

print(next(ret))
print(ret.send('hahaha'))
print(ret.send('xxx'))
