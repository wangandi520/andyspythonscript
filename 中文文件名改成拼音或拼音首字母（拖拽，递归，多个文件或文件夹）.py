# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip install pypinyin

from pathlib import Path
from pypinyin import pinyin, lazy_pinyin, Style
import sys

def doPinyin(filePath):
    # type(filePath): Path
    # 文件名全拼 = 1，首字母 = 0
    setStyle = 1
    if setStyle:
        filePath.rename(filePath.parent.joinpath(''.join(lazy_pinyin(filePath.name))))
    else:
        filePath.rename(filePath.parent.joinpath(''.join(lazy_pinyin(filePath.name, style=Style.FIRST_LETTER))))
    
def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                doPinyin(file)
                    
        if Path.is_file(Path(aPath)):
            doPinyin(Path(aPath))
            
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass