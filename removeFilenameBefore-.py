# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import os
    
def main(inputPath):
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            allFiles = os.listdir(aPath)
            for file in allFiles:
                if '-' in file:
                    #print('rename "' + str(Path(aPath).joinpath(Path(file))) + '" "' + file[file.index('-') + 2:] + '"')
                    os.system('rename "' + str(Path(aPath).joinpath(Path(file))) + '" "' + file[file.index('-') + 2:] + '"')
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass