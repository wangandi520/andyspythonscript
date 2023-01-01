# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip install pillow

from PIL import Image
from pathlib import Path
import sys

def doVerify(filePath): 
    fileType = ['.png','.jpg','.jpeg','.bmp','.webp']
    fileValid = True
    if filePath.suffix.lower() in fileType:
        fileObj = open(filePath, 'rb')
        fileRead = fileObj.read()
        if fileRead[6:10] in (b'JFIF', b'Exif'):
            if not fileRead.rstrip(b'\0\r\n').endswith(b'\xff\xd9'):
                fileValid = False
        else:        
            try:  
                Image.open(fileObj).verify() 
            except:  
                fileValid = False
    return fileValid

def main(inputPath):
    print('只显示可能损坏的文件名：')
    
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if not doVerify(file):
                    print(file)
                
        if Path.is_file(Path(aPath)):
            if not doVerify(Path(aPath)):
                print(Path(aPath))

    print('检测结束。')
    input()
    
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass