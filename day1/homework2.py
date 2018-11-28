#!/usr/bin/env python
# -*- coding:UTF-8 -*-

zone = {'浙江':{'杭州':['西湖', '下城', '滨江'], '温州': ['龙湾', '鹿城', '瓯海']},
        '黑龙江':{'哈尔滨':['道外','道里'],'牡丹江':['爱民','东安']}}

s_list = list(zone.keys())


for i in s_list:
    print(i)
a = input("请输入省名")
if a in s_list:
    shi_list = list(zone[a].keys())
    for i in shi_list:
        print(i)
    b = input('请输入市名')
    if b in shi_list:
        for i in zone[a][b]:
            print(i)
        c = input("请输入区")
        if c in zone[a][b]:
            print("有哦")
        else:
            print("没有这个区")
    else:
        print("没有这个市")

else:
    print("没有这个省！")