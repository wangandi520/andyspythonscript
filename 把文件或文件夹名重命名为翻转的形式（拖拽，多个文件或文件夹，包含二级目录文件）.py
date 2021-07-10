# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
    
def main(inputPath):
    del inputPath[0]
    
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('*'):
                newFileName = Path(file).stem[::-1] + Path(file).suffix
                Path(file).rename(Path(file).parent.joinpath(newFileName))
            newFolderName = Path(aPath).name[::-1]
            Path(aPath).rename(Path(aPath).parent.joinpath(newFolderName))
                
        if Path.is_file(Path(aPath)):
            newFileName = Path(aPath).stem[::-1] + Path(aPath).suffix
            Path(aPath).rename(Path(aPath).parent.joinpath(newFileName))
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass