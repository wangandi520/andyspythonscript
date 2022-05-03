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
    
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            allFilesPath = []
            for file in Path(aPath).glob('**/*'):
                if file.suffix in fileType:
                    allFilesPath.append(file)
            for imgIndex in range(0, len(allFilesPath), 2):
                if Path.is_file(allFilesPath[imgIndex]) and Path.is_file(allFilesPath[imgIndex + 1]) and (allFilesPath[imgIndex].suffix == allFilesPath[imgIndex + 1].suffix):
                    cmd = 'convert.exe +append "' + str(allFilesPath[imgIndex]) + '" "' + str(allFilesPath[imgIndex + 1]) + '" "' + str(Path(aPath).joinpath(allFilesPath[imgIndex].stem + '_' + allFilesPath[imgIndex + 1].stem + allFilesPath[imgIndex].suffix)) + '"'
                    print(cmd)
                    os.system(cmd)
               
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass