# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip3 install requests
# pip3 install bs4

import requests
from bs4 import BeautifulSoup

def writefile(fileName, filereadlines):
    #write file
    fileName = fileName.replace('/', ' ')
    with open(fileName + '.txt', mode='w', encoding='UTF-8') as newfile:
        newfile.writelines(filereadlines)

def main():
    tid = [1000,1001]
    for eachtid in tid:
        url = 'https://www.manhuabudang.com/read.php?tid=' + str(eachtid)
        print(url)
        getHtml = requests.get(url)
        soup = BeautifulSoup(getHtml.text, 'html.parser')
        getName = soup.find(attrs={'id' : 'subject_tpc'}).string
        getTime = '\n\n' + soup.find(attrs={'id' : 'readfloor_tpc'}).find(attrs={'class' : 'tipTop s6'}).findAll('span')[-1].get_text() + '\n'
        getContent = str(soup.find(attrs={'id' : 'read_tpc'}))
        getContent = getContent.replace('<br/>',"\n")
        getContent = BeautifulSoup(getContent, 'html.parser').get_text()
        writefile(getName, url + getTime + getContent)
        
if __name__ == '__main__':
    main()
    
