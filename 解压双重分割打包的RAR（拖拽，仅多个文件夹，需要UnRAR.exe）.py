# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# 需要UnRAR.exe 或 pip3 install unrar

from pathlib import Path
import sys
import os
import rarfile

def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        tmpPath = ''
        firstRARName = ''
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('*.part1.rar'):
                firstRARName = file 
                tmpPath = Path(aPath).joinpath(firstRARName)
            print('UnRAR: ' + str(tmpPath))
            rar = rarfile.RarFile(tmpPath)
            rar.extractall(Path(aPath), pwd = '1234')
            rar.close()
            for file in Path(aPath).glob('*.part1.rar'):
                if file.name != firstRARName:
                    tmpPath = Path(aPath).joinpath(file)
                    break
            print('UnRAR: ' + str(tmpPath))
            rar = rarfile.RarFile(tmpPath)
            rar.extractall(Path(aPath), pwd = '1234')
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