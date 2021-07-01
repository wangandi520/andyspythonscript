# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from opencc import OpenCC
from pathlib import Path
import sys
import re
       
def main(inputPath):
    del inputPath[0]
    # 文件名设置成简体 = True，繁体 = False
    fileNameType = True
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            folderName = Path(aPath).name
            nameParts = re.findall("(\\[[^\\]]*\\])", folderName)
            if fileNameType:
                workName = OpenCC('t2s').convert(nameParts[0][1:-1])
                authorName = OpenCC('t2s').convert(nameParts[1][1:-1])
            else:
                workName = OpenCC('s2t').convert(nameParts[0][1:-1])
                authorName = OpenCC('s2t').convert(nameParts[1][1:-1])
            
            authorPath = Path(aPath).parent.joinpath(Path(authorName))
            if not authorPath.exists():
                Path.mkdir(authorPath)
            workPath = Path(authorPath).joinpath(Path(workName))
            if not workPath.exists():
                Path.mkdir(workPath)
            for file in Path(aPath).glob('*'):
                oldFilePath = Path(aPath).joinpath(Path(file.name))
                newFilePath = Path(workPath).joinpath(Path(file.name))
                Path(oldFilePath).replace(newFilePath)
            Path.rmdir(Path(aPath))
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass