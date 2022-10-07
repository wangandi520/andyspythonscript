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
    print('正在生成' + str(filePath.name) + '.pdf')
    cmd = 'convert.exe "' + str(filePath) + '\*" "' + str(filePath) + '.pdf"'
    if Path(str(filePath) + '.pdf').exists():
        print('错误，文件已存在')
    else:
        os.system(cmd)
        print('生成完成：' + str(filePath) + '.pdf')
        
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