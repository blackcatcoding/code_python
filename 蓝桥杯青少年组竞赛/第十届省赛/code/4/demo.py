# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/25 19:38
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import random

f = open('userpass.txt', 'r', encoding='utf-8')

username, passwd = f.read().split(',')

f.close()
# print(username, passwd)
yzm = random.randint(100000, 1000000)

print('您的验证码：', yzm)

input_name = input('请输入用户名：')
input_passwd = input('请输入密码：')
input_yzm = input('请输入验证码：')

if input_name != username or input_passwd != passwd or input_yzm != str(yzm):
    print('身份验证失败')
else:
    print('身份验证通过，欢迎登陆')

    while True:

        f = open('goods.txt', 'r', encoding='utf-8')
        goods_info = f.read().split(';')
        f.close()

        for good in goods_info:
            print(good)

        op = input('::')

        if op == 'add':
            good_num = input('商品编号：')
            good_name = input('商品名称：')
            good_type = input('商品类型：')
            good_count = input('商品库存：')

            new_good_info = ';' + good_num + ',' + good_name + ',' + good_type + ',' + good_count

            f = open('goods.txt', 'a', encoding='utf-8')
            f.write(new_good_info)

            f.close()

        if op == 'count':
            f = open('goods.txt', 'r', encoding='utf-8')
            goods_info = f.read().split(';')
            cnt = 0
            for good in goods_info:
                cur_good_li = good.split(',')
                try:
                    cnt += int(cur_good_li[3])
                except:
                    print('输入库存信息不合法')

            print(cnt)







