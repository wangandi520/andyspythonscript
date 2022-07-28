# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

# pip install numpy
# pip install pillow

import numpy
import sys
from PIL import Image
from pathlib import Path
from codecs import encode

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

def formatFileSize(sizeBytes):
    # 格式化文件大小
    sizeBytes = float(sizeBytes)
    result = float(abs(sizeBytes))
    suffix = "B"
    if (result > 1024):
        suffix = "KB"
        mult = 1024
        result = result / 1024
    if (result > 1024):
        suffix = "MB"
        mult *= 1024
        result = result / 1024
    if (result > 1024):
        suffix = "GB"
        mult *= 1024
        result = result / 1024
    if (result > 1024):
        suffix = "TB"
        mult *= 1024
        result = result / 1000
    if (result > 1024):
        suffix = "PB"
        mult *= 1024
        result = result / 1024
    return format(result, '.2f') + suffix
        
def writeToFile(filename, filereadlines):
    newfile = open(filename + '.txt', mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()
    
def main(inputPath):

    #是否输出到文件
    outputToFile = False
    #是否显示exif等其他信息
    showOtherInfo = False
    # 设置文件类型
    #fileType = ['.png']
    fileType = ['.png','.jpg']
    
    allFileInfo = []
    
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if file.suffix.lower() in fileType:
                    imgData = Image.open(file)
                    allFileInfo.append('文件名： ' + str(file.name) + '\n')
                    allFileInfo.append('大小： ' + str(formatFileSize(file.stat().st_size)) + '\n')
                    allFileInfo.append('格式： ' + str(imgData.format) + '\n')
                    allFileInfo.append('宽度： ' + str(imgData.size[0]) + ' 像素\n')
                    allFileInfo.append('高度： ' + str(imgData.size[1]) + ' 像素\n')
                    allFileInfo.append('模式： ' + str(imgData.mode) + '\n')
                    if showOtherInfo:
                        allFileInfo.append('信息： ' + str(imgData.info) + '\n')
                    print('文件名： ' + str(file.name))
                    print('大小： ' + str(formatFileSize(file.stat().st_size)))
                    print('格式： ' + str(imgData.format))
                    print('宽度： ' + str(imgData.size[0]) + ' 像素')
                    print('高度： ' + str(imgData.size[1]) + ' 像素')
                    print('模式： ' + str(imgData.mode))
                    if showOtherInfo:
                        print('信息： ' + str(imgData.info))
                    imgDataRGBA = imgData.convert('RGBA')
                    imgDataRGBAArray = numpy.array(imgDataRGBA)
                    uniqueImgDataRGBAArray = numpy.unique(imgDataRGBAArray)
                    allFileInfo.append('颜色表数量： ' + str(len(uniqueImgDataRGBAArray)) + '\n')
                    print('颜色表数量： ' + str(len(uniqueImgDataRGBAArray)))
                    for eachColor in uniqueImgDataRGBAArray:
                        allFileInfo.append('rgb(' + str(eachColor) + ',' + str(eachColor) + ',' + str(eachColor) + ') #' + str(hex(eachColor))[2:] * 3 + '\n')
                        print('rgb(' + str(eachColor) + ',' + str(eachColor) + ',' + str(eachColor) + ') #' + str(hex(eachColor))[2:] * 3)
                    allFileInfo.append('\n')
                    imgData.close()
                    print()
                if file.suffix in ['.act', '.ACT']:
                    print('文件名： ' + str(file.name))
                    allFileInfo.append('文件名： ' + str(file.name) + '\n')
                    with open(file, 'rb') as actFile:
                        rawData = actFile.read()
                    hexData = encode(rawData, 'hex')
                    totalColorsCount = (int(hexData[-7:-4], 16))
                    misterious_count = (int(hexData[-4:-3], 16))
                    tempAllColors = [hexData[i:i+6].decode() for i in range(0, totalColorsCount*6, 6)]
                    allColors = []
                    allFileInfo.append('颜色表数量： ' + str(totalColorsCount) + '\n')
                    for eachColor in tempAllColors:
                        print('rgb(' + str(int(eachColor[:2],16)) + ',' + str(int(eachColor[2:4],16)) + ',' + str(int(eachColor[4:6],16)) + ') #' + eachColor)
                        allFileInfo.append('rgb(' + str(int(eachColor[:2],16)) + ',' + str(int(eachColor[2:4],16)) + ',' + str(int(eachColor[4:6],16)) + ') #' + eachColor + '\n')
                    print()
                    allFileInfo.append('\n')
            
        if Path.is_file(Path(aPath)):
            if Path(aPath).suffix.lower() in fileType:
                imgData = Image.open(aPath)
                allFileInfo.append('文件名： ' + str(Path(aPath).name) + '\n')
                allFileInfo.append('大小： ' + str(formatFileSize(Path(aPath).stat().st_size)) + '\n')
                allFileInfo.append('格式： ' + str(imgData.format) + '\n')
                allFileInfo.append('宽度： ' + str(imgData.size[0]) + ' 像素\n')
                allFileInfo.append('高度： ' + str(imgData.size[1]) + ' 像素\n')
                allFileInfo.append('模式： ' + str(imgData.mode) + '\n')
                if showOtherInfo:
                    allFileInfo.append('信息： ' + str(imgData.info) + '\n')
                print('文件名： ' + str(Path(aPath).name))
                print('大小： ' + str(formatFileSize(Path(aPath).stat().st_size)))
                print('格式： ' + str(imgData.format))
                print('宽度： ' + str(imgData.size[0]) + ' 像素')
                print('高度： ' + str(imgData.size[1]) + ' 像素')
                print('模式： ' + str(imgData.mode))
                if showOtherInfo:
                    print('信息： ' + str(imgData.info))
                imgDataRGBA = imgData.convert('RGBA')
                imgDataRGBAArray = numpy.array(imgDataRGBA)
                uniqueImgDataRGBAArray = numpy.unique(imgDataRGBAArray)
                allFileInfo.append('颜色表数量： ' + str(len(uniqueImgDataRGBAArray)) + '\n')
                print('颜色表数量： ' + str(len(uniqueImgDataRGBAArray)))
                for eachColor in uniqueImgDataRGBAArray:
                    allFileInfo.append('rgb(' + str(eachColor) + ',' + str(eachColor) + ',' + str(eachColor) + ') #' + str(hex(eachColor))[2:] * 3 + '\n')
                    print('rgb(' + str(eachColor) + ',' + str(eachColor) + ',' + str(eachColor) + ') #' + str(hex(eachColor))[2:] * 3)
                allFileInfo.append('\n')
                imgData.close()
                print()
            if Path(aPath).suffix in ['.act', '.ACT']:
                print('文件名： ' + str(Path(aPath).name))
                allFileInfo.append('文件名： ' + str(Path(aPath).name) + '\n')
                with open(Path(aPath), 'rb') as actFile:
                    rawData = actFile.read()
                hexData = encode(rawData, 'hex')
                totalColorsCount = (int(hexData[-7:-4], 16))
                misterious_count = (int(hexData[-4:-3], 16))
                tempAllColors = [hexData[i:i+6].decode() for i in range(0, totalColorsCount*6, 6)]
                allColors = []
                allFileInfo.append('颜色表数量： ' + str(totalColorsCount) + '\n')
                print('颜色表数量： ' + str(totalColorsCount))
                for eachColor in tempAllColors:
                    print('rgb(' + str(int(eachColor[:2],16)) + ',' + str(int(eachColor[2:4],16)) + ',' + str(int(eachColor[4:6],16)) + ') #' + eachColor)
                    allFileInfo.append('rgb(' + str(int(eachColor[:2],16)) + ',' + str(int(eachColor[2:4],16)) + ',' + str(int(eachColor[4:6],16)) + ') #' + eachColor + '\n')
                print()
                allFileInfo.append('\n')
    
    if outputToFile:
        writeToFile(allFileInfo[0][4:-1], allFileInfo)
        
    input('按回车键退出')
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass