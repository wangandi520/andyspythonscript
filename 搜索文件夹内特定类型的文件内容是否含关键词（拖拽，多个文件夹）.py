# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import os

def myPrint(string, padding = 80):
    padding = ' ' * (padding - len(string)) if padding else ''
    print(string + padding, end = '\r')

def searchKeywordInFile(filePath, keyword):
    # 读取文件
    # 如果搜索的关键词前后10个字含有这些关键词，就不输出
    # excludeKeyword = ['关键词01', '关键词02']
    excludeKeyword = []
    with open(filePath, mode='r', encoding='UTF-8') as file:
        filereadlines = file.readlines()
    myPrint('正在扫描' + filePath.name)
    for i in range(len(filereadlines)):
        filereadlines[i] = filereadlines[i].rstrip()
        for eachKeyword in keyword:
            getKeywordLocation = filereadlines[i].lower().find(eachKeyword)
            if getKeywordLocation > -1:
                toShow = True
                for eachExcludeKeyword in excludeKeyword:
                    if eachExcludeKeyword in filereadlines[i][getKeywordLocation - 10:getKeywordLocation + 10].lower():
                        toShow = False
                if toShow:
                    print(filereadlines[i][getKeywordLocation - 10:getKeywordLocation + 10] + '    ' + str(i + 1) + '    ' + str(filePath.name) + '    ' + str(filePath))
    
def main(inputPath):
    # 设置你的关键词
    myKeywords = ['微信', '公众号']
    # 要搜索的文件的扩展名
    mySuffix = ['.html', '.xhtml', '.opf', '.txt']
    del inputPath[0]
    print('搜索关键词：' + '，'.join(myKeywords))
    print('内容 行数 文件名 文件路径')
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if file.suffix.lower() in mySuffix:
                    searchKeywordInFile(file, myKeywords)      
    print('\n搜索完成\n')
    os.system('pause')
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass