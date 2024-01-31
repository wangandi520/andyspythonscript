# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
from PIL import Image
import sys
import os

def ifIsChinese(eachChar):
    if '\u4e00' <= eachChar <= '\u9fff':
        return True
    else:
        return False

def getFileWordCount(eachFilePath):
    wordCount = 0
    with open(eachFilePath, mode='r', encoding='UTF-8') as file:
        filereadlines = file.readlines()
    for eachLine in filereadlines:
        for eachChar in eachLine:
            if ifIsChinese(eachChar):
                wordCount = wordCount + 1
    return wordCount

def getWordCount(filePath):
    # 拖拽的是文件夹，就统计里面所有符合扩展名类型的文件的中文字数
    # 拖拽的是文件，只统计这个文件内的中文字数
    # 要统计字数的文件的扩展名
    mySuffix = ['.html', '.xhtml', '.txt']
    if Path.is_dir(Path(filePath)):
        wordCount = 0
        for eachFilePath in Path(filePath).glob('**/*'):
            if eachFilePath.suffix in mySuffix:
                wordCount = wordCount + getFileWordCount(eachFilePath)
                # 输出格式：字数  文件名或文件夹名
        print(str(wordCount) + '  ' + str(Path(filePath).name))
    if Path.is_file(Path(filePath)):
        if Path(filePath).suffix in mySuffix:
            # 输出格式：字数  文件名或文件夹名
            print(str(getFileWordCount(filePath)) + '  ' + str(Path(filePath).name))

def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        getWordCount(aPath)
    os.system('pause')

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass