# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

import sys
import re
import datetime
from pathlib import Path

def readfile(filename):
    # 读取文件
    with open(filename, mode='r', encoding='UTF-8') as file:
        filereadlines = file.readlines()
    for i in range(len(filereadlines)):
        filereadlines[i] = filereadlines[i].rstrip()
    return filereadlines

def writefile(filename,filereadlines):
    # 写入文件
    newfile = open(Path(filename).parent.joinpath(Path(filename).stem + '转换后' + Path(filename).suffix), mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()
    print('完成：' + str(Path(filename).name))
    
def formatDateAddZero(date_str):
    parts = str(date_str.group()).split('.')
    year, month, day = parts
    return f"{year}.{month.zfill(2)}.{day.zfill(2)}"

def formatDatesForLine(text):
    """
    从文本中提取并格式化日期
    格式化日期字符串（补零）
    
    参数：
    text (str): 包含日期的长字符串
    
    返回：
    list: 格式化后的日期列表
    """
    # 匹配格式为YYYY.M.D或YYYY.MM.DD的日期
    datePattern = r'\d{4}\.\d{1,2}\.\d{1,2}'
    raw_dates = re.sub(datePattern, formatDateAddZero, text)
    return raw_dates
    
def formatDatesForFile(filePath):
    # 读取.txt文件
    filereadlines = readfile(filePath)
    print('处理：' + str(Path(filePath).name))
    # 存储所有文本
    tempContent = []
    for eachLine in filereadlines:
        tempContent.append(formatDatesForLine(eachLine) + '\n')
    print(tempContent)
    writefile(filePath, tempContent)

def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                formatDatesForFile(file)

        if Path.is_file(Path(aPath)):
            formatDatesForFile(Path(aPath))
            
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass