# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip install fleep
# https://pypi.org/project/fleep/

import sys
import fleep
from pathlib import Path

def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        # 把文件扩展名改成真正的扩展名 = True，不改名只显示信息 = False
        renameToRealSuffix = False
        
        if not renameToRealSuffix:
            print('如果需要修改扩展名请把第14行改为renameToRealSuffix = True')
            print()
            
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if Path.is_file(file):
                    with open(file, 'rb') as openFile:
                        info = fleep.get(openFile.read(128))
                    if not info.extension_matches(Path(file).suffix[1:]):
                        if renameToRealSuffix and len(info.extension) == 1:
                            Path(file).rename(Path(file).parent.joinpath(Path(file).stem + '.' + info.extension[0]))
                            print('已修改，' + Path(file).name + ' -> ' + Path(file).stem + '.' + info.extension[0])
                        else:
                            if len(info.extension) == 1:
                                print('未修改，扩展名可能是 ' + info.extension[0] + '： ' + Path(file).name)
                            if len(info.extension) > 1:
                                print('未修改，这个文件的扩展名可能有多种可能： ' + ', '.join(info.extension))

        if Path.is_file(Path(aPath)):
            with open(aPath, 'rb') as openFile:
                info = fleep.get(openFile.read(128))
            if not info.extension_matches(Path(aPath).suffix[1:]):
                if renameToRealSuffix and len(info.extension) == 1:
                    Path(aPath).rename(Path(aPath).parent.joinpath(Path(aPath).stem + '.' + info.extension[0]))
                    print('已修改，' + Path(aPath).name + ' -> ' + Path(aPath).stem + '.' + info.extension[0])
                else:
                    if len(info.extension) == 1:
                        print('未修改，扩展名可能是 ' + info.extension[0] + '： ' + Path(aPath).name)
                    if len(info.extension) > 1:
                        print('未修改，这个文件的扩展名可能有多种可能： ' + ', '.join(info.extension))
    
    print()
    print('执行结束，如果没有输出，可是所有文件扩展名未出错')
    getInput = input('输入回车退出: ')
    print()
    
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass