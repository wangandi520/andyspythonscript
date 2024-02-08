# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip install numpy
# pip install pillow

import numpy
import sys
from PIL import Image
from pathlib import Path

# mode	描述
# 1	1位像素，黑白，每字节存储一个像素
# L	8位像素，黑白
# P 	8位像素，使用调色板映射到任何其他模式
# RGB 	3x8位像素，真彩
# RGBA 	4x8位像素，带透明蒙版的真彩
# CMYK 	4x8位像素，分色
# YCbCr 	3x8位像素，彩色视频格式
# LAB 	3x8位像素，L * a * b颜色空间
# HSV 	3x8位像素，色相，饱和度，值颜色空间
# I 	32位有符号整数像素
# F 	32位浮点像素
    
def getImageColor(eachFilePath):
    imgData = Image.open(eachFilePath)
    imgDataRGBA = imgData.convert('RGBA')
    imgDataRGBAArray = numpy.array(imgDataRGBA)
    uniqueImgDataRGBAArray = numpy.unique(imgDataRGBAArray)
    colorImageFolder = Path(eachFilePath).parent.joinpath(Path('color'))
    bwImageFolder = Path(eachFilePath).parent.joinpath(Path('bw'))
    if not colorImageFolder.exists():
        Path.mkdir(colorImageFolder)
    if not bwImageFolder.exists():
        Path.mkdir(bwImageFolder)
    # 颜色表数量 文件名
    print(str(len(uniqueImgDataRGBAArray)) + '    ' + Path(eachFilePath).name)
    if len(uniqueImgDataRGBAArray) < 256:
        # 黑白图片
        newFilePath = Path(eachFilePath.name).joinpath(Path(bwImageFolder)).joinpath(eachFilePath.name)
        Path(eachFilePath).replace(newFilePath)
    if len(uniqueImgDataRGBAArray) == 256:
        # 彩色图片
        newFilePath = Path(eachFilePath).joinpath(Path(colorImageFolder)).joinpath(eachFilePath.name)
        Path(eachFilePath).replace(newFilePath)

def main(inputPath):
    del inputPath[0]
    allFilePath = []
    mySuffix = ['.jpg', '.jpeg', '.png']
    for aPath in inputPath:
        if Path.is_file(Path(aPath)) and Path(aPath).suffix in mySuffix:
            allFilePath.append(Path(aPath))
        if Path.is_dir(Path(aPath)):
            for eachPath in Path(aPath).glob('**/*'):
                if Path(eachPath).suffix in mySuffix:
                    allFilePath.append(Path(eachPath))
    for eachFilePath in allFilePath:
        getImageColor(eachFilePath)
    input('按回车键退出')
    
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass