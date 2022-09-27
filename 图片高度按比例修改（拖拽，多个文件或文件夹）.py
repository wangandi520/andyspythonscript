# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip install pillow

from PIL import Image
from pathlib import Path
import sys

def doChangeImageHeight(filePath):
    # type(filePath): Path
    # 图片高度
    imgHeight = 3000
    # 设置文件类型
    #fileType = ['.png']
    fileType = ['.png','.jpg']
    if filePath.suffix.lower() in fileType:
        img = Image.open(filePath)
        imgWidth = int(img.size[0] / (img.size[1] / imgHeight ))
        img = img.resize((imgWidth, imgHeight),Image.ANTIALIAS) 
        img.save(filePath.parent.joinpath(filePath.stem + '_' + str(imgHeight) + filePath.suffix)) 

def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                doChangeImageHeight(file)
                
        if Path.is_file(Path(aPath)):
            doChangeImageHeight(Path(aPath))

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass