# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
    
def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('*.1234'):
                if Path.is_file(file) and file.suffix == '.1234':
                    file.rename(Path(aPath).joinpath(file.stem))
                    print(file.name + '  ->  ' + file.stem)
        if Path.is_file(Path(aPath)) and Path(aPath).suffix == '.1234':
            Path(aPath).rename(Path(aPath).parent.joinpath(Path(aPath).stem))
            print(Path(aPath).name + '  ->  ' + Path(aPath).stem)
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass