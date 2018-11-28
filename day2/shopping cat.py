#!/usr/bin/env python
# -*- coding:UTF-8 -*-

shops = [[1,'iPhone',5000],[2,'cat',222],[3,'bick',2555]]
shop_list = []
a = int(input("输入你的工资:"))
c = 1

while True:
    # for i in range(3):
    #     for j in range(3):
    #         print(shops[i][j])
    for i in shops:
       print(i)

    c = input('输入你要购买的商品编号，结束请按q')
    if c=='q':
        break;
    if a >= shops[int(c)-1][2]:
        a = a-shops[int(c)-1][2]
        shop_list.append(shops[int(c)-1])
    else:
        print("钱不够哦 滚犊子！")

print("这是你的购物清单和余额！")
s =""
for i in shop_list:
    li = i[:]
    for j in li:
        s = s + str(j) +" "
    print(s)
    s=""

print("你的余额",a)
