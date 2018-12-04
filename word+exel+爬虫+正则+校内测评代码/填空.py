import re
import os
import xlwt
def num_1(data):
    if  "帅" in data:
        return 4
    else:
        return 0

def num_2(data):
    right = ['869','871','874','879','929']
    comm = re.compile("(\d+)", re.S)
    list1 = re.findall(comm, data)
    if len(list1) != 5:
        return 0
    else:
        j = 0
        for i in list1:
            if i != right[j]:
                return 0
            else:
                j = j+1

        return 6

def num_4(data):
    list1 =['mod(a*a%k,p/2,k)','mod(a*a%k,p/2,k)%k', 'mod(a*a%k,p>>1,k)%k','mod(a*a%k,p>>1,k)','mod(a%k,p/2,k)*mod(a%k,p/2,k)%k','mod(a%k,p/2,k)*mod(a%k,p/2,k)']
    data = data.replace(" ",'').replace("\n","")
    if data in list1:
        return 10
    else:
        return 0

if __name__ == "__main__":
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('sheet 1')
    list_dir = os.listdir("C:\\Users\\wxk\\Desktop\\蓝桥杯校内选拔赛")
    name_index = 1
    sheet.write(0, 0, '姓名')
    sheet.write(0, 1, '班级')
    sheet.write(0, 2, '账号')
    sheet.write(0, 3, "1.不可告人的秘密")
    sheet.write(0, 4, "2. 玩游戏")
    sheet.write(0, 6, "4. 递归版取余模运算")
    for i in list_dir:
        print(i)
        list_name = os.listdir("C:\\Users\\wxk\\Desktop\\蓝桥杯校内选拔赛"+"\\"+i)
        str1 = i.split("--")
        sheet.write(name_index, 0, str1[-1])
        sheet.write(name_index, 1, str1[0])
        sheet.write(name_index, 2, str1[1])
        # num_1,num_2,num_4 = 1,2,4
        for j in list_name:
            if "1.不可告人的秘密" in j:
                with open("C:\\Users\\wxk\\Desktop\\蓝桥杯校内选拔赛"+"\\"+i+"\\"+j,"r") as f:
                    data = f.read()
                sheet.write(name_index, 3, num_1(data))
            elif "2. 玩游戏" in j:
                with open("C:\\Users\\wxk\\Desktop\\蓝桥杯校内选拔赛"+"\\"+i+"\\"+j,"r") as f:
                    data = f.read()
                sheet.write(name_index, 4, num_2(data))
            elif "4. 递归版取余模运算" in j:
                with open("C:\\Users\\wxk\\Desktop\\蓝桥杯校内选拔赛"+"\\"+i+"\\"+j,"r") as f:
                    data = f.read()
                sheet.write(name_index, 6, num_4(data))
        name_index += 1

    wbk.save('test.xls')