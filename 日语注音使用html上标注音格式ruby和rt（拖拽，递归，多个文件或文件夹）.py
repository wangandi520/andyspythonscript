# encoding:utf-8
# https://github.com/wangandi520/ClippingsToMarkdown
# by Andy
# v0.1
# pip install pykakasi

from pathlib import Path
from pykakasi import kakasi
from collections import Counter
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

def convertLine(kakasiPart):
    allLine = ''
    for eachPart in kakasiPart:
        orig = eachPart['orig']
        hira = eachPart['hira']
        newLine = ''
        if orig == '\n':
            break
        else:
            if ifIsChinese(orig[-1]):
                # 全是汉字
                newLine = newLine + orig + '<rt>' + hira + '</rt>'
            elif len(orig) == len(hira) and not ifIsChinese(orig[0]):
                # 全是平片假名
                for eachChar in orig:
                    newLine = newLine + eachChar + '<rt></rt>'
            else:
                for tempIndex in range(0, len(orig)):
                    if not ifIsChinese(orig[tempIndex]):
                        getIndex = tempIndex
                        break
                # 对比转换前后相同的部分
                myCompare = Counter(hira) & Counter(orig)
                getSuffix = ''.join(myCompare.keys())
                newLine = newLine + orig[0:orig.find(getSuffix)] + '<rt>' +  hira[0:hira.find(getSuffix)] + '</rt>'
                for eachChar in getSuffix:
                     newLine = newLine + eachChar + '<rt></rt>'
            allLine = allLine + newLine
    return allLine
        

def convertToHTML(filename):
    # 是否在每行首尾添加<p></p>
    addPTag = False
    readFileContent = readfile(filename)
    outputFileContent = []
    mykakasi = kakasi()
    for eachLine in readFileContent:
        if addPTag:
            newLine = '<p><ruby>'
        else:
            newLine = '<ruby>'
        if eachLine == '\n':
            outputFileContent.append('\n')
        else:
            newLine = newLine.replace('\n','') + convertLine(mykakasi.convert(eachLine))
            if addPTag:
                newLine = newLine.replace('\n','') +  '</ruby></p>\n'
            else:
                newLine = newLine.replace('\n','') +  '</ruby>\n'
            outputFileContent.append(newLine)
    newFileName = filename.parent.joinpath(Path(filename).stem + '.html')
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
