# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip3 install requests bs4

import requests
import time
from bs4 import BeautifulSoup

def writefile(fileName, filereadlines):
    #write file
    fileName = fileName.replace('/', ' ')
    with open(fileName + '.txt', mode='w', encoding='UTF-8') as newfile:
        newfile.writelines(filereadlines)

def main():
    for eachtid in range(4, 1971):
        url = 'https://www.manhuabudangbbs.com/read-htm-tid-' + str(eachtid) + '.html'
        print(url)
        getHtml = requests.get(url)
        try:
            soup = BeautifulSoup(getHtml.text, 'html.parser')
            getName = soup.select('#subject_tpc')[0].get_text()[:-7]
            getTime = '\n\n' + soup.select('#td_tpc > div.tipTop.s6 > span:nth-child(3)')[0].get_text() + '\n'
            getContent = soup.select('#td_tpc > div.tpc_content')
            getContent = str(getContent).replace('<br/>','\n')
            getContent = str(getContent).replace('<br>','\n')
            getContent = str(getContent).replace('</blockquote>','\n')
            getContent = str(getContent).replace('</div>','\n')
            getContent = BeautifulSoup(getContent, 'html.parser').get_text()
            writefile(getName, getName + '\n' + url + getTime + getContent)
        except:
            print(eachtid + 'Error')
        time.sleep(3)     
        
if __name__ == '__main__':
    main()
    
