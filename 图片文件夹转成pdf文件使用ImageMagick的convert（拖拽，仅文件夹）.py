# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import os

# https://mupdf.com/downloads/archive/mupdf-1.20.0-windows.zip
# https://imagemagick.org/script/convert.php
# mutool.exe convert -o 1.pdf 1.jpg 2.jpg

def doConvert(filePath):
    # type(filePath): Path
    print('正在制作' + str(filePath.name) + '.pdf"')
    cmd = 'convert.exe ' + str(filePath) + '\* "' + str(filePath.name) + '.pdf"'
    os.system(cmd)
    print('制作完成')
        
def main(inputPath):
    for aPath in inputPath[1:]:
        if Path.is_dir(Path(aPath)):
            doConvert(Path(aPath))

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass