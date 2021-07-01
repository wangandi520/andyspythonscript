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
                SimplifiedName = OpenCC('t2s').convert(fileName)
                Path(file).rename(Path(file).parent.joinpath(SimplifiedName))
            folderName = Path(aPath).name
            SimplifiedName = OpenCC('t2s').convert(folderName)
            Path(aPath).rename(Path(aPath).parent.joinpath(SimplifiedName))
                
        if Path.is_file(Path(aPath)):
            fileName = Path(aPath).name
            SimplifiedName = OpenCC('t2s').convert(fileName)
            Path(aPath).rename(Path(aPath).parent.joinpath(SimplifiedName))
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass