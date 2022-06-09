# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/25 15:47
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import turtle as t
import random

t.tracer(False)
t.screensize(800, 600)

def draw_tree(level, length, flag):

    if level == 0:
        return

    t.left(20 * flag)
    t.fd(length)

    draw_tree(level - 1, length - 6, flag)

    t.fd(-length)
    t.right(15 * flag)
    t.fd(length)

    draw_tree(level - 1, length - 6, flag)

    t.fd(-length)

    t.right(5 * flag)

for i in range(50):
    level = random.randint(4, 6)
    length = random.randint(30, 60)
    t.up()
    y = random.randint(-300, 300)

    if i % 2 == 0:
        t.seth(120)
        x = random.randint(-400, -1)
        t.goto(x, y)
        t.pd()
        draw_tree(level, length, 1)
    else:
        t.seth(60)
        x = random.randint(1, 400)
        t.goto(x, y)
        t.pd()
        draw_tree(level, length, -1)

t.done()