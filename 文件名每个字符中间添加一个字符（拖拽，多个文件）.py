# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
    
def main(inputPath):
    del inputPath[0]
    # 需要添加的字符
    addChar = '啊'
    for aPath in inputPath:
        if Path.is_file(Path(aPath)):
            newFileName = ''
            for eachChar in Path(aPath).stem:
                newFileName = newFileName + eachChar + addChar
            newFileName = newFileName + Path(aPath).suffix
            Path(aPath).rename(Path(aPath).parent.joinpath(newFileName))
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass