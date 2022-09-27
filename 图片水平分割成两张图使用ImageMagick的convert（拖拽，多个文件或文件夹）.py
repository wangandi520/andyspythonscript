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
# https://imagemagick.org/script/command-line-options.php#crop

def doCrop(filePath):
    # 设置图片质量，越大体积越大，1到100，质量85体积差不多容差20，质量100三倍体积容差5
    setQuality = 85
    # 设置新图片的文件名结尾
    # 左页
    leftImgName = '_left'
    # 右页
    rightImgName = '_right'
    img = Image.open(filePath)
    imgWidth, imgHeight = img.size
    cmd = 'convert.exe "' + str(filePath) + '" -crop ' + str(imgWidth / 2) + 'x' + str(imgHeight) + ' -quality ' + str(setQuality) + ' "' + str(filePath) + '"'
    print(cmd)
    os.system(cmd)
    
def main(inputPath):
    # 设置文件类型
    fileType = ['.png','.jpg']
    
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if file.suffix.lower() in fileType:
                    doCrop(file)
                
        if Path.is_file(Path(aPath)):
            if Path(aPath).suffix.lower() in fileType:
                doCrop(Path(aPath))

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass