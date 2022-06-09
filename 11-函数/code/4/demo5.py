# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/20 15:50
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : http://www.blackcat1995.com/

import time

def calc_time(f):

    def inner():

        start_time = time.time()
        ret = f()
        end_time = time.time()

        print('程序运行%.3f秒' % (end_time - start_time))

        return ret

    return inner

@calc_time
def index():
    time.sleep(2)
    return 'index'

print(index())