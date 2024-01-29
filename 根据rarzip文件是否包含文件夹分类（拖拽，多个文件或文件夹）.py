# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import zipfile
import rarfile

def doClassifyFile(inputPath):
    # workMode = 1只显示是否包含文件夹不移动文件，workMode = 2会把分好类的文件移动到含文件夹，不含文件夹两个文件夹中
    workMode = 1
    withSubDir = []
    noSubDir = []
    file = inputPath
    if file.suffix == '.rar' and rarfile.is_rarfile(file):
        rf = rarfile.RarFile(file)
        noDir = True
        for eachFile in rf.infolist():
            if eachFile.is_dir():
                noDir = False
                if file not in withSubDir:
                    withSubDir.append(file)
                break
        if noDir and (file not in noSubDir):
            noSubDir.append(file)
        rf.close()
    if file.suffix == '.zip' and zipfile.is_zipfile(file):
        zf = zipfile.ZipFile(file)
        noDir = True
        for eachFile in zf.infolist():
            if eachFile.is_dir():
                noDir = False
                if file not in withSubDir:
                    withSubDir.append(file)
                break
        if noDir and (file not in noSubDir):
            noSubDir.append(file)
        zf.close()
    withSubDirPath = Path(file).parent.joinpath(Path('含文件夹'))
    noSubDirPath = Path(file).parent.joinpath(Path('不含文件夹'))
    if workMode  == 1:
        for file in withSubDir:
            print('  含文件夹 ' + str(file))
        for file in noSubDir:
            print('不含文件夹 ' + str(file))
    if workMode == 2:
        if not withSubDirPath.exists() and withSubDir:
            Path.mkdir(withSubDirPath)
        if not noSubDirPath.exists() and noSubDir:
            Path.mkdir(noSubDirPath)
        for file in withSubDir:
            print('  含文件夹 ' + str(file))
            Path(file).replace(withSubDirPath.joinpath(file.name))
        for file in noSubDir:
            print('不含文件夹 ' + str(file))
            Path(file).replace(noSubDirPath.joinpath(file.name))
            
def main(inputPath):
    del inputPath[0]
    allFilePath = []
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                allFilePath.append(file)
        if Path.is_file(Path(aPath)):
            allFilePath.append(Path(aPath))
    for eachFilePath in allFilePath:
        doClassifyFile(eachFilePath)
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass