# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import os

# https://imagemagick.org/
# 需要ImageMagick包中的convert.exe
# ImageMagick-7.1.0-portable-Q16-HDRI-x64.zip
# convert +append u-0.jpg u-1.jpg u.jpg

def main(inputPath):
    # 合并的文件的文件名
    convertFileName = 'new01.jpg'
    # 合并的压缩后文件名
    resizeFileName = 'new02.jpg'
    # 压缩比例（%）
    resizeNum = '75'
    # 垂直合并
    setMethod = '-'
    # 水平合并
    # setMethod = '+'
    
    del inputPath[0]
    allFilesPath = ''
    for aPath in inputPath:
        if Path.is_file(Path(aPath)):
            # 读取所有文件
            allFilesPath = allFilesPath + '"' + aPath + '" '

    if setMethod == '-':
        print('合并方式：垂直合并，新文件名：' + convertFileName + '，压缩后文件名：' + resizeFileName + '，压缩比例：' + resizeNum  + '%')
    elif setMethod == '+':
        print('合并方式：水平合并，新文件名：' + convertFileName + '，压缩后文件名：' + resizeFileName + '，压缩比例：' + resizeNum  + '%')
    print()
    
    convertCmd = 'convert.exe ' + setMethod + 'append ' + allFilesPath + '"' + convertFileName + '"'
    print(convertCmd)
    os.system(convertCmd)   
    resizeCmd = 'convert -quality ' + resizeNum + '% ' + convertFileName + ' ' + resizeFileName
    print(resizeCmd)
    os.system(resizeCmd)   
               
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass