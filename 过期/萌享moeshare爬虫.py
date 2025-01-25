# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip3 install requests bs4

import requests
import time
import re
from bs4 import BeautifulSoup

def validFileName(oldFileName):
    # '/ \ : * ? " < > |'
    # 替换为下划线
    validChars = r"[\/\\\:\*\?\"\<\>\|]"  
    newFileName = re.sub(validChars, "_", oldFileName)
    return newFileName
    
def writefile(fileName, filereadlines):
    #write file
    fileName = validFileName(fileName)
    with open(fileName + '.html', mode='w', encoding='UTF-8') as newfile:
        newfile.writelines(filereadlines)

def main():
    myCookie = ""

    myAgent = ""
    
    myProxies = {
    'https': '',
    'http': ''  
    }
    # myProxies = {
        # 'https': 'http://127.0.0.1:7890',
        # 'http': 'http://127.0.0.1:7890'  
    # }
    
    headers = {"User-Agent": myAgent,
           "Cookie": myCookie + str(int(round(time.time()))) + "; 8017a_lastvisit=0	" + str(int(round(time.time()))) + "	/index.php"}
    #for eachtid in range(1, 1974):
    for eachtid in [247766]:
        url = 'https://moeshare.cc/read-htm-tid-' + str(eachtid) + '.html'
        getHtml = requests.get(url, proxies = myProxies, headers=headers)
        allContent = ''
        soup = BeautifulSoup(getHtml.text, 'html.parser')
        getTitle = '<br/>'.join(soup.select('#subject_tpc')[0].contents)
        allContent = allContent + getTitle + '<br/>'
        print(url + ' ' + getTitle)
        getName = '<br/>'.join(soup.select('div.readName.b > a')[0].contents)
        allContent = allContent + getName + '<br/>'
        getTime = '<br/>'.join(soup.select('#td_tpc > div.tipTop.s6 > span:nth-child(3)')[0].contents)
        allContent = allContent + getTime + '<br/>'
        getContent = '<br/>'.join(str(each) for each in soup.select('#read_tpc')[0].contents)
        allContent = allContent + getContent + '<br/>'
        allContent = allContent + '本帖抓取时间 ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '<br/>'
        writefile(getTitle, allContent)
        time.sleep(2)     
        
if __name__ == '__main__':
    main()
    
