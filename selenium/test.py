#coding=utf8
#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox') # 这个配置很重要
chrome_options.add_argument('--incognito') # 启用无痕模式
#client = webdriver.Chrome(chrome_options=chrome_options, executable_path='./chromedriver')    # 如果没有把chromedriver加入到PATH中，就需要指明路径
client = webdriver.Chrome(chrome_options=chrome_options)    # 如果没有把chromedriver加入到PATH中，就需要指明路径

cookies = client.get_cookies()
print("main: cookies = {%s}" % cookies)
client.delete_all_cookies()

client.get("http://select.pdgzf.com/villageLists")
#print(client.find_element(By.CLASS_NAME, 'village-house-lists'))
#print (client.page_source.encode('utf-8'))
#page = client.page_source.encode('utf-8')
time.sleep(3)
page = client.page_source
bsobj = BeautifulSoup(page,'lxml')
#print(page)
head = bsobj.head

villages = bsobj.find("ul",{"class":"village-house-lists"}).findAll('li')
print(len(villages))
for village in villages:
    print(village.get_text())
    village_info = village.find("div")
    print(village.h4.get_text())
#print(village-house-lists.get_text())
#print(head)
#print(village)


client.quit()

