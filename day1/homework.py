#!/usr/bin/env python
# -*- coding:UTF-8 -*-




while True:
    user = open("nam.txt", 'r')
    lock = open('look.txt', 'r+')
    user_flag = False
    username = input("请输入用户名")
    for j in lock:
        j= j.split()
        if username == j[0]:
            print("该用户已被锁定")
            user_flag = True
            break
    if user_flag == True:
        continue
    for i in user:
        i = i.split()
        if username == i[0]:
            for ci in range(3):
                password = input("请输入密码")
                if password == i[1]:
                    print("欢迎登录")
                    break
                else:
                    print("你还有",2-ci,"机会输入密码")
            else:
                print("用户被锁定")
                lock.write(username+'\n')




