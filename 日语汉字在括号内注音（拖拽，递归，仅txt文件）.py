# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# by Andy
# v0.1
# pip install pykakasi

from pathlib import Path
from pykakasi import kakasi
from collections import Counter
from opencc import OpenCC
import sys
import re

def readfile(filename):
    with open(filename, mode='r', encoding='UTF-8') as file:
        filereadlines = file.readlines()
    return filereadlines

def writefile(filename,filereadlines):
    newfile = open(filename, mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()
    
def ifIsCJK(char):
    """判断字符是否为 CJK 汉字（包括所有扩展区）"""
    otherChars = {'々'}
    if char in otherChars:
        return True
        
    cp = ord(char)
    
    # 基本区
    if 0x4E00 <= cp <= 0x9FFF:
        return True
    
    # 扩展A区
    if 0x3400 <= cp <= 0x4DBF:
        return True
    
    # 扩展B区 (使用代理对表示)
    if 0x20000 <= cp <= 0x2A6DF:
        return True
    
    # 扩展C区
    if 0x2A700 <= cp <= 0x2B73F:
        return True
    
    # 扩展D区
    if 0x2B740 <= cp <= 0x2B81F:
        return True
    
    # 扩展E区
    if 0x2B820 <= cp <= 0x2CEAF:
        return True
    
    # 扩展F区
    if 0x2CEB0 <= cp <= 0x2EBEF:
        return True
    
    # 扩展G区 (2020年新增)
    if 0x30000 <= cp <= 0x3134F:
        return True
    
    # 兼容扩展区
    if 0xF900 <= cp <= 0xFAFF:
        return True
    
    # 兼容补充区
    if 0x2F800 <= cp <= 0x2FA1F:
        return True
    
    return False

# def ifIsChinese(eachChar):
    # otherChars = {'々'}
    # if '\u4e00' <= eachChar <= '\u9fff' or eachChar in otherChars:
        # return True
    # else:
        # return False

def convertLine(kakasiPart):
    allLine = ''
    for eachPart in kakasiPart:
        orig = eachPart['orig']
        hira = eachPart['hira']
        newLine = ''
        if orig == '\n':
            break
        else:
            if ifIsCJK(orig[-1]):
                # 全是汉字
                newLine = newLine + orig + '（' + hira + '）'
            elif len(orig) == len(hira) and not ifIsCJK(orig[0]):
                # 全是平片假名
                for eachChar in orig:
                    newLine = newLine + eachChar + ''
            else:
                for tempIndex in range(0, len(orig)):
                    if not ifIsCJK(orig[tempIndex]):
                        getIndex = tempIndex
                        break
                # 对比转换前后相同的部分
                myCompare = Counter(hira) & Counter(orig)
                getSuffix = ''.join(myCompare.keys())
                newLine = newLine + orig[0:orig.find(getSuffix)] + '（' +  hira[0:hira.find(getSuffix)] + '）'
                for eachChar in getSuffix:
                     newLine = newLine + eachChar + ''
            allLine = allLine + newLine
    return allLine
        

def convertToHTML(filename):
    readFileContent = readfile(filename)
    outputFileContent = []
    mykakasi = kakasi()
    for eachLine in readFileContent:
        newLine = ''
        eachLine = OpenCC('s2t').convert(eachLine)
        if eachLine == '\n':
            outputFileContent.append('\n')
        else:
            newLine = newLine.replace('\n','') + convertLine(mykakasi.convert(eachLine))
            newLine = newLine.replace('\n','') +  '\n'
            outputFileContent.append(newLine)
    newFileName = filename.parent.joinpath(Path(filename).stem + '_new.txt')
    writefile(newFileName, outputFileContent)

def main(inputPath):
    fileType = ['.txt']
    for aPath in inputPath[1:]:
        if Path.is_dir(Path(aPath)):
            for eachFile in Path(aPath).glob('**/*'):
                if (Path(eachFile).suffix in fileType):
                    convertToHTML(Path(eachFile))
        if Path.is_file(Path(aPath)):
            if (Path(aPath).suffix in fileType):
                convertToHTML(Path(aPath))

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass
