# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# by Andy
# v0.1

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
                    newZipFilePath = Path(eachFilePath).joinpath(Path(eachFilePath).stem)
                    myzipfile.extract(eachFilePath, '.')
                    Path(eachFilePath).replace(filePath.stem + Path(eachFilePath).suffix)
                    while Path(eachFilePath).parent.exists() and Path(eachFilePath).parent != Path('.'):
                        # 去掉这4行的注释可以删掉多余的空文件夹
                        # try:
                            # Path(eachFilePath).parent.rmdir()
                        # except OSError:
                            # pass
                        print('可删除的文件夹 ' + str(Path(eachFilePath).parent))
                        eachFilePath = Path(eachFilePath).parent

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