# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import os

# https://imagemagick.org/
# 需要ImageMagick包中的convert.exe
# ImageMagick-7.1.0-portable-Q16-HDRI-x64.zip
# convert -rotate 90 jb.jpg 90.jpg

def main(inputPath):
    # 设置文件类型
    #fileType = ['.png']
    fileType = ['.png','.jpg']
    # 旋转角度，90 = 顺时针90度
    setRotate = 90
    
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if file.suffix.lower() in fileType:
                    cmd = 'convert.exe -rotate ' + str(setRotate) + ' "' + str(file) + '" "' + str(file) + '"'
                    os.system(cmd)
                
        if Path.is_file(Path(aPath)):
            if Path(aPath).suffix.lower() in fileType:
                cmd = 'convert.exe -rotate ' + str(setRotate) + ' "' + aPath + '" "' + aPath + '"'
                os.system(cmd)

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass