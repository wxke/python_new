#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
a = webdriver.Firefox()
a.get("https://www.baidu.com")
b = a.find_element_by_id('kw')
b.send_keys("python")
b.send_keys(Keys.ENTER)
wait = WebDriverWait(a,10)
wait.until(EC.presence_of_all_elements_located((By.ID,'content_left')))
print(a.current_url)
print(a.get_cookies())
print(a.page_source)
a.close()
