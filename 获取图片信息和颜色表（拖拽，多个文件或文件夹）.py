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

def writeToFile(filename, filereadlines):
    newfile = open(filename + '.txt', mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()
    
def main(inputPath):

    #是否输出到文件
    outputToFile = True
    #是否显示exif等其他信息
    showOtherInfo = False
    
    allFileInfo = []
    
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                imgData = Image.open(file)
                allFileInfo.append('文件名： ' + str(file.name) + '\n')
                allFileInfo.append('格式： ' + str(imgData.format) + '\n')
                allFileInfo.append('宽度： ' + str(imgData.size[0]) + ' 像素\n')
                allFileInfo.append('高度： ' + str(imgData.size[1]) + ' 像素\n')
                allFileInfo.append('模式： ' + str(imgData.mode) + '\n')
                if showOtherInfo:
                    allFileInfo.append('信息： ' + str(imgData.info) + '\n')
                
                print('文件名： ' + str(file.name))
                print('格式： ' + str(imgData.format))
                print('宽度： ' + str(imgData.size[0]) + ' 像素')
                print('高度： ' + str(imgData.size[1]) + ' 像素')
                print('模式： ' + str(imgData.mode))
                if showOtherInfo:
                    print('信息： ' + str(imgData.info))
                
                imgDataRGBA = imgData.convert('RGBA')
                imgDataRGBAArray = numpy.array(imgDataRGBA)
                uniqueImgDataRGBAArray = numpy.unique(imgDataRGBAArray)
                allFileInfo.append('颜色表： ' + str(len(uniqueImgDataRGBAArray)) + '\n')
                print('颜色表： ' + str(len(uniqueImgDataRGBAArray)))
                for eachColor in uniqueImgDataRGBAArray:
                    allFileInfo.append('rgb(' + str(eachColor) + ',' + str(eachColor) + ',' + str(eachColor) + ') #' + str(hex(eachColor))[2:] * 3 + '\n')
                    print('rgb(' + str(eachColor) + ',' + str(eachColor) + ',' + str(eachColor) + ') #' + str(hex(eachColor))[2:] * 3)
                allFileInfo.append('\n')
                print()
            
        if Path.is_file(Path(aPath)):
            imgData = Image.open(aPath)
            allFileInfo.append('文件名： ' + str(Path(aPath).name) + '\n')
            allFileInfo.append('格式： ' + str(imgData.format) + '\n')
            allFileInfo.append('宽度： ' + str(imgData.size[0]) + ' 像素\n')
            allFileInfo.append('高度： ' + str(imgData.size[1]) + ' 像素\n')
            allFileInfo.append('模式： ' + str(imgData.mode) + '\n')
            if showOtherInfo:
                allFileInfo.append('信息： ' + str(imgData.info) + '\n')
        
            print('文件名： ' + str(Path(aPath).name))
            print('格式： ' + str(imgData.format))
            print('宽度： ' + str(imgData.size[0]) + ' 像素')
            print('高度： ' + str(imgData.size[1]) + ' 像素')
            print('模式： ' + str(imgData.mode))
            if showOtherInfo:
                print('信息： ' + str(imgData.info))
            
            imgDataRGBA = imgData.convert('RGBA')
            imgDataRGBAArray = numpy.array(imgDataRGBA)
            uniqueImgDataRGBAArray = numpy.unique(imgDataRGBAArray)
            allFileInfo.append('颜色表： ' + str(len(uniqueImgDataRGBAArray)) + '\n')
            print('颜色表： ' + str(len(uniqueImgDataRGBAArray)))
            for eachColor in uniqueImgDataRGBAArray:
                allFileInfo.append('rgb(' + str(eachColor) + ',' + str(eachColor) + ',' + str(eachColor) + ') #' + str(hex(eachColor))[2:] * 3 + '\n')
                print('rgb(' + str(eachColor) + ',' + str(eachColor) + ',' + str(eachColor) + ') #' + str(hex(eachColor))[2:] * 3)
            allFileInfo.append('\n')
            print()
    
    if outputToFile:
        writeToFile(allFileInfo[0][4:-1], allFileInfo)
        
    input()
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass