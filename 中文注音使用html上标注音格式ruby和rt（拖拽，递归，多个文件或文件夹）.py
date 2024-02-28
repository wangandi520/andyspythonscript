# encoding:utf-8
# https://github.com/wangandi520/ClippingsToMarkdown
# by Andy
# v0.1
# pip install pypinyin

from pathlib import Path
from pypinyin import pinyin, lazy_pinyin, Style
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
    
def ifIsChinese(eachChar):
    if '\u4e00' <= eachChar <= '\u9fff':
        return True
    else:
        return False

def ifIsRareChinese(eachChar):
    myPattern = re.compile(u'[~!@#$%^&* ]')
    getMatch = myPattern.search(eachChar)
    if getMatch:
        return True
    try:
        eachChar.encode('gb2312')
    except UnicodeEncodeError:
        return True
    return False
    
def convertToHTML(filename):
    # 是否只注音生僻字
    onlyConvertRare = False
    # 是否在每行首尾添加<p></p>
    addPTag = False
    readFileContent = readfile(filename)
    outputFileContent = []
    for eachLine in readFileContent:
        if addPTag:
            newLine = '<p><ruby>'
        else:
            newLine = '<ruby>'
        if eachLine != '\n':
            for eachChar in eachLine:
                if onlyConvertRare:
                    if ifIsChinese(eachChar) and ifIsRareChinese(eachChar):
                        newLine = newLine + eachChar + '<rt>' + ''.join(pinyin(eachChar)[0]) + '</rt>'
                    else:
                        newLine = newLine + eachChar + '<rt></rt>'
                else:
                    if ifIsChinese(eachChar):
                        newLine = newLine + eachChar + '<rt>' + ''.join(pinyin(eachChar)[0]) + '</rt>'
                    else:
                        newLine = newLine + eachChar + '<rt></rt>'
            if addPTag:
                newLine = newLine.replace('\n','') +  '</ruby></p>\n'
            else:
                newLine = newLine.replace('\n','') +  '</ruby>\n'
            outputFileContent.append(newLine)
        elif eachLine == '\n':
            outputFileContent.append('\n')
    newFileName = filename.parent.joinpath(filename.stem + '.html')
    if not Path(newFileName).exists():
        writefile(newFileName, outputFileContent)

def main(inputPath):
    fileType = ['.txt', '.md', '.html']
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
