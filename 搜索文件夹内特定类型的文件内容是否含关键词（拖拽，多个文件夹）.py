# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import os

def searchKeywordInFile(filePath, keyword):
    # readfile
    with open(filePath, mode='r', encoding='UTF-8') as file:
        filereadlines = file.readlines()
    for i in range(len(filereadlines)):
        filereadlines[i] = filereadlines[i].rstrip()
        if keyword in filereadlines[i]:
            print(str(i + 1) + ' ' + str(filePath.name) + '  ' + str(filePath))
    
def main(inputPath):
    # 设置你的关键词
    myKeyword = '微信'
    # 要搜索的文件的扩展名
    mySuffix = ['.html', '.xhtml']
    del inputPath[0]
    print('搜索关键词：' + myKeyword)
    print('行数 文件名 文件路径')
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if file.suffix.lower() in mySuffix:
                    searchKeywordInFile(file, myKeyword)      
    print('搜索完成\n')
    os.system('pause')                    
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass