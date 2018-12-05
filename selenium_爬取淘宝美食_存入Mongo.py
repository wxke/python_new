# import requests
# import selenium
# import lxml
# from pyquery import PyQuery as pq
# from selenium import webdriver
# from bs4 import BeautifulSoup
# import redis
# # import django
# # from flask import Flask
# import pymongo
# import pymysql
# import jupyter
# import pika
# import threading
# import time
# soup = BeautifulSoup("<html></html>","lxml")
# print(soup)
# a= webdriver.Firefox()
# import docx
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import pymongo
MONGO_URL="localhost"
MONGO_DB = 'taobao'
MONGO_TABLE = 'product'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

def open_url():
    browser.get("https://www.taobao.com/")

    input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#q')))
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
    input.send_keys("美食")
    button.click()
    if wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))):
        print("aaa")
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#q')))
        input.clear()
        input.send_keys("美食")
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_SearchForm > button')))
        button.click()
        sum_page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total')))

        sum_page = int(re.findall("(\d+)",sum_page.text)[0])

        return sum_page
    else :
        print("查找失败")


def download_info(sum_page):
    for i in range(1,sum_page):
        print("1111")
        div = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#q')))
        lis = browser.find_elements_by_class_name("J_MouserOnverReq")
        for j in lis:
            info = {
                'title': j.find_element_by_class_name("title").text,
                'price': j.find_element_by_class_name("price").text,
                'deal' : j.find_element_by_class_name("deal-cnt").text[:-3]
            }
            print(info)
            db[MONGO_TABLE].insert(info)
        next_page(i+1)


def next_page(Current_page):
    print(Current_page)
    input_a = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > input')))
    input_a.clear()
    input_a.send_keys(Current_page)
    button_a = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
    button_a.click()
    wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(Current_page)))

if __name__ == "__main__":
    sum_page =open_url()
    download_info(sum_page)
    browser.close()

























