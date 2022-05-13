# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
from PIL import Image
from shutil import copyfile
import sys
import os

# https://imagemagick.org/
# 需要ImageMagick包中的convert.exe
# ImageMagick-7.1.0-portable-Q16-HDRI-x64.zip
# convert +append u-0.jpg u-1.jpg u.jpg

def main(inputPath):
    # 设置文件类型
    #fileType = ['.png']
    fileType = ['.png','.jpg']
    # 从右到左 = True, 从左到右 = False
    RightToLeftDirection = True
    # 设置第一张单页图片是第几张，第一张 = 0
    setFirstSinglePage = 3
    
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            # 读取所有文件
            allFilesPath = []
            allFilesPathWithoutDoublePage = []
            allFilesPathWithDoublePage = []
            for file in Path(aPath).glob('*'):
                if file.suffix.lower() in fileType:
                    allFilesPath.append(file)
            # 新建文件夹存放合并后的图片
            newPath = Path(aPath).joinpath('convertedImageFolder')
            if not newPath.exists():
                Path.mkdir(newPath)
            # 获取单页文件宽度
            normalImgWidth = Image.open(allFilesPath[setFirstSinglePage]).size[0]
            for i in range(0, len(allFilesPath)):
                # 跳过双页文件
                if not Image.open(allFilesPath[i]).size[0] > normalImgWidth * 1.8:
                    allFilesPathWithoutDoublePage.append(allFilesPath[i])
                else:
                    allFilesPathWithDoublePage.append(allFilesPath[i])
            allFilesPath = allFilesPathWithoutDoublePage
            for img in allFilesPathWithDoublePage:
                copyfile(img, newPath.joinpath(img.name))
                print('copy ' + str(newPath.joinpath(img.name)))
            for imgIndex in range(0, len(allFilesPathWithoutDoublePage), 2):
                if Path.is_file(allFilesPathWithoutDoublePage[imgIndex]) and Path.is_file(allFilesPathWithoutDoublePage[imgIndex + 1]) and (allFilesPathWithoutDoublePage[imgIndex].suffix == allFilesPathWithoutDoublePage[imgIndex + 1].suffix):
                    if RightToLeftDirection:
                        cmd = 'convert.exe +append "' + str(allFilesPathWithoutDoublePage[imgIndex + 1]) + '" "' + str(allFilesPathWithoutDoublePage[imgIndex]) + '" "' + str(Path(newPath).joinpath(allFilesPathWithoutDoublePage[imgIndex].stem + '_' + allFilesPathWithoutDoublePage[imgIndex + 1].stem + allFilesPathWithoutDoublePage[imgIndex].suffix)) + '"'
                    else:
                        cmd = 'convert.exe +append "' + str(allFilesPathWithoutDoublePage[imgIndex]) + '" "' + str(allFilesPathWithoutDoublePage[imgIndex + 1]) + '" "' + str(Path(newPath).joinpath(allFilesPathWithoutDoublePage[imgIndex].stem + '_' + allFilesPathWithoutDoublePage[imgIndex + 1].stem + allFilesPathWithoutDoublePage[imgIndex].suffix)) + '"'
                    print(cmd)
                    os.system(cmd)            
               
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass