# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import os
import rarfile
import os

def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        tmpPath = ''
        doRARName = ''
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('*.part1.rar'):
                doRARName = file 
                tmpPath = Path(aPath).joinpath(doRARName)
            print('UnRAR: ' + str(tmpPath))
            rar = rarfile.RarFile(tmpPath)
            rar.extractall(pwd = '1234')
            rar.close()
            for file in Path(aPath).glob('*.part1.rar'):
                if file.name != doRARName:
                    doRARName = file.name 
                    tmpPath = Path(aPath).joinpath(doRARName)
            print('UnRAR: ' + str(tmpPath))
            rar = rarfile.RarFile(tmpPath)
            rar.extractall(pwd = '1234')
            rar.close()
            fileList = rar.namelist()
            print('Done: ')
            for file in fileList:
                print(file)

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass