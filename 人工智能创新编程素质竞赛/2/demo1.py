# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/7/5 17:14
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

# 输入：abcABC345^&*xyzXYZ
# 输出：defDEF345^&*abcABC

s = input()

for ch in s:
    if 'a' <= ch <= 'z': # 'a' => ASCII 97
        print(chr(97 + (ord(ch) + 3 - 97) % 26), end='')
    elif 'A' <= ch <= 'Z': # 'A' => ASCII 65
        print(chr(65 + (ord(ch) + 3 - 65) % 26), end='')
    else:
        print(ch, end='')
