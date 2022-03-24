# -*- coding=utf-8 -*-

import json
import time
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def info(url):
    """
    调用selenium,开启selenium的日志收集功能，收集所有日志，并从中挑出network部分，分析格式化数据，传出
    :param url:
    :return:
    """
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option('w3c', False)
    caps = {
        'browserName': 'chrome',
        'loggingPrefs': {
            'browser': 'ALL',
            'driver': 'ALL',
            'performance': 'ALL',
        },
        'goog:chromeOptions': {
            'perfLoggingPrefs': {
                'enableNetwork': True,
            },
            'w3c': False,
        },
    }
    driver = webdriver.Chrome(desired_capabilities=caps, chrome_options=chrome_options)
    driver.get(url)
    time.sleep(5)
    # input = driver.find_element_by_xpath('/html/body')
    # time.sleep(2)
    # for i in range(22):
        # input.send_keys(Keys.LEFT)
        # time.sleep(0.2)
    myrequests = []
    response = []
    for log in driver.get_log('performance'):
        print(log)
        x = json.loads(log['message'])['message']
        if x["method"] == "Network.responseReceived":
            try:
                ip = x["params"]["response"]["remoteIPAddress"]
            except BaseException as p:
                ip = ""
            try:
                port = x["params"]["response"]["remotePort"]
            except BaseException as f:
                port = ""
            response.append(
                [
                    x["params"]["response"]["url"],
                    ip,
                    port,
                    x["params"]["response"]["status"],
                    x["params"]["response"]["statusText"],
                    x["params"]["type"]
                ]
            )
        elif x["method"] == "Network.requestWillBeSent":
            myrequests.append(
                [
                    x["params"]["request"]["url"],
                    x["params"]["initiator"]["type"],
                    x["params"]["request"]["method"],
                    x["params"]["type"]
                ]
            )
        else:
            pass
    newlist = []
    for iqurl in myrequests:
        qwelist = [iqurl]
        for ipurl in response:
            if iqurl[0] == ipurl[0]:
                qwelist.append(ipurl)
            else:
                pass
        newlist.append(qwelist)
    for ipurl in response:
        p = 0
        for i in newlist:
            if len(i) == 1:
                pass
            else:
                if ipurl == i[1]:
                    p += 1
                else:
                    pass
        if p == 0:
            newlist.append(ipurl)
        else:
            pass
    returnList = []
    for a in newlist:
        dic = {
            "url": "",
            "method": "",
            "status": "",
            "statusText": "",
            "type": "",
            "initiator": "",
            "remoteIPAddress": "",
            "remotePort": ""

        }
        if len(a) == 2 and '?sv=' in a[0][0]:
            dic["url"] = a[0][0]
            dic["initiator"] = a[0][1]
            dic["method"] = a[0][2]
            dic["type"] = a[0][3]
            #dic["netloc"] = netloc_info(a[0][0])
            dic["remoteIPAddress"] = a[1][1]
            dic["remotePort"] = a[1][2]
            dic["status"] = a[1][3]
            dic["statusText"] = a[1][4]
            returnList.append(dic)
        elif len(a) == 1:
            if len(a[0]) == 4 and '?sv=' in a[0][0]:
                dic["url"] = a[0][0]
                #dic["netloc"] = netloc_info(a[0][0])
                dic["initiator"] = a[0][1]
                dic["method"] = a[0][2]
                dic["type"] = a[0][3]
                returnList.append(dic)
            elif len(a[0]) == 6 and '?sv=' in a[0][0]:
                dic["url"] = a[0][0]
                #dic["netloc"] = netloc_info(a[0][0])
                dic["remoteIPAddress"] = a[0][1]
                dic["remotePort"] = a[0][2]
                dic["status"] = a[0][3]
                dic["statusText"] = a[0][4]
                dic["type"] = a[0][5]
                returnList.append(dic)
            else:
                pass
        else:
            pass
    # for a in newlist:
        # if '?sv=' in a[0][0]:
            # print(a[0][4])
            # returnList.append(a[0][0])
    for each in returnList:
        print(each)
        newdriver = webdriver.Chrome()
        newdriver.get(each["url"])
        time.sleep(2)
        img = newdriver.find_element_by_xpath('/html/body/img')
        print(img)
        img.context_click()
        #src = img[0].get_attribute('src')
      
        # driver.close()
        # driver.quit()
        # src = newdriver.find_element_by_tag_name('img')
        # print(src)
        # response = requests.get(src)
        # with open('picture.jpg', 'wb') as file:
            # file.write(response.content)
    driver.close()
    driver.quit()
    return returnList


if __name__ == '__main__':
    bookID = 'e18cc9ec-5e31-4593-d97d-08d9fcfcff4f'
    info('https://ebook.tongli.com.tw/reader/FireBase2.html?bookID=' + bookID + '&isLogin=false&isSerial=true')