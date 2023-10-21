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

def getLatestTid():
    url = 'https://www.manhuabudangbbs.com'
    getTid = ''
    mySession = requests.session()
    mySession.mount('http://', HTTPAdapter(max_retries = 3))
    mySession.mount('https://', HTTPAdapter(max_retries = 3))
    try:
        getHtml = mySession.request('GET', url=url, timeout=10)
        soup = BeautifulSoup(getHtml.text, 'html.parser')
        getTidA = soup.select('#tabswi1_B > div:nth-child(1) > div > dl > dt > a')[0].get('href')
        getTid = getTidA[13:getTidA.index('.html')]
    except requests.exceptions.RequestException as e:
        print(' 连接超时，重试中...')
    except:
        print(' 帖子不存在或其他错误')
    if getTid != '':
        return getTid
    
def main():
    # 46行是开始的tid（包含），48行是结束的tid（包含）
    # 网址格式：https://www.manhuabudangbbs.com/read-htm-tid-1000.html
    eachtid = 6011
    # 自动获取最新帖子的tid，如果手动设置请改成自己需要的数字，例如myLatestTid = 1000
    myLatestTid = int(getLatestTid())
    print('最新tid = ' + str(myLatestTid))
    while eachtid <= myLatestTid:
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
            writefile(str(eachtid) + ' ' + getName, getName + '\n\n' +  getAuthor +getTime + '\n\n' + getContent + '\n\n'  +url)
            eachtid = eachtid + 1
        except requests.exceptions.RequestException as e:
            print(str(eachtid) + ' 连接超时，重试中...')
        except:
            print(str(eachtid) + ' 帖子不存在或其他错误')
            eachtid = eachtid + 1
        time.sleep(2)
    print('爬虫结束') 
    os.system('pause')
        
if __name__ == '__main__':
    main()
    
