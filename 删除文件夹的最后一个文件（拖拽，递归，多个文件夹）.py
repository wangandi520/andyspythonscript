# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
    
def main(inputPath):
    del inputPath[0]
    
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            allFilePath = []
            for file in Path(aPath).glob('**/*'):
                if Path.is_file(file):
                    allFilePath.append(file)
            allFilePath[-1].unlink()
                
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass