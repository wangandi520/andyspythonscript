# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# by Andy
# v0.2

from pathlib import Path
import sys

from typing import List, Union

def writefile(fileName: Path, allFileContent: list[str]) -> None:
    try:
        with open(fileName, mode='w', encoding='UTF-8') as newfile:
            newfile.writelines(allFileContent)
    except Exception as e:
        print(f'写入文件失败：{fileName}，错误：{str(e)}')

def readfile(fileName: Path) -> list[str]:
    try:
        with open(fileName, mode='r', encoding='UTF-8') as newfile:
            return newfile.readlines()
    except Exception as e:
        print(f'读取文件失败：{fileName}，错误：{str(e)}')
        return []

def doConvert(fileName: Path) -> None:
    try:
        print(f'处理文件：{fileName}')
        # readFileContent = readfile(fileName)
        # for eachLine in readFileContent:
            # print(eachLine)
        # newFileName = fileName.parent.joinpath(fileName.stem + '.html')
        # if not Path(newFileName).exists():
            # writefile(newFileName, ttempFileContent)
    except Exception as e:
        print(f'处理文件时出错：{fileName}，错误：{str(e)}')

def main(inputPath: list[str]) -> None:
    fileType = {'.txt'}  # 使用集合而不是列表，查找更快
    try:
        for eachPath in inputPath[1:]:
            eachPath = Path(eachPath)
            if eachPath.is_dir():
                for eachFile in eachPath.glob('**/*'):
                    if eachFile.suffix.lower() in fileType:
                        doConvert(eachFile)
            elif eachPath.is_file() and eachPath.suffix.lower() in fileType:
                doConvert(eachPath)
    except Exception as e:
        print(f'程序执行出错：{str(e)}')

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
        else:
            print('请拖拽文件到本脚本，或者命令行运行时添加文件路径')
    except IndexError:
        pass