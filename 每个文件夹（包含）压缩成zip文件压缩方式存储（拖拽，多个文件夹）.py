# encoding:utf-8
# https://github.com/wangandi520/ClippingsToMarkdown
# by Andy
# v0.1

from pathlib import Path
import sys
import zipfile

def doZipFolder(inputPath):
    # 每个文件夹压缩成zip文件，包含这个文件夹，zip文件=文件夹名，压缩方式：存储（速度最快）
    allFilePath = []
    for eachFilePath in inputPath.glob('**/*'):
        allFilePath.append(eachFilePath.relative_to(inputPath.parent))
    myZipFile = zipfile.ZipFile(inputPath.stem + '.zip', 'w', zipfile.ZIP_STORED)
    for eachFilePath in allFilePath:
        myZipFile.write(eachFilePath)
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