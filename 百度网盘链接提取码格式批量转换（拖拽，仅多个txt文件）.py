# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# https://github.com/wangandi520/andysTampermonkey

from pathlib import Path
import sys

def readfile(filename):
    #readfile
    with open(filename, mode='r', encoding='UTF-8') as file:
        filereadlines = file.readlines()
    #remove blank lines
    for i in filereadlines:
        if i == '\n':
            filereadlines.remove(i)
    #remove '\n' in line end
    for i in range(len(filereadlines)):
        filereadlines[i] = filereadlines[i].rstrip()
    return filereadlines

def writefile(filename,filereadlines):
    #write file
    newfile = open(filename, mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()

def main(inputPath):
    del inputPath[0]
    for file in inputPath:
        pathFile = Path(file)
        if Path.is_file(pathFile) and pathFile.suffix == '.txt':
            inputLines = readfile(pathFile)
            outputLines = []
            for line in inputLines:
                splitLine = line.split(' ')
                if len(splitLine) == 5 and splitLine[0] == '链接:' and splitLine[2] == '提取码:':
                    outputLines.append(splitLine[1] + '#' + splitLine[3] + '\n\n')
                else:
                    outputLines.append(line + '\n')
        writefile(str(pathFile.parent.joinpath(pathFile)) + '.txt', outputLines)
    
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass