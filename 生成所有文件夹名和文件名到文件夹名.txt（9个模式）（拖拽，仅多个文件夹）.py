# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

import sys
from pathlib import Path

def writefile(filereadlines, fileName):
    newfile = open(fileName + '.txt', mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()     
    
def main(inputPath):
    del inputPath[0]
    # setType运行模式：
    # 1=输出所有文件名和文件夹名，使用绝对路径
    # 2=输出所有文件名和文件夹名，使用相对路径
    # 3=仅输出文件夹名，使用绝对路径
    # 4=仅输出文件夹名，使用相对路径
    # 5=仅输出文件名，使用绝对路径
    # 6=仅输出文件名，使用相对路径
    # 7=仅输出文件夹名，无路径
    # 8=仅输出文件名和扩展名，无路径
    # 9=仅输出文件名，无路径无扩展名
    setType = 9
    
    for aPath in inputPath:
        allData = []
        if Path.is_dir(Path(aPath)):
            for eachPath in Path(aPath).glob('**/*'):
                if setType == 1:
                    allData.append(str(Path(aPath).joinpath(eachPath)) + '\n')   
                if setType == 2:
                    allData.append(str(eachPath.relative_to(aPath)) + '\n')
                if setType == 3 and Path.is_dir(eachPath):
                    allData.append(str(Path(aPath).joinpath(eachPath)) + '\n')
                if setType == 4 and Path.is_dir(eachPath):
                    allData.append(str(eachPath.relative_to(aPath)) + '\n')
                if setType == 5 and Path.is_file(eachPath):
                    allData.append(str(Path(aPath).joinpath(eachPath)) + '\n')
                if setType == 6 and Path.is_file(eachPath):
                    allData.append(str(eachPath.relative_to(aPath)) + '\n')
                if setType == 7 and Path.is_dir(eachPath):
                    allData.append(str(eachPath.name) + '\n')
                if setType == 8 and Path.is_file(eachPath):
                    allData.append(str(eachPath.name) + '\n')
                if setType == 9 and Path.is_file(eachPath):
                    allData.append(str(eachPath.stem) + '\n') 
            writefile(allData, Path(aPath).name)
    
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass