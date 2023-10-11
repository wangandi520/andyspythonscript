# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip3 install requests bs4

import requests
import time
from bs4 import BeautifulSoup

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
    for eachtid in range(1, 500):
        url = 'https://www.manhuabudangbbs.com/read-htm-tid-' + str(eachtid) + '.html'
        getHtml = requests.get(url)
        try:
            soup = BeautifulSoup(getHtml.text, 'html.parser')
            getName = soup.select('#subject_tpc')[0].get_text()[:-7]
            print(url + ' ' + getName)
            getAuthor = soup.select('.readName.b a')[0].get_text() + ' '
            getTime = soup.select('#td_tpc > div.tipTop.s6 > span:nth-child(3)')[0].get_text() + '\n'
            getContent = soup.select('#td_tpc > div.tpc_content')
            # 替换成换行
            myReplace = ['<br/>', '<br>', '</blockquote>', '</div>']
            for eachReplace in myReplace:
                getContent = str(getContent).replace(eachReplace, '\n')
            getContent = BeautifulSoup(getContent, 'html.parser').get_text()
            writefile(getName, getName + '\n\n' +  getAuthor +getTime + '\n\n' + getContent + '\n\n'  +url)
        except:
            print(str(eachtid) + '帖子错误')
        time.sleep(2)     
        
if __name__ == '__main__':
    main()
    
