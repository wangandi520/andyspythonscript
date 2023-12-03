# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip3 install requests bs4

import requests
import time
import datetime
import os
import sys
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from pathlib import Path

def validFileName(fileName):
    # 把不能作为文件的字符替换成空格
    for each in fileName:
        if each in '\/:*?"<>|,':
            fileName = fileName.replace(each, ' ')
    return fileName
    
def writefile(fileName, filereadlines):
    #write file
    with open(fileName, mode='w', encoding='UTF-8') as newfile:
        newfile.writelines(filereadlines)

def readfile(filename):
    # readfile
    with open(filename, mode='r', encoding='UTF-8') as file:
        filereadlines = file.readlines()
    return filereadlines
    
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
        
def updateTidEachtime(latestTid):
    myReadFile = readfile(sys.argv[0])
    newFile = []
    for i in range(0, len(myReadFile)):
        if i == 63:
            newFile.append('    eachtid = ' + str(latestTid) + '\n')
        else:
            newFile.append(myReadFile[i])
    writefile(Path(sys.argv[0]).name, newFile)
    
def main():
    # 设置文件路径，如'd:\\new\\'，'/srv/ftp/'
    myPath = ''
    # 64行是开始的tid（包含），66行是结束的tid（包含）
    eachtid = 4
    # 自动获取最新帖子的tid，如果手动设置请改成自己需要的数字，例如myLatestTid = 1000
    myLatestTid = int(getLatestTid())
    print('开始tid = ' + str(eachtid) + ' 最新tid = ' + str(myLatestTid))
    # 是否更新脚本的起始tid为最新tid，适用于每天定时运行
    
    while eachtid <= myLatestTid:
        url = 'https://www.manhuabudangbbs.com/read-htm-tid-' + str(eachtid) + '.html'
        mySession = requests.session()
        mySession.mount('http://', HTTPAdapter(max_retries = 3))
        mySession.mount('https://', HTTPAdapter(max_retries = 3))
        try:
            getHtml = mySession.request('GET', url=url, timeout=10)
            soup = BeautifulSoup(getHtml.text, 'html.parser')
            getName = validFileName(soup.select('#subject_tpc')[0].get_text()[:-7])
            print(str(eachtid) + ' ' + getName + ' ' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            getAuthor = soup.select('.readName.b a')[0].get_text() + ' '
            getTime = soup.select('#td_tpc > div.tipTop.s6 > span:nth-child(3)')[0].get_text() + '\n'
            getContent = soup.select('#td_tpc > div.tpc_content')
            # 替换成换行
            myReplace = ['<br/>', '<br>', '</blockquote>', '</div>']
            for eachReplace in myReplace:
                getContent = str(getContent).replace(eachReplace, '\n')
            getContent = BeautifulSoup(getContent, 'html.parser').get_text()
            writefile(myPath + str(eachtid) + ' ' + getName + '.txt', getName + '\n\n' +  getAuthor +getTime + '\n\n' + getContent + '\n\n'  +url)
            eachtid = eachtid + 1
        except requests.exceptions.RequestException as e:
            print(str(eachtid) + ' 连接超时，重试中...')
        except:
            print(str(eachtid) + ' 帖子不存在或其他错误')
            eachtid = eachtid + 1
        time.sleep(2)
    print('爬虫结束') 
    
    if True:
        updateTidEachtime(myLatestTid + 1)
        print('爬虫下次开始tid = ' + str(myLatestTid + 1))
        
    os.system('pause')
        
if __name__ == '__main__':
    main()
    
