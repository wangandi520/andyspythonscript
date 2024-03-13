# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# by Andy
# v0.2

from pathlib import Path
import sys
import zipfile

def doZipFolder(inputPath):
    # 每个文件夹压缩成zip文件，包含这个文件夹，zip文件=文件夹名
    allFilePath = []
    # 压缩方式：存储（速度最快），体积和压缩前差不多
    myZipType = zipfile.ZIP_STORED
    # 压缩方式：标准（速度一般），体积会变小
    #myZipType = zipfile.ZIP_DEFLATED
    # 保存位置：在脚本所在的目录
    #myZipSavePath = inputPath.stem + '.zip'
    # 保存位置：在目标文件夹所在的目录
    myZipSavePath = inputPath.parent.joinpath(Path(inputPath.stem + '.zip'))
    myZipFile = zipfile.ZipFile(myZipSavePath, 'w', myZipType)
    print('正在新建压缩文件：' + str(myZipSavePath))
    for eachFilePath in inputPath.glob('**/*'):
        myZipFile.write(eachFilePath, eachFilePath.relative_to(inputPath.parent))
    myZipFile.close()

def main(inputPath):
    for aPath in inputPath[1:]:
        if Path.is_dir(Path(aPath)):
            doZipFolder(Path(aPath))

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass