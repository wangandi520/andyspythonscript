# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import os

def doCMD(allFilePath):
    # 需要运行的脚本的地址
    myCMD = 'D:\\new\\test.py'
    for eachFilePath in allFilePath:
        cmd = myCMD + ' "' + str(eachFilePath) + '"'
        print(cmd)
        os.system(cmd)
    
def main(inputPath):
    del inputPath[0]
    allFilePath = []
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                allFilePath.append(file) 
        if Path.is_file(Path(aPath)):
            allFilePath.append(Path(aPath))
    doCMD(allFilePath)

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass