#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import re
import requests
from requests.exceptions import RequestException
def open_one_pape(url):
    headers = {
        'Host':'maoyan.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
        'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, * / *;q = 0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding':'gzip, deflate',
        'Referer': 'http://maoyan.com/board',
        'Cookie': '__mta=212048811.1538625750548.1538625751737.1538625752995.3; uuid_n_v=v1; uuid=4F1439E0C78A11E88614CBD339395C0BBBC160C5887642E6AD6CDC165069DA38; _csrf=d4925f71d9310b3dc21626a8082186ff53af370437720ca4b92f87e56157f14c; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=1663d3dc32ec8-0d57c5046bb445-4c312878-100200-1663d3dc32fc8; _lxsdk_s=1663d3dc330-2b3-ebb-c75%7C%7C8; _lxsdk=4F1439E0C78A11E88614CBD339395C0BBBC160C5887642E6AD6CDC165069DA38; __mta=212048811.1538625750548.1538625750548.1538625751737.2',
        'Connection':'keep - alive',
        'Upgrade - Insecure - Requests': '1',
        'Cache - Control': 'max - age = 0'
    }
    try:
        request = requests.get(url,headers = headers)
        req = request.text
        re_test(req)
    except RequestException as e:
        print('出错')

def re_test (req):

    comm = re.compile('<dd>.*?board-inde.*?>(.*?)</i>.*?tit'
                      +'le="(.*?)".*?data-src="(.*?)".*?class="star">'
                      +'(.*?)</p>.*?class="releasetime">(.*?)</p>.*?"integer"'
                      +'>(.*?)</i>.*?class="fraction">(.*?)</i>.*?</dd>',re.S)
    list = re.findall(comm,req)

    for i in list:
        str = i[0]+' '+i[1]+' '+i[2]+' '+i[3].strip()+' '+i[4].strip()+' '+i[5]+i[6]+'\n'
        f = open("test.txt",'a',encoding='utf-8')
        f.write(str)
        f.close()

if __name__ == '__main__':
    for i in range(10):
        url = 'http://maoyan.com/board/4?offset='+str(i*10)
        open_one_pape(url)
