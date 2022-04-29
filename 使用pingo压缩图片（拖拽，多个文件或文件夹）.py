# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import os.path
  
# https://css-ig.net/bin/pingo-win64.zip
# usage (examples)
# pingo [options] files/folders pingo -s0 *.png pingo -s0 myfolder pingo -s0 c:\myfolder
# PNG — lossless
# pingo -sN file.png
# N from 0 to 9, optimization level

def main(inputPath):
    # 设置文件类型
    #fileType = ['.png']
    fileType = ['.png','.jpg']
    
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if file.suffix in fileType:
                    print('pingo.exe -s9 "' + str(file) + '"')
                    cmd = 'pingo.exe -s9 "' + str(file) + '"'
                    os.system(cmd)
                
        if Path.is_file(Path(aPath)):
            if Path(aPath).suffix in fileType:
                print('pingo.exe -s9 "' + aPath)
                cmd = 'pingo.exe -s9 "' + aPath + '"'
                os.system(cmd)

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass