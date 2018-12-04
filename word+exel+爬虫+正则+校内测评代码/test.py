#!/usr/bin/env python
# import urllib,re

import os
from win32com import client as wc
list_dir = os.listdir("C:\\Users\\wxk\\Desktop\\蓝桥杯校内选拔赛")
print(list_dir)
for i in list_dir:
    lis = os.listdir("C:\\Users\\wxk\\Desktop\\蓝桥杯校内选拔赛\\"+i)
    print(i)
    for j in lis:
        if j[-4:] != '.txt':
            word = wc.Dispatch("Word.Application")
            try:
                print("1")
                doc = word.Documents.Open("C:\\Users\\wxk\\Desktop\\蓝桥杯校内选拔赛\\"+i+"\\"+j)
                doc.SaveAs("C:\\Users\\wxk\\Desktop\\蓝桥杯校内选拔赛\\"+i+"\\"+j[:-4]+".txt", 4)
                os.remove("C:\\Users\\wxk\\Desktop\\蓝桥杯校内选拔赛\\"+i+"\\"+j)

            except:
                doc = word.Documents.Open("C:\\Users\\wxk\\Desktop\\蓝桥杯校内选拔赛\\" + i + "\\" + j)
                doc.SaveAs("C:\\Users\\wxk\\Desktop\\蓝桥杯校内选拔赛\\" + i + "\\" + j[:-4] + ".txt", 4)
                os.remove("C:\\Users\\wxk\\Desktop\\蓝桥杯校内选拔赛\\" + i + "\\" + j)
                range = doc.Range(doc.Content.Start, doc.Content.End)
                text = range.__str__()
                print(text)
                print("2")
                with open("C:\\Users\\wxk\\Desktop\\蓝桥杯校内选拔赛\\"+i+"\\"+j[:-4]+".txt","w") as f:
                    f.write(text)
                os.remove("C:\\Users\\wxk\\Desktop\\蓝桥杯校内选拔赛\\" + i + "\\" + j)
            doc.Close()

    # range = doc.Range(doc.Content.Start, doc.Content.End)
    # text = range.__str__()
    # print(text)


print("end")
#
# with open("17级计算机一班--2018120247--孙亮--1.不可告人的秘密","r") as f:
#     print(f.read())








