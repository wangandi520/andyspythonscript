# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

import os
import sys
from pathlib import Path

def writefile(filereadlines, fileName):
    newfile = open(fileName + '.txt', mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()     
    
def main(inputPath):
    # 输出相对路径 = 1，还是绝对路径 = 0
    showPathType = 1
    del inputPath[0]
    
    for aPath in inputPath:
        allFolders = []
        for folder in Path(aPath).glob('**/*'):
            if Path.is_dir(folder):
                if showPathType:
                    allFolders.append(str(folder.relative_to(aPath)) + '\n')
                else:
                    allFolders.append(str(Path(aPath).joinpath(folder)) + '\n')
        writefile(allFolders, Path(aPath).name)
    
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass