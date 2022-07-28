# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
from PIL import Image
import sys
import os

# https://imagemagick.org/
# 需要ImageMagick包中的convert.exe
# ImageMagick-7.1.0-portable-Q16-HDRI-x64.zip
# convert old.jpg -crop 128x128 new.jpg

def main(inputPath):
    # 设置文件类型
    #fileType = ['.png']
    fileType = ['.png','.jpg']
    # 设置新图片的文件名结尾
    # 左页
    leftImgName = '_left'
    # 右页
    rightImgName = '_right'
    
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if file.suffix.lower() in fileType:
                    img = Image.open(file)
                    imgWidth, imgHeight = img.size
                    cmd = 'convert.exe "' + str(file) + '" -crop ' + str(imgWidth / 2) + 'x' + str(imgHeight) + ' "' + str(file) + '"'
                    os.system(cmd)
                
        if Path.is_file(Path(aPath)):
            if Path(aPath).suffix.lower() in fileType:
                img = Image.open(Path(aPath))
                imgWidth, imgHeight = img.size
                cmd = 'convert.exe "' + aPath + '" -crop ' + str(imgWidth / 2) + 'x' + str(imgHeight) + ' "' + aPath + '"'
                os.system(cmd)

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass