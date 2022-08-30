# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import os

# https://mupdf.com/downloads/archive/mupdf-1.20.0-windows.zip
# mutool.exe extract xxx.pdf

def domupdf(pythonPath, filePath):
    # type(pythonPath): Path
    # type(filePath): Path
    # 提取图片字体
    print('提取中...' + str(filePath.name))
    cmd = 'mutool.exe extract "' + str(filePath) + '"'
    output = os.popen(cmd).read().split('\n')
    # 提取的文件名
    allFileName = []
    for eachLine in output:
        if 'extracting' in eachLine:
            allFileName.append(eachLine[11:])
    # 新建文件夹
    newFolderPath = Path(filePath).parent.joinpath(Path(filePath).stem)
    if not newFolderPath.exists():
        Path.mkdir(newFolderPath)
    # 移动文件到文件夹
    for eachFileName in allFileName:
        oldFilePath = pythonPath.parent.joinpath(eachFileName)
        newFilePath = newFolderPath.joinpath(eachFileName)
        Path(oldFilePath).replace(newFilePath)
    print('提取完成')
        
def main(inputPath):
    # 设置文件类型
    fileType = ['.pdf']
    path0 = Path(inputPath[0])
    
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if file.suffix.lower() in fileType:
                    domupdf(path0, file)
                
        if Path.is_file(Path(aPath)):
            if Path(aPath).suffix.lower() in fileType: 
                domupdf(path0, Path(aPath))

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass