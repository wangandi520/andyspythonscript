# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import os

def checkFileNameIndex(filePath):
    # 如果image001.jpg后是image003.jpg，则输出可能缺失的文件image002.jpg
    # 设置文件名最后几位是数字，image001是3
    getIndexNumber = 3
    # 文件夹
    allFilePath = []
    getFlag = True
    if Path.is_dir(Path(filePath)):
        for eachFilePath in Path(filePath).glob('*'):
            allFilePath.append(eachFilePath)
    # 符合这几个条件才继续执行脚本：文件夹不包含子文件夹，所有文件名长度相同，扩展名相同
    firstFileLength = len(allFilePath[0].stem)
    firstFileSuffix = allFilePath[0].suffix
    for eachFilePath in allFilePath:
        if len(eachFilePath.stem) != firstFileLength:
            getFlag = False
        if eachFilePath.suffix != firstFileSuffix:
            getFlag = False
        if Path.is_dir(eachFilePath):
            getFlag = False
    if getFlag:
        # 只显示可能缺失的文件名
        for fileIndex in range(1, len(allFilePath)):
            previousFileIndex = allFilePath[fileIndex - 1].name[firstFileLength - getIndexNumber : firstFileLength]
            currentFileIndex = allFilePath[fileIndex].name[firstFileLength - getIndexNumber : firstFileLength]
            if previousFileIndex.isdigit() and currentFileIndex.isdigit():
                if int(currentFileIndex) - int(previousFileIndex) != 1:
                    # 输出：可能缺失的文件名  文件夹名
                    print(allFilePath[fileIndex - 1].name[0 : firstFileLength - getIndexNumber] + str(int(previousFileIndex) + 1).zfill(getIndexNumber) + firstFileSuffix + '  ' + Path(allFilePath[0]).parent.name)
            else:
                print('其他错误：文件名数字位数错误或其他')

def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        for eachPath in Path(aPath).glob('**/'):
            checkFileNameIndex(eachPath)
    os.system('pause')

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass