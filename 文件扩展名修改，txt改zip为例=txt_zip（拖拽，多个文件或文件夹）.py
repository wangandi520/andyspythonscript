# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
    
def doChangeSuffix(filePath, afterSuffix):
    # type(filePath): Path
    newFileName = Path(filePath).parent.joinpath(Path(filePath).stem + afterSuffix)
    if not newFileName.exists():
        Path(filePath).rename(newFileName)
        print(Path(filePath).name + '  ->  ' + Path(filePath).stem + afterSuffix)
	
def main(inputPath):
    # 任何旧扩展名都改成新扩展名 = True，否则 = False
    changeAllSuffix = False
    # 没有扩展名的文件添加新扩展名 = True，否则 = False
    addSuffix = True
    # 从文件名读取参数
    theFileName = Path(inputPath[0]).stem
    if ('=' in theFileName and '_' in theFileName):
        tempValue = theFileName.split('=')[1]
        tempValue = tempValue.split('（')[0]
        # 原扩展名
        oldSuffix = '.' + tempValue.split('_')[0]
        # 新扩展名
        newSuffix = '.' + tempValue.split('_')[1]
                 
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('*'):
                if addSuffix and file.suffix == '':
                    doChangeSuffix(file, newSuffix)
                if changeAllSuffix and Path.is_file(file):
                        doChangeSuffix(file, newSuffix)
                if not changeAllSuffix and Path.is_file(file) and file.suffix == oldSuffix:
                        doChangeSuffix(file, newSuffix)
        if Path.is_file(Path(aPath)):
            if addSuffix and Path(aPath).suffix == '':
                doChangeSuffix(aPath, newSuffix)
            if changeAllSuffix:
                doChangeSuffix(aPath, newSuffix)
            if not changeAllSuffix and Path(aPath).suffix == oldSuffix:
                    doChangeSuffix(aPath, newSuffix)
    
    print()
    print('执行结束')
    getInput = input('输入回车退出或右上角关闭: ')
    print()
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass