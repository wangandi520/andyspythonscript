# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import os
import zipfile

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
    # 是否重命名文件，在文件名最后添加字数
    renameFile = False
    # 文件夹
    if Path.is_dir(Path(filePath)):
        wordCount = 0
        for eachFilePath in Path(filePath).glob('**/*'):
            if eachFilePath.suffix in mySuffix:
                wordCount = wordCount + getFileWordCount(eachFilePath)
                # 输出格式：字数  文件夹名
        print(str(wordCount) + '  ' + str(Path(filePath).name))
     
    # 文件
    if Path.is_file(Path(filePath)) and Path(filePath).suffix in mySuffix:
            # 输出格式：字数  文件名
            print(str(getFileWordCount(filePath)) + '  ' + str(Path(filePath).name))
            if renameFile:
                Path(filePath).rename(Path(filePath).parent.joinpath(Path(filePath).stem + str(getFileWordCount(filePath)) + Path(filePath).suffix))
    # epub
    if Path.is_file(Path(filePath)) and Path(filePath).suffix == '.epub':
        wordCount = 0
        with zipfile.ZipFile(filePath) as myzipfile:
            for eachFile in myzipfile.namelist():
                if eachFile.endswith(tuple(mySuffix)):
                    with myzipfile.open(eachFile, 'r') as tempFile:
                        for eachLine in tempFile.readlines():
                            eachLine = eachLine.decode('utf-8')
                            for eachChar in eachLine:
                                if ifIsChinese(eachChar):
                                    wordCount = wordCount + 1
        # 输出格式：字数  epub文件名
        print(str(wordCount) + '  ' + str(Path(filePath).name))
        if renameFile:
            Path(filePath).rename(Path(filePath).parent.joinpath(Path(filePath).stem + str(wordCount) + Path(filePath).suffix))

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