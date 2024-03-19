# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# by Andy
# v0.1

from pathlib import Path
import sys

def writefile(fileName, allFileContent):
    with open(fileName, mode='w', encoding='UTF-8') as newfile:
        newfile.writelines(allFileContent)

def readfile(fileName):
    with open(fileName, mode='r', encoding='UTF-8') as newfile:
        allFileContent = newfile.readlines()
    return allFileContent

def doConvert(fileName):
    # readFileContent = readfile(fileName)
    # for eachLine in readFileContent:
        # print(eachLine)
    # newFileName = fileName.parent.joinpath(fileName.stem + '.html')
    # if not Path(newFileName).exists():
        # writefile(newFileName, ttempFileContent)
        
def main(inputPath):
    fileType = ['.txt']
    for aPath in inputPath[1:]:
        if Path.is_dir(Path(aPath)):
            for eachFile in Path(aPath).glob('**/*'):
                if (Path(eachFile).suffix.lower() in fileType):
                    doConvert(Path(eachFile))
        if Path.is_file(Path(aPath)):
            if (Path(aPath).suffix.lower() in fileType):
                doConvert(Path(aPath))

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass