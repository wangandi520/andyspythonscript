# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
from PIL import Image
import sys
import os.path

# https://imagemagick.org/
# 需要ImageMagick包中的convert.exe
# ImageMagick-7.1.0-portable-Q16-HDRI-x64.zip
# convert +append u-0.jpg u-1.jpg u.jpg

def main(inputPath):
    # 设置文件类型
    #fileType = ['.png']
    fileType = ['.png','.jpg']
    # 从右到左 = True, 从左到右 = False
    direction = True
    
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            allFilesPath = []
            for file in Path(aPath).glob('**/*'):
                if file.suffix in fileType:
                    allFilesPath.append(file)
            newPath = Path(aPath).joinpath('convertedImageFolder')
            if not newPath.exists():
                Path.mkdir(newPath)
            for imgIndex in range(0, len(allFilesPath), 2):
                if Path.is_file(allFilesPath[imgIndex]) and Path.is_file(allFilesPath[imgIndex + 1]) and (allFilesPath[imgIndex].suffix == allFilesPath[imgIndex + 1].suffix):
                    if direction:
                        cmd = 'convert.exe +append "' + str(allFilesPath[imgIndex + 1]) + '" "' + str(allFilesPath[imgIndex]) + '" "' + str(Path(newPath).joinpath(allFilesPath[imgIndex].stem + '_' + allFilesPath[imgIndex + 1].stem + allFilesPath[imgIndex].suffix)) + '"'
                    else:
                        cmd = 'convert.exe +append "' + str(allFilesPath[imgIndex]) + '" "' + str(allFilesPath[imgIndex + 1]) + '" "' + str(Path(newPath).joinpath(allFilesPath[imgIndex].stem + '_' + allFilesPath[imgIndex + 1].stem + allFilesPath[imgIndex].suffix)) + '"'
                    print(cmd)
                    os.system(cmd)
               
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass