# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip3 install requests bs4

import requests
from bs4 import BeautifulSoup

def writefile(fileName, filereadlines):
    #write file
    fileName = fileName.replace('/', ' ')
    with open(fileName + '.txt', mode='w', encoding='UTF-8') as newfile:
        newfile.writelines(filereadlines)

def main():
    tid = [4]
    for eachtid in tid:
        url = 'https://www.manhuabudangbbs.com/read-htm-tid-' + str(eachtid) + '.html'
        print(url)
        getHtml = requests.get(url)
        soup = BeautifulSoup(getHtml.text, 'html.parser')
        getName = soup.select('#subject_tpc')[0].get_text()[:-7]
        getTime = '\n\n' + soup.select('#td_tpc > div.tipTop.s6 > span:nth-child(3)')[0].get_text() + '\n'
        getContent = soup.select('#td_tpc > div.tpc_content')
        getContent = str(getContent).replace('<br/>',"\n")
        getContent = BeautifulSoup(getContent, 'html.parser').get_text()
        writefile(getName, url + getTime + getContent)
        
if __name__ == '__main__':
    main()
    
