import requests
import hashlib
import re
import os
def get_csrf(s):
    url = 'http://10.90.16.100/csrf.php'
    request_csrf = s.get(url)
    data = request_csrf.text
    com = re.compile('.*?value="(.*?)" class')
    value = re.findall(com,data)

    return value[0]
def login(s,name,password):
    url = "http://10.90.16.100/login.php"
    csrf_val = get_csrf(s)
    data = {
        'user_id': name,
        'password': password,
        'submit': '',
        'csrf': csrf_val,
    }
    resquest = s.post(url,data=data)

a = 0
def sumbit(s,pid,txt):

    url = "http://10.90.16.100/submit.php"
    csrf_val = get_csrf(s)
    data = {
        'cid': '1014',
        'pid': pid ,
        'language': '1',
        'source': txt,
        'csrf':csrf_val,
    }
    request = s.post(url,data=data)
    global a
    print(a)
    a = a+1
def logout(s):
    request =s.get(url='http://10.90.16.100/logout.php')

if __name__ == "__main__":
    s = requests.Session()
    list_dir = os.listdir("C:\\Users\\wxk\\Desktop\\蓝桥杯校内选拔赛")
    for i in list_dir:
        list_name = os.listdir("C:\\Users\\wxk\\Desktop\\蓝桥杯校内选拔赛" + "\\" + i)
        name = i.split("--")
        name = name[1]
        print(name)
        password = 'e10adc3949ba59abbe56e057f20f883e'
        nj = i[:2]
        print(i)
        login(s, name, password)
        for j in list_name:

            # if "5. 回文日期" in j:
            #     with open("C:\\Users\\wxk\\Desktop\\蓝桥杯校内选拔赛"+"\\"+i+"\\"+j,"r") as f:
            #         data = f.read()
            #         pid ="0"
            #         sumbit(s,pid,data)
            # if "6. 2 的幂" in j:
            #     with open("C:\\Users\\wxk\\Desktop\\蓝桥杯校内选拔赛"+"\\"+i+"\\"+j,"r") as f:
            #         data = f.read()
            #         pid ="1"
            #         sumbit(s,pid,data)
            if  "7. balabala(低年级组-大一" in j and ("孙亮" not in j):
                with open("C:\\Users\\wxk\\Desktop\\蓝桥杯校内选拔赛"+"\\"+i+"\\"+j,"r") as f:
                    data = f.read()
                    pid = "2"
                    sumbit(s,pid,data)
            # if nj == '17' and "8. 数独(高年级组-大二)" in j:
            #     with open("C:\\Users\\wxk\\Desktop\\蓝桥杯校内选拔赛"+"\\"+i+"\\"+j,"r") as f:
            #         data = f.read()
            #         pid = "3"
            #         sumbit(s,pid, data)
            # if "9. 汉明距离" in j:
            #     with open("C:\\Users\\wxk\\Desktop\\蓝桥杯校内选拔赛"+"\\"+i+"\\"+j,"r") as f:
            #         data = f.read()
            #         pid = "4"
            #         sumbit(s,pid, data)

