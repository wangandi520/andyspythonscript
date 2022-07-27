# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip install fleep
# https://pypi.org/project/fleep/

import sys
import fleep
from pathlib import Path

def doChangeFileSuffix(filePath):
    # typeof(filePath): Path
    # 把文件扩展名改成真正的扩展名 = True，不改名只显示信息 = False
    renameToRealSuffix = False
    # 有多个可能时，强行修改成第N个扩展名，不强行修改 = -1，改成第1个 = 0，改成第2个 = 1
    forceRenameToRealSuffixIndex = -1
    
    if Path.is_file(filePath):
        with open(filePath, 'rb') as openFile:
            info = fleep.get(openFile.read(128))
        if not info.extension_matches(filePath.suffix[1:]):
            if renameToRealSuffix and len(info.extension) == 1:
                filePath.rename(filePath.parent.joinpath(filePath.stem + '.' + info.extension[0]))
                print('已修改， ' + filePath.name + ' -> ' + filePath.stem + '.' + info.extension[0])
            elif renameToRealSuffix and len(info.extension) > 1 and forceRenameToRealSuffixIndex >= 0:
                filePath.rename(filePath.parent.joinpath(filePath.stem + '.' + info.extension[forceRenameToRealSuffixIndex]))
                print('已修改， ' + filePath.name + ' -> ' + filePath.stem + '.' + info.extension[forceRenameToRealSuffixIndex])
            else:
                if len(info.extension) == 1:
                    print('未修改， ' + filePath.name + ' 的扩展名可能是 ' + info.extension[0])
                if len(info.extension) > 1:
                    print('未修改， ' + filePath.name + ' 的扩展名可能有多种可能： ' + ', '.join(info.extension))
        
def main(inputPath):
    print('如果需要修改扩展名请把第13行改为renameToRealSuffix = True')
    
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                doChangeFileSuffix(file)

        if Path.is_file(Path(aPath)):
            doChangeFileSuffix(Path(aPath))
    
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