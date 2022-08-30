# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip install pillow

from PIL import Image
from pathlib import Path
import sys

def doVerify(filePath):
    # type(filePath): Path
    # 设置文件类型
    fileType = ['.png','.jpg','.jpeg','.bmp','.webp']
    if filePath.suffix.lower() in fileType:
        try:  
            Image.open(filePath).verify() 
        except:  
            print(filePath.name)

def main(inputPath):
    print('只显示可能损坏的文件名：')
    
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                doVerify(file)
                
        if Path.is_file(Path(aPath)):
            doVerify(Path(aPath))

    print('检测结束。')
    input()
    
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass