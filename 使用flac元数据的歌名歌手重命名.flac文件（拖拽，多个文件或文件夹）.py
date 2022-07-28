# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# base on: https://github.com/devsnd/tinytag
# pip install tinytag

import sys
from tinytag import TinyTag
from pathlib import Path

def validFileName(fileName):
    # 把不能作为文件的字符替换成空格
    for each in fileName:
        if each in '\/:*?"<>|,':
            fileName = fileName.replace(each, ' ')
    return fileName

def doChangeFileName(filePath):
    # typeof(filePath): Path
    # 文件格式，如果需要其他格式请手动添加，支持的格式见第三行的网址
    fileType = ['.flac', '.mp3']
    # newFileName是文件名格式，按需求修改，eachTag.title是歌名，eachTag.artist是歌手，其他信息见第三行的网址
    
    if Path.is_file(filePath) and (filePath.suffix.lower() in fileType):
        eachTag = TinyTag.get(filePath)
        newFileName = validFileName(eachTag.title + ' - ' + eachTag.artist) + filePath.suffix
        filePath.rename(filePath.parent.joinpath(newFileName))
        print(filePath.name + ' -> ' + newFileName)

def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                doChangeFileName(file)

        if Path.is_file(Path(aPath)):
            doChangeFileName(Path(aPath))
            
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass