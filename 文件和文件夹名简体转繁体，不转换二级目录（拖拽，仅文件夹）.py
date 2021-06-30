# encoding:utf-8
# pip install opencc-python-reimplemented
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
from opencc import OpenCC
import sys
    
def main(inputPath):
    del inputPath[0]
    
    for aPath in inputPath:
        fileName = Path(aPath).name
        TraditionalName = OpenCC('s2t').convert(fileName)
        Path(aPath).rename(Path(aPath).parent.joinpath(TraditionalName))
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass