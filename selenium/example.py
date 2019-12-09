#coding:utf8

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import platform
import traceback
import time
from prettytable import PrettyTable
CHROMEDRIVER_WIN = ''
CHROMEDRIVER_LINUX = './chromedriver'
WAITTIME = 20
URL = "https://weixin.sogou.com"


class Driver1():
    _instance = None
    driver = None

    def __new__(cls,*args,**kwargs):
        if not cls._instance:
            cls._instance = super(Driver,cls).__new__(cls,*args,**kwargs)
            cls.driver = cls._instance.initdriver()


    def initdriver(self):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        option.add_argument('--headless')
        option.add_argument('--disable-gpu')
        option.add_argument('--no-sandbox')  # 这个配置很重要
        option.add_argument('--incognito')  # 启用无痕模式
        sysinfo = platform.platform()
        if 'windows' in sysinfo.lower():
            driver = webdriver.Chrome(executable_path = CHROMEDRIVER_WIN, \
                                      chrome_options=option)
        else:
            driver = webdriver.Chrome(executable_path = CHROMEDRIVER_LINUX, \
                                      chrome_options=option)
        return driver
    
    def quitdriver(self):
        self.driver.delete_all_cookies()
        self.driver.quit()

class Driver():

    def __init__(self):
        self._driver = None

    @property
    def driver(self):
        if self._driver == None:
            option = webdriver.ChromeOptions()
            option.add_argument('disable-infobars')
            option.add_argument('--headless')
            option.add_argument('--disable-gpu')
            option.add_argument('--no-sandbox')  # 这个配置很重要
            option.add_argument('--incognito')  # 启用无痕模式
            sysinfo = platform.platform()
            if 'windows' in sysinfo.lower():
                self._driver = webdriver.Chrome(executable_path=CHROMEDRIVER_WIN, \
                                          chrome_options=option)
            else:
                self._driver = webdriver.Chrome(executable_path=CHROMEDRIVER_LINUX, \
                                          chrome_options=option)

        return self._driver

    def __delete__(self, instance):
        self._driver.delete_all_cookies()
        self._driver.quit()


def waitid(driver,id):
    try:
        WebDriverWait(driver,WAITTIME,1).until(
            EC.presence_of_element_located((By.ID,id))
        )
    except:
        traceback.print_exc()
        return 0,'wait id 20s timeout'
    return 1,'wait id finish'

def waitcss(driver,css):
    try:
        WebDriverWait(driver,WAITTIME,1).until(
                lambda x: x.find_element_by_css_selector(css)
        )
    except:
        traceback.print_exc()
        return 0,'wait css 20s timeout'
    return 1,'wait css finish'

def waitxpath(driver,xpath):
    try:
        WebDriverWait(driver,WAITTIME,1).until(
                lambda x: x.find_element_by_xpath(xpath)
        )
    except:
        traceback.print_exc()
        return 0,'waitidit xpath 20s timeout'
    return 1,'wait xpath finish'



def main():
    querything = input("请输入要查询的内容: ")
    MyDriver = Driver()
    driver = MyDriver.driver
    driver.get(URL)
    queryid = 'query'
    print('waitid')
    waitid(driver,queryid)
    queryinput = driver.find_element_by_id(queryid)
    queryinput.clear()
    queryinput.send_keys(querything)
    print('\n------------------------------------------------\n')
    print(driver.page_source)

    querybutton = driver.find_element_by_class_name('swz')
    ActionChains(driver).move_to_element(querybutton).click(querybutton).perform()

    time.sleep(3)
    table = PrettyTable(['文章标题','文章简介','来源与时间'])

    print('find xpath')
    print('\n------------------------------------------------\n')
    print(driver.page_source)
    lis = driver.find_elements_by_xpath("//ul[contains(@class,'news-list')]/child::li")

    for li in lis:
        print(li)
        texts = li.text.split('\n')
        if len(texts)>=3:
            print(texts[0],texts[1],texts[2])
            table.add_row([texts[0],texts[1],texts[2]])

    print(table)


if __name__ == '__main__':
    main()
