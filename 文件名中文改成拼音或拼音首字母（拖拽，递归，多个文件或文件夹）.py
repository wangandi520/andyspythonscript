# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip install pypinyin

from pathlib import Path
from pypinyin import pinyin, lazy_pinyin, Style
from typing import List, Union
import sys

# 把可以更改的设置都放在这里
CONFIG = {
    # 重命名成全拼 = True，首字母 = False
    'setStyle': True
}

def doConvert(filePath):
    # type(filePath): Path
    # 文件名全拼 = 1，首字母 = 0
    setStyle = 1
    if CONFIG.get('setStyle', True):
        filePath.rename(filePath.parent.joinpath(''.join(lazy_pinyin(filePath.name))))
    else:
        filePath.rename(filePath.parent.joinpath(''.join(lazy_pinyin(filePath.name, style=Style.FIRST_LETTER))))
    
def main(inputPath):
    try:
        for eachPath in inputPath[1:]:
            eachPath = Path(eachPath)
            if eachPath.is_dir():
                for eachFile in eachPath.glob('**/*'):
                    doConvert(eachFile)
            elif eachPath.is_file():
                doConvert(eachPath)
    except Exception as e:
        print(f'程序执行出错：{str(e)}')
       
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
        else:
            print('请拖拽文件到本脚本，或者命令行运行时添加文件路径')
    except IndexError:
        pass