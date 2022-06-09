# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/20 15:52
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : http://www.blackcat1995.com/

import time

def calc_time(f):

    def inner(*args, **kwargs):

        start_time = time.time()
        ret = f(*args, **kwargs)
        end_time = time.time()

        print('程序运行%.3f秒' % (end_time - start_time))

        return ret

    return inner

@calc_time
def add(a, b, c):
    time.sleep(2)
    return a + b + c

print(add(1, 2, 3))