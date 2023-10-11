# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip3 install requests bs4

import requests
import time
import datetime
import os
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter

def validFileName(fileName):
    # 把不能作为文件的字符替换成空格
    for each in fileName:
        if each in '\/:*?"<>|,':
            fileName = fileName.replace(each, ' ')
    return fileName
    
def writefile(fileName, filereadlines):
    #write file
    fileName = validFileName(fileName)
    with open(fileName + '.txt', mode='w', encoding='UTF-8') as newfile:
        newfile.writelines(filereadlines)

def main():
    # 第二个数字tid
    # 网址格式：https://www.manhuabudangbbs.com/read-htm-tid-1000.html
    for eachtid in range(1, 2000):
        url = 'https://www.manhuabudangbbs.com/read-htm-tid-' + str(eachtid) + '.html'
        mySession = requests.session()
        mySession.mount('http://', HTTPAdapter(max_retries = 3))
        mySession.mount('https://', HTTPAdapter(max_retries = 3))
        try:
            getHtml = mySession.request('GET', url=url, timeout=10)
            soup = BeautifulSoup(getHtml.text, 'html.parser')
            getName = soup.select('#subject_tpc')[0].get_text()[:-7]
            print(str(eachtid) + ' ' + getName + ' ' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            getAuthor = soup.select('.readName.b a')[0].get_text() + ' '
            getTime = soup.select('#td_tpc > div.tipTop.s6 > span:nth-child(3)')[0].get_text() + '\n'
            getContent = soup.select('#td_tpc > div.tpc_content')
            # 替换成换行
            myReplace = ['<br/>', '<br>', '</blockquote>', '</div>']
            for eachReplace in myReplace:
                getContent = str(getContent).replace(eachReplace, '\n')
            getContent = BeautifulSoup(getContent, 'html.parser').get_text()
            writefile(getName, getName + '\n\n' +  getAuthor +getTime + '\n\n' + getContent + '\n\n'  +url)
        except requests.exceptions.RequestException as e:
            print(str(eachtid) + ' 连接超时，请修改脚本tid后重新运行')
            os.system('pause')
        except:
            print(str(eachtid) + ' 帖子错误')
        time.sleep(2)     
        
if __name__ == '__main__':
    main()
    
