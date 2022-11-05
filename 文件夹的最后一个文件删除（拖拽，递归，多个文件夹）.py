# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys

def getLastFile(filePath):
    # type(filePath): Path
    allFilePath = []
    for file in Path(filePath).glob('*'):
        if Path.is_file(file):
            allFilePath.append(file)
    allFilePath.sort()
    return allFilePath[-1]

def main(inputPath):
    # type(inputPath): Path
    allFilePath = []
    allDir = []
    # 读取所有被拖拽的文件夹和子文件夹
    for aPath in inputPath[1:]:
        if Path.is_dir(Path(aPath)):
            allDir.append(Path(aPath))
        for file in Path(aPath).glob('**/*'):
            if Path.is_dir(file):
                allDir.append(file)
    for eachDir in allDir:
        allFilePath.append(getLastFile(eachDir))
    for eachFile in allFilePath:
        print(eachFile)
    myChoice = input('要删除以上' + str(len(allFilePath)) + '个文件, 请输入y或yes：')
    if myChoice.lower() in ['y', 'yes']:
        for eachFile in allFilePath:
            eachFile.unlink()
                
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass