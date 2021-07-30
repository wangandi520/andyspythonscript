# encoding:utf-8
# pip3 install opencv-python
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import cv2
import sys

def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('*.png'):
                oldImg = cv2.imread(str(file), 0)
                print(str(Path(aPath).joinpath(file.name)))
                retVal, newImg = cv2.threshold(oldImg, 127, 255, cv2.THRESH_BINARY)
                cv2.imwrite(str(Path(aPath).joinpath(file.name)), newImg, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
        if Path.is_file(Path(aPath)) and Path(aPath).suffix == '.png':
            oldImg = cv2.imread(str(aPath), 0)
            print(Path(aPath).parent.joinpath(aPath))
            retVal, newImg = cv2.threshold(oldImg, 127, 255, cv2.THRESH_BINARY)
            cv2.imwrite(str(Path(aPath).parent.joinpath(aPath)), newImg, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass