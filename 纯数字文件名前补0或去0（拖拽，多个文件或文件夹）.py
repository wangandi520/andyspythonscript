# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys

def renameByAddZero(filePath):
    # type(filePath): Path
    # 只对纯数字文件名有效，文件名前添加几个0
    # fileNameFill，文件名几位数字，001这样就填3，01这样就填2
    fileNameFill = 3
    if filePath.stem.isdigit():
        newFilePath = filePath.parent.joinpath(filePath.stem.zfill(fileNameFill) + filePath.suffix)
        if not newFilePath.exists():
            filePath.rename(newFilePath)
            
def renameByRemoveZero(filePath):
    # type(filePath): Path
    # fileNameFill，处理后的文件名，文件名长度大于这个数字才能去0，填3时，0001会去掉一个0，00001会去掉两个0
    fileNameFill = 3
    if filePath.stem.isdigit():
        fileNameLength = len(str(filePath.stem))
        ifRename = True
        for count in range(0, fileNameLength - fileNameFill):
            if str(filePath.stem)[count] != '0':
                ifRename = False
        if ifRename and fileNameLength > fileNameFill:
            newFilePath = filePath.parent.joinpath(filePath.stem[fileNameLength - fileNameFill:] + filePath.suffix)
            if not newFilePath.exists():
                filePath.rename(newFilePath)   
            
def main(inputPath):
    # 模式1，补0。模式2，去0
    mode = 1
    for aPath in inputPath[1:]:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if mode == 1:
                    renameByAddZero(file)
                if mode == 2:
                    renameByRemoveZero(file)
        if Path.is_file(Path(aPath)):
            if mode == 1:
                renameByAddZero(Path(aPath))
            if mode == 2:
                renameByRemoveZero(Path(aPath))

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass