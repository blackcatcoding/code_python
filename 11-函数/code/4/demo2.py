# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/20 15:41
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : http://www.blackcat1995.com/
import time

def index():

    time.sleep(2)

def calc_time():

    start_time = time.time()
    index()
    end_time = time.time()

    print('程序运行%.3f秒' % (end_time - start_time))

calc_time()
