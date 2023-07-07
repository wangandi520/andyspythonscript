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
    newnewfilereadlines = []
    # 第几行到第几行
    startIndex = 0
    endIndex = 9
    while startIndex < endIndex:
        newnewfilereadlines.append(newfilereadlines[startIndex])
        startIndex = startIndex + 1
    return newnewfilereadlines

def writefile(eachFilePath, filereadlines):
    # 写入new.txt
    newfile = open(eachFilePath.parent.joinpath(eachFilePath.stem + '_new' + eachFilePath.suffix), mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()

def main(allFilePath):
    del allFilePath[0]
    
    for eachFilePath in allFilePath:
        if Path(eachFilePath).suffix == '.txt':
            allFileLine =  readfile(eachFilePath)
            writefile(Path(eachFilePath), allFileLine)

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        main(sys.argv)
