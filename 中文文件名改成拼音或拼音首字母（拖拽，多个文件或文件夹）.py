# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip install pypinyin

from pathlib import Path
from pypinyin import pinyin, lazy_pinyin, Style
import sys
    
def main(inputPath):
    # 文件名全拼 = 1，首字母 = 0
    setStyle = 1
    
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('*'):
                if Path.is_file(file):
                    if setStyle:
                        file.rename(Path(aPath).joinpath(''.join(lazy_pinyin(file.name))))
                    else:
                        file.rename(Path(aPath).joinpath(''.join(lazy_pinyin(file.name, style=Style.FIRST_LETTER))))
        if Path.is_file(Path(aPath)):
            if setStyle:
                Path(aPath).rename(Path(aPath).parent.joinpath(''.join(lazy_pinyin(Path(aPath).name))))
            else:
                Path(aPath).rename(Path(aPath).parent.joinpath(''.join(lazy_pinyin(Path(aPath).name, style=Style.FIRST_LETTER))))
            
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass