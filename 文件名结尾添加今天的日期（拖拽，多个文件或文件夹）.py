# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

import sys
import re
import datetime
from pathlib import Path
from typing import List, Union

def validFileName(oldFileName):
    # '/ \ : * ? " < > |'
    # 替换为下划线
    validChars = r"[\/\\\:\*\?\"\<\>\|]"  
    newFileName = re.sub(validChars, "_", oldFileName)
    return newFileName

def doChangeFileName(filePath):
    # type(filePath): Path
    # getTime，%Y%m%d%H%M%S分别是年月日时分秒，可以替换成自己需要的格式
    getTime = datetime.datetime.now().strftime("%Y%m%d")
    if Path.is_file(filePath):
        newFileName = validFileName(filePath.stem + getTime) + filePath.suffix
        newFilePath = Path(filePath).parent.joinpath(newFileName)
        if not newFilePath.exists():
            filePath.rename(newFilePath)
            print(str(filePath) + ' -> ' + str(newFilePath))
            
def main(inputPath: list[str]) -> None:
    try:
        for eachPath in inputPath[1:]:
            eachPath = Path(eachPath)
            if eachPath.is_dir():
                for eachFile in eachPath.glob('**/*'):
                    doChangeFileName(eachFile)
            elif eachPath.is_file():
                doChangeFileName(eachPath)
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