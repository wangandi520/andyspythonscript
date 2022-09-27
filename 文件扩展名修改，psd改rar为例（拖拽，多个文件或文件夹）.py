# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
    
def main(inputPath):
    # 原扩展名
    oldSuffix = '.psd'
    # 新扩展名
    newSuffix = '.rar'
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('*'):
                if Path.is_file(file) and file.suffix == oldSuffix:
                    file.rename(Path(aPath).joinpath(file.stem + newSuffix))
                    print(file.name + '  ->  ' + file.stem)
        if Path.is_file(Path(aPath)) and Path(aPath).suffix == oldSuffix:
            Path(aPath).rename(Path(aPath).parent.joinpath(Path(aPath).stem + newSuffix))
            print(Path(aPath).name + '  ->  ' + Path(aPath).stem)
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass