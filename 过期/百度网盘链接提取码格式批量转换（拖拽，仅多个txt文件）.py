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
        outputLines = []
        if Path.is_file(pathFile) and pathFile.suffix == '.txt':
            inputLines = readfile(pathFile)
            lastLine = ''
            for line in inputLines:
                if line.startswith('提取码'):
                    if line[3] == '：' and line[4] != ' ':
                        line = line.replace('：', ': ')
                    if lastLine[2] == '：' and lastLine[3] != ' ':
                        lastLine = lastLine.replace('：', ': ')
                    line = lastLine + ' ' + line 
                else:
                    outputLines.append(lastLine + '\n')
                lastLine = ''
                splitLine = line.split(' ')
                if len(splitLine) >= 4 and splitLine[0] == '链接:' and splitLine[2] == '提取码:':
                    outputLines.append(splitLine[1] + '#' + splitLine[3] + '\n\n')
                else:
                    if '提取码' in line:
                        outputLines.append(line + '\n')
                    else:
                        lastLine = line
        writefile(str(pathFile.parent.joinpath(pathFile)) + '.txt', outputLines)
    
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass