# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import os
import piexif

# pip install piexif
# 需要pingo.exe
# https://css-ig.net/bin/pingo-win64.zip
# usage (examples)
# pingo [options] files/folders pingo -s0 *.png pingo -s0 myfolder pingo -s0 c:\myfolder
# PNG — lossless
# pingo -sN file.png
# N from 0 to 9, optimization level
# JPEG — lossless
# -jpgtype=M -sN in.jpg
# M from 0 to 2, compression type

def doPingo(filePath):
    # type(filePath): Path
    # 文件格式
    # fileType = ['.png','.jpg','.webp']
    # 是否保留jpg文件的metadata
    preserveJPGsMetadata = True
    
    if filePath.suffix.lower() == '.png':
        cmd = 'pingo.exe -lossless  "' + str(filePath) + '"'
        os.system(cmd)
    if filePath.suffix.lower() == '.jpg':
        if preserveJPGsMetadata:
            oldImgExif = piexif.dump(piexif.load(str(filePath)))
        cmd = 'pingo.exe -lossless  "' + str(filePath) + '"'
        os.system(cmd)
        if preserveJPGsMetadata:
            piexif.insert(oldImgExif, str(filePath))   
    if filePath.suffix.lower() == '.webp':
        cmd = 'pingo.exe -webp-lossless "' + str(filePath) + '"'
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