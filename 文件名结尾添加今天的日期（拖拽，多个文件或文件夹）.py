# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

import sys
import re
import datetime
from pathlib import Path

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

def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                doChangeFileName(file)

        if Path.is_file(Path(aPath)):
            doChangeFileName(Path(aPath))
            
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass