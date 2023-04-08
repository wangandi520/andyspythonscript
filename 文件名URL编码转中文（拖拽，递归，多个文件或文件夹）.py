# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip install opencc-python-reimplemented

from pathlib import Path
from urllib.parse import unquote
import sys

def doUTF8(filePath):
    # type(filePath): Path
    # %e1%e1的形式转成中文
    fileName = filePath.name
    newFileName = unquote(fileName, encoding="UTF-8")
    filePath.rename(filePath.parent.joinpath(newFileName))

def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                doUTF8(file)
            doUTF8(Path(aPath))
                
        if Path.is_file(Path(aPath)):
            doUTF8(Path(aPath))
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass