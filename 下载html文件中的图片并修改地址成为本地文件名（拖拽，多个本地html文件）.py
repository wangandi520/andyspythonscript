# encoding:utf-8
# https://github.com/wangandi520/ClippingsToMarkdown
# Programmed by Andy
# v0.2

from pathlib import Path
from bs4 import BeautifulSoup
import sys
import time
import requests

def readfile(filename):
    with open(filename, mode='r', encoding='UTF-8') as file:
        filereadlines = file.readlines()
    return filereadlines

def writefile(filename,filereadlines):
    newfile = open(filename, mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()
    
def main(inputPath):
    # html会被修改
    # 获取本地html文件内所有img的src地址
    for aPath in inputPath[1:]:
        if Path.is_file(Path(aPath)) and Path(aPath).suffix == '.html':
            # 第一个文件的编号
            fileIndex = 1
            # 文件名序号位数，3 = 000-999
            fileNameFill = 3
            # 文件名前缀
            #fileNamePrefix = 'image'
            fileNamePrefix = Path(aPath).stem
            print('正在处理的文件 ' + Path(aPath).name)
            oldHtmlFile = readfile(Path(aPath))
            newHtmlFile = []
            # 解析图片src
            with open(Path(aPath), 'r', encoding = 'utf-8') as myFile:
                mySoupHtml = myFile.read()
            soup = BeautifulSoup(mySoupHtml, 'html.parser')
            allImages = soup.find_all('img')
            tempImageName = []
            for tempIndex in range(0, len(allImages)):
                getFileName = str(Path(allImages[tempIndex].get('src')).name)
                getPartUrl = allImages[tempIndex].get('src').replace(getFileName, '')
                if getPartUrl[0:4] == 'http':
                    # [不含图片名的url，原图片名，保存的图片名]
                    tempImageName.append([getPartUrl, getFileName, fileNamePrefix + str(tempIndex + 1).zfill(fileNameFill) + Path(allImages[tempIndex].get('src')).suffix])
            print('需要下载' + str(len(allImages)) + '张图片')
            for tempIndex in range(0, len(oldHtmlFile)):
                for eachImage in tempImageName:
                    if (eachImage[0] + eachImage[1]) in oldHtmlFile[tempIndex]:
                        oldHtmlFile[tempIndex] = oldHtmlFile[tempIndex].replace((eachImage[0] + eachImage[1]), eachImage[2])
            for eachImage in tempImageName:
                imgData = requests.get(url=eachImage[0] + eachImage[1]).content
                print('正在下载 ' + eachImage[0] + eachImage[1])
                # 保存图片
                with open(eachImage[2], 'wb') as imageFile:
                    imageFile.write(imgData)
            # 写入原html文件
            writefile(Path(aPath).name, oldHtmlFile)
            
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass