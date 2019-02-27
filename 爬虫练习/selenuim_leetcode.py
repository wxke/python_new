from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
str1 = 'https://leetcode-cn.com'
list1 = []
def login(url):
    browser.get(url)
    input_user = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#app > div > div.sign-in-wrapper__2SAX > div > div.placeholder-bottom__2SYS > div > div > div > form > span:nth-child(1) > input')))
    input_password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#app > div > div.sign-in-wrapper__2SAX > div > div.placeholder-bottom__2SYS > div > div > div > form > span:nth-child(3) > input')))
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div > div.sign-in-wrapper__2SAX > div > div.placeholder-bottom__2SYS > div > div > div > button')))
    input_user.send_keys("你的账号")
    input_password.send_keys("你的密码")
    time.sleep(2)
    button.click()
def find_topic():
    sum_page = 2
    count = 0
    for i in range(0,sum_page):
        div = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#question-app > div > div:nth-child(2) > div.question-list-base')))
        time.sleep(2)
        lis = browser.find_elements_by_tag_name('tr')
        for j in lis:
            source_text = j.get_attribute('innerHTML')
            if 'value="ac"' in source_text:
                con = re.compile('<td label=.*?>(.*?)</td>.*?<div><a href="(.*?)">(.*?)</a>&nbsp;',re.S)
                res = re.findall(con,source_text)
                list1.append(res)
                count +=1
        if i != sum_page-1:
            button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-app > div > div:nth-child(2) > div.question-list-base > div.table-responsive.question-list-table > table > tbody.reactable-pagination > tr > td > span.pagination-buttons > a.reactable-next-page')))
            button.click()
    print(count)
def load(list1):
    cont = 0
    for i in list1:
        name = './test-leetcode/' + i[0][0] + " " +i[0][2] + '.txt'
        url_code = str1 + i[0][1]+'/submissions/'
        code = find_code(url_code)
        print(code)
        with open(name,'w',encoding='utf-8') as f:
            f.write(i[0][2] + '\n' + code)
def find_code(url):
    browser.get(url)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#question-detail-main-tabs > div.tab-pane__280T.css-xailxq-TabContent.e5i1odf5 > div > div')))
    time.sleep(2)
    tbody = browser.find_element_by_class_name('submissions__23-1')
    a_list = tbody.find_elements_by_tag_name('a')
    for i in a_list:
        te = i.get_attribute('innerHTML')
        if i.get_attribute('text') == '通过':
            res = i.get_attribute('href')
            break
    browser.get(res)
    cls = browser.find_elements_by_class_name("ace_line_group")
    code = ''
    for i in cls:
        code += i.text + '\n'
    return code
if __name__ =='__main__':
    url_login = 'https://leetcode-cn.com/accounts/login/'
    login(url_login)
    find_topic()
    load(list1)
