# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip install ddddocr

from pathlib import Path
import ddddocr
import sys

def getCode(filePath):
    if filePath.suffix in ['.png', '.jpg', '.jpeg', '.gif']:
        ocr = ddddocr.DdddOcr()
        with open(filePath, 'rb') as f:
            img_bytes = f.read()
        getResult = ocr.classification(img_bytes)
        print(getResult)
        fileName = filePath.name
        filePath.rename(filePath.parent.joinpath(getResult + filePath.suffix))
    
def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                getCode(file)
                
        if Path.is_file(Path(aPath)):
            getCode(Path(aPath))
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass