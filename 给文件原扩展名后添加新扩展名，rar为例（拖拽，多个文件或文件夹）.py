# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
    
def main(inputPath):
    # 新扩展名
    newSuffix = '.rar'
    
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('*'):
                if Path.is_file(file) and file.suffix != newSuffix:
                    file.rename(Path(aPath).joinpath(file.name + newSuffix))
        if Path.is_file(Path(aPath)) and Path(aPath).suffix != newSuffix:
            Path(aPath).rename(Path(aPath).parent.joinpath(Path(aPath).name + newSuffix))
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass