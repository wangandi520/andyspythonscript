# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import re
    
def main(inputPath):
    # 文件名格式[][]xxx
    for file in inputPath[1:]:
        fileName = Path(file).name
        leftSymbol = []
        rightSymbol = []
        if '][' in fileName:
            getFileName = re.compile(r'[\[](.*?)[\]]', re.S)
            getFileNamePart = re.findall(getFileName, fileName)
            getLastIndex = len(getFileNamePart[0]) + len(getFileNamePart[1])
            newFileName = '[' + getFileNamePart[1] + '][' + getFileNamePart[0] + ']' + fileName[getLastIndex + 4:]
            Path(file).rename(Path(file).parent.joinpath(newFileName))
        else:
            print('文件（夹）名不符合规则：[][]')
            
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass