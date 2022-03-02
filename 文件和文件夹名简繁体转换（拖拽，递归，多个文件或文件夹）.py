# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip install opencc-python-reimplemented

from pathlib import Path
from opencc import OpenCC
import sys
    
def main(inputPath):
    del inputPath[0]
    
    # 注意安装第三行的文件
    # 简体->繁体 = t2s，繁体->简体 = s2t
    #setMethod = 's2t'
    setMethod = 't2s'
    
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                fileName = Path(file).name
                newFileName = OpenCC(setMethod).convert(fileName)
                Path(file).rename(Path(file).parent.joinpath(newFileName))
            folderName = Path(aPath).name
            newFileName = OpenCC(setMethod).convert(folderName)
            Path(aPath).rename(Path(aPath).parent.joinpath(newFileName))
                
        if Path.is_file(Path(aPath)):
            fileName = Path(aPath).name
            newFileName = OpenCC(setMethod).convert(fileName)
            Path(aPath).rename(Path(aPath).parent.joinpath(newFileName))
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass