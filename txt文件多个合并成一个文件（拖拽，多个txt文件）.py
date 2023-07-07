# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
import sys
from pathlib import Path

def readfile(filename):
    # 读取
    with open(filename, mode='r', encoding='UTF-8') as file:
        filereadlines = file.readlines()
    newfilereadlines = []
    for each in filereadlines:
        # 过滤掉长度小于某数值的行
        if len(each.rstrip()) >= 0 and each != '\n':
            newfilereadlines.append(each)
    newfilereadlines.append('\n')
    return newfilereadlines

def writefile(filereadlines):
    # 写入new.txt
    newfile = open('new.txt', mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()

def main(allFilePath):
    del allFilePath[0]
    
    allFileLine = []
    for eachFilePath in allFilePath:
        if Path(eachFilePath).suffix == '.txt':
            allFileLine = allFileLine  + readfile(eachFilePath)
    writefile(allFileLine)

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        main(sys.argv)
