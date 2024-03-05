# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# by Andy
# v0.2

from pathlib import Path
import sys
import os
import zipfile

def getEpubCoverImage(filePath):
    # type(filePath): Path
    # 文件格式
    fileType = ['.epub']
    # 封面图片名
    coverImageFilename = ['cover.jpg', 'cover.jpeg']
    if Path.is_file(filePath) and (filePath.suffix.lower() in fileType):
        print('正在处理epub：' + filePath.name)
        with zipfile.ZipFile(filePath, 'r') as myzipfile:
            # 获取所有文件列表
            eachFileList = myzipfile.namelist()
            for eachFilePath in eachFileList:
                if Path(eachFilePath).name.lower() in coverImageFilename:
                    imageData = myzipfile.read(eachFilePath)
                    imageFilePath = filePath.parent.joinpath(Path(filePath).stem + Path(eachFilePath).suffix)
                    Path(imageFilePath).write_bytes(imageData)

def main(inputPath):
    for aPath in inputPath[1:]:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                getEpubCoverImage(file)
        if Path.is_file(Path(aPath)):
            getEpubCoverImage(Path(aPath))

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass