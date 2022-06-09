# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/25 15:43
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import turtle as t

def draw_tree(level, length):

    if level == 0:
        return

    t.left(30)
    t.fd(length)

    draw_tree(level - 1, length - 6)

    t.fd(-length)
    t.right(60)
    t.fd(length)

    draw_tree(level - 1, length - 6)

    t.fd(-length)

    t.left(30)


t.seth(90)
draw_tree(4, 60)

t.done()