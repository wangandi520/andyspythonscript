# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip install opencc-python-reimplemented

from pathlib import Path
from opencc import OpenCC
import sys

def doOpenCC(filePath):
    # type(filePath): Path
    # 注意安装第三行的文件
    # 简体->繁体 = t2s，繁体->简体 = s2t
    setMethod = 's2t'
    #setMethod = 't2s'
    fileName = filePath.name
    newFileName = OpenCC(setMethod).convert(fileName)
    filePath.rename(filePath.parent.joinpath(newFileName))

def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                doOpenCC(file)
            doOpenCC(Path(aPath))
                
        if Path.is_file(Path(aPath)):
            doOpenCC(Path(aPath))
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass