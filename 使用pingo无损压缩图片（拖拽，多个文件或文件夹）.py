# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import os.path
  
# https://css-ig.net/bin/pingo-win64.zip
# 需要pingo.exe
# usage (examples)
# pingo [options] files/folders pingo -s0 *.png pingo -s0 myfolder pingo -s0 c:\myfolder
# PNG — lossless
# pingo -sN file.png
# N from 0 to 9, optimization level

def doPingo(filePath):
    # typeof(filePath): Path
    # 文件格式，暂时支持png jpg
    # fileType = ['.png','.jpg']
    
    if filePath.suffix == '.png':
        cmd = 'pingo.exe -s9 "' + str(filePath) + '"'
        os.system(cmd)
    if filePath.suffix == '.jpg':
        cmd = 'pingo.exe -jpgtype=0 -s0 "' + str(filePath) + '"'
        os.system(cmd)
    
def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                doPingo(file)
                
        if Path.is_file(Path(aPath)):
            doPingo(Path(aPath))

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass