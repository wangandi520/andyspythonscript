# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
    
def main(inputPath):
    # 新文件名，不修改扩展名
    newFileName = '0001'
    
    del inputPath[0]
    
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            allFilePath = []
            for file in Path(aPath).glob('**/*'):
                if Path.is_file(file):
                    allFilePath.append(file)
            allFilePath[-1].rename(allFilePath[-1].parent.joinpath(newFileName + allFilePath[-1].suffix))
                
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass