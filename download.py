# -*- codeing = utf-8 -*-
# @Time : 2022/1/7 2:31
# @Author : LiuQi
# @File : download.py
# @Software : PyCharm
from selenium import webdriver
import time
import pandas as pd

from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

f = pd.read_csv(r'1.csv',names=['title','url','download'])
url = f['url'].values.tolist()
a = 0
# for i in range(0,len(url)):
#     if url[i] == 'https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&dbname=CJFD2010&filename=XSLT201002015':
#         print(i)
for i in range(474,len(url)):
    driver.get(url[i])
    try:
        driver.find_element_by_link_text('PDF下载').click()
    except:
        try:
            driver.find_element_by_link_text('CAJ下载').click()
        except:
            pass
    a+=1
    driver.implicitly_wait(2)
    if(a<2):
        driver.switch_to.window(driver.window_handles[-1])
        driver.implicitly_wait(2)
        driver.find_element_by_xpath("//div[@class='btn']/a[@id='Button2']").click()
    if a/20 != 0:
        time.sleep(10)

