# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

import sys
from pathlib import Path

def doChangeFileNameByFileType(allFilePath):
    # type(allFilePath): Path
    # 文件名重命名以某个扩展名的文件名命名其他文件
    # 相同的扩展名的文件有2个或以上时，不会执行重命名
    # 比如同时拖拽1.html，2.mp3，3.jpg，在setRenameFileType设置成'.html'，那么3个文件会以.html文件名命名，结果是1.html，1.mp3，1.jpg
    setRenameFileType = '.html'
    getRenameFileName = ''
    allFileSuffix = {}
    checkSuffixCount = True
    for eachFile in allFilePath:
        if eachFile.suffix == setRenameFileType:
            getRenameFileName = eachFile
        if eachFile.suffix not in allFileSuffix:
            allFileSuffix[eachFile.suffix] = 1
        else:
            allFileSuffix[eachFile.suffix] = allFileSuffix[eachFile.suffix] + 1
            checkSuffixCount = False
    if checkSuffixCount and allFileSuffix[setRenameFileType]:
        for eachFile in allFilePath:
            newFileName = eachFile.parent.joinpath(getRenameFileName.stem + eachFile.suffix)
            if not Path(newFileName).exists():
                eachFile.rename(newFileName)
    else:
        print('相同的扩展名的文件有2个或以上时，不会执行重命名。或不存在需要的后缀名的文件。')

def main(inputPath):
    allFilePath = []
    for aPath in inputPath[1:]:
        if Path.is_file(Path(aPath)):
            allFilePath.append(Path(aPath))
    if len(allFilePath) > 1:
        doChangeFileNameByFileType(allFilePath)
    else:
        print('需要拖拽2个或以上文件')
            
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass