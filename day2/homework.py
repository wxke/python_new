#!/usr/bin/env python
# -*- coding:UTF-8 -*-

a = input("用户or商家")
shang_dict={}
if a == '用户':
    yimai_dict={}
    shangpin = open('shangpin.txt','r')
    for i in shangpin:
        key,value = i.split(':')
        shang_dict[key]=value.strip()
    yue = open('money.txt','r+')
    money = 0
    for i in yue:
        i = i.split()
        money = int(i[0])
    if money == 0:
        money = int(input("第一次登录，输入你的余额："))
        yue.write(str(money)+'\n')

    for i in shang_dict:
        print(i,shang_dict[i])
    while money >=0:
        hao = input("输入要买商品的名称：/q退出")
        if hao == 'q':
            break
        if hao not in shang_dict:
            print("没有这件商品")
        elif money >= int(shang_dict[hao]):
            print("已购买",hao)
            money = money - int(shang_dict[hao])
            yimai_dict[hao]= shang_dict[hao]
        else:
            print("买不起咯~~~~")
    yue.seek(0)
    yue.truncate()
    yue.write(str(money) + '\n')
    for i in yimai_dict:
        print(i,yimai_dict[i])

    print("you's money",money)
    yue.close()
    shangpin.close()
elif a == '商家':
    name = input("请输入要修改价格的商品名称")
    shangpin = open('shangpin.txt','r+')
    for i in shangpin:
        key,value = i.split(':')
        shang_dict[key]=value.strip()

    shang_dict[name] = input("输入价格")
    shangpin.seek(0)
    shangpin.truncate()
    for i in shang_dict.keys():
        shangpin.write(i+":"+shang_dict[i]+'\n')

    for i in shang_dict:
        print(i,shang_dict[i])
