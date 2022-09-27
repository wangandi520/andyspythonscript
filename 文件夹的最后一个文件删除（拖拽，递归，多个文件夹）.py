# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
    
def main(inputPath):
    allallFilePath = []
    for aPath in inputPath[1:]:
        if Path.is_dir(Path(aPath)):
            allFilePath = []
            for file in Path(aPath).glob('**/*'):
                if Path.is_file(file):
                    allFilePath.append(file)
            allFilePath.sort()     
            allallFilePath.append(allFilePath[-1])
    for eachFile in allallFilePath:
        print(eachFile)
    myChoice = input('是否要删除以上文件, (y)es or (n)o:')
    if myChoice.lower() in ['y', 'yes']:
        for eachFile in allallFilePath:
            eachFile.unlink()
                
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass