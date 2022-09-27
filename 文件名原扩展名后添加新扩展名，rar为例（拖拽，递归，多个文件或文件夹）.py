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
            for file in Path(aPath).glob('**/*'):
                if Path.is_file(file) and file.suffix.lower() != newSuffix:
                    try:
                        file.rename(Path(file).parent.joinpath(file.name + newSuffix))
                    except FileExistsError:
                        print('文件已存在')
        if Path.is_file(Path(aPath)) and Path(aPath).suffix.lower() != newSuffix:
            try:
                Path(aPath).rename(Path(aPath).parent.joinpath(Path(aPath).name + newSuffix))
            except FileExistsError:
                print('文件已存在')
                
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass