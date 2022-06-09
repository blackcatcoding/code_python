# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/20 15:44
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : http://www.blackcat1995.com/

import time

def index():

    time.sleep(2)

def calc_time(f):

    def inner():

        start_time = time.time()
        f()
        end_time = time.time()

        print('程序运行%.3f秒' % (end_time - start_time))

    return inner

# index = calc_time(index)
# index()

# 语法糖
@calc_time
def f():
    time.sleep(1.2)

f()
# f = calc_time(f)
# f()