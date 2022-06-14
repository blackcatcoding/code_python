# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/14 11:24
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

while True:

    score = int(input('请输入你的成绩：'))

    if score >= 0 and score < 60:
        print('不及格')
    elif score >= 60 and score < 85:
        print('良')
    elif score >= 85 and score <= 100:
        print('优')

