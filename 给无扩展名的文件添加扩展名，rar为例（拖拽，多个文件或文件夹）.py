# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
    
def main(inputPath):
    suffix = '.rar'
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('*'):
                if Path.is_file(file) and file.suffix == '':
                    file.rename(Path(aPath).joinpath(file.name + suffix))
                    print(file.name + '  ->  ' + file.stem)
        if Path.is_file(Path(aPath)) and Path(aPath).suffix == '':
            Path(aPath).rename(Path(aPath).parent.joinpath(Path(aPath).name + suffix))
            print(Path(aPath).name + '  ->  ' + Path(aPath).stem)
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass