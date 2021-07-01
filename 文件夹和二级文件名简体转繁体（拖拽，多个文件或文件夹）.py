# encoding:utf-8
# pip install opencc-python-reimplemented
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
from opencc import OpenCC
import sys
    
def main(inputPath):
    del inputPath[0]
    
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('*'):
                fileName = Path(file).name
                TraditionalName = OpenCC('s2t').convert(fileName)
                Path(file).rename(Path(file).parent.joinpath(TraditionalName))
            folderName = Path(aPath).name
            TraditionalName = OpenCC('s2t').convert(folderName)
            Path(aPath).rename(Path(aPath).parent.joinpath(TraditionalName))
                
        if Path.is_file(Path(aPath)):
            fileName = Path(aPath).name
            TraditionalName = OpenCC('s2t').convert(fileName)
            Path(aPath).rename(Path(aPath).parent.joinpath(TraditionalName))
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass