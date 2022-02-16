# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

# py -m ensurepip --upgrade
# pip install numpy
# pip install pillow

import numpy
import sys
from PIL import Image
from pathlib import Path

def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('*'):
                img = Image.open(file)
                img = Image.fromarray(numpy.uint8(img.convert('L')))  # *255
                img.save(file.parent.joinpath(file.stem + ' new.png'))

        if Path.is_file(Path(aPath)):
            file = Path(aPath)
            img = Image.open(file)
            img = Image.fromarray(numpy.uint8(img.convert('L')))  # *255
            img.save(file.parent.joinpath(file.stem + ' new.png'))
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass