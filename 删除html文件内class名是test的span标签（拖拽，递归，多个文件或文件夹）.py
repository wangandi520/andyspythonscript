# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

import sys
from bs4 import BeautifulSoup
from pathlib import Path

def readfile(filename):
    # 读取文件
    with open(filename, mode='r', encoding='UTF-8') as file:
        filereadlines = file.read()
    return filereadlines

def writefile(filename,filereadlines):
    # 写入文件
    newfile = open(Path(filename).parent.joinpath(Path(filename).stem + '转换后' + Path(filename).suffix), mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()
    print('完成：' + str(Path(filename).name))

def removeSpans(filePath):
    # 读取HTML文件
    filereadlines = readfile(filePath)
    
    # 解析HTML内容
    soup = BeautifulSoup(filereadlines, 'html.parser')
    
    # 查找所有class为"test"的span标签
    test_spans = soup.find_all('span', class_='test')
    
    # 直接删除这些span标签（包括标签自身和内容）
    for span in test_spans:
        span.decompose()  # 或 span.extract()
    
    # 保存新文件
    writefile(filePath, str(soup))
        
def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                removeSpans(file)

        if Path.is_file(Path(aPath)):
            removeSpans(Path(aPath))
            
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass