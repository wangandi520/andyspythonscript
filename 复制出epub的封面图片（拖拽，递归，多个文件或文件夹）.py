# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# by Andy
# v0.2

from pathlib import Path
import sys
import os
import zipfile

def makeStringShorten(myString, cutLength = 10):
    # cutLength = 头尾要显示的字符长度
    if len(myString) < 10:
        return myString
    else:
        return myString[0: cutLength] + '......' + myString[-cutLength:]
        
def getEpubCoverImage(filePath):
    # type(filePath): Path
    # 文件格式
    fileType = ['.epub']
    # 封面图片名
    coverImageFilename = ['cover.jpg', 'cover.jpeg']
    # 图片复制到哪个位置
    #copyToLocation = 'epub'，epub目录下
    #copyToLocation = 'script'，脚本目录下
    #copyToLocation = 'myfolder'，自己设置的目录下
    copyToLocation = 'script'
    myfolder = 'd:\\cover\\'
    if Path.is_file(filePath) and (filePath.suffix.lower() in fileType):
        print('正在处理文件：' + makeStringShorten(filePath.name))
        coverImageExist = False
        with zipfile.ZipFile(filePath, 'r') as myzipfile:
            # 获取所有文件列表
            eachFileList = myzipfile.namelist()
            for eachFilePath in eachFileList:
                if Path(eachFilePath).name.lower() in coverImageFilename:
                    imageData = myzipfile.read(eachFilePath)
                    if copyToLocation == 'epub':
                        imageFilePath = filePath.parent.joinpath(Path(filePath).stem + Path(eachFilePath).suffix)
                    if copyToLocation == 'script':
                        imageFilePath = Path(sys.argv[0]).parent.joinpath(Path(filePath).stem + Path(eachFilePath).suffix)
                    if copyToLocation == 'myfolder':
                        imageFilePath = Path(myfolder).joinpath(Path(filePath).stem + Path(eachFilePath).suffix)
                    Path(imageFilePath).write_bytes(imageData)
                    coverImageExist = True
        if coverImageExist:
            print('成功提取封面：' + makeStringShorten(filePath.name))
        else:
            print('无法找到封面：' + makeStringShorten(filePath.name))

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