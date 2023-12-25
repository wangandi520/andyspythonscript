# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import os

def doCMD(filePath):
    # 需要运行的脚本的地址，地址要双斜杠，例如'D:\\new\\test.py'
    # 效果，你拖拽了文件夹1和文件1.txt，文件夹1里有2.txt，相当于运行test.py 2.txt 1.txt
    myCMD = 'D:\\new\\test.py'
    cmd = myCMD + ' "' + str(filePath) + '"'
    os.system(cmd)
    
def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                doCMD(file)
                
        if Path.is_file(Path(aPath)):
            doCMD(Path(aPath))

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass