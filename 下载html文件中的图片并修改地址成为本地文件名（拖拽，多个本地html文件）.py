# encoding:utf-8
# https://github.com/wangandi520/ClippingsToMarkdown
# Programmed by Andy
# v0.1

from pathlib import Path
from bs4 import BeautifulSoup
import sys
import time
import requests

def main(inputPath):
    # 获取本地html文件内所有img的src地址
    # 第一个文件的编号
    fileIndex = 1
    # 文件名前缀
    fileNamePrefix = 'image'
    # 文件名序号位数，3 = 000-999
    fileNameFill = 3
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.55 Safari/537.36'}
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_file(Path(aPath)):
            if (Path(aPath).suffix == '.html'):
                print('正在处理的文件 ' + Path(aPath).name)
                with open(Path(aPath), 'r', encoding = 'utf-8') as file:
                    myHtml = file.read()
                soup = BeautifulSoup(myHtml, 'html.parser')
                allImages = soup.find_all('img')
                for eachImage in allImages:
                    src = eachImage.get('src')
                    # 修改html文件中图片的src地址
                    eachImage['src'] = '../Images/' + fileNamePrefix + str(fileIndex).zfill(fileNameFill) + '.jpg'
                    imgData = requests.get(url=src, headers=headers).content
                    imgPath = fileNamePrefix + str(fileIndex).zfill(fileNameFill) + '.jpg'
                    # 保存图片
                    with open(imgPath, 'wb') as f:
                        f.write(imgData)
                    # 保存html
                    with open(Path(aPath), 'w', encoding = 'utf-8') as file:
                        file.write(str(soup))
                    fileIndex = fileIndex + 1
                # 改名

   
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass