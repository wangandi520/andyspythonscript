# encoding:utf-8

from pathlib import Path
import sys
import os

def readfile(filename):
    # readfile
    with open(filename, mode='r', encoding='UTF-8') as file:
        filereadlines = file.readlines()
    # remove blank lines
    for i in filereadlines:
        if i == '\n':
            filereadlines.remove(i)
    for i in range(len(filereadlines)):
        filereadlines[i] = filereadlines[i].rstrip()
    return filereadlines

def writefile(filename,filereadlines):
    # write file
    newfile = open(Path(filename).parent.joinpath(Path('new ' + Path(filename).name)), mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()
    
def removeSpan(filename):
    # span格式，只需要写前面一部分
    spanFormat = '<span data-wr-id='
    # readfile
    filereadlines = readfile(filename)
    
    eachcontent = []
    for i in range(0, len(filereadlines)):
        eachLine = ''
        try:
            for j in range(0, len(filereadlines[i])):
                if filereadlines[i][j: ].startswith(spanFormat):
                    k = j
                    while (filereadlines[i][k] != '>'):
                        k = k + 1
                    #print(filereadlines[i][j + k + 1])
                    #print(filereadlines[i][k + 1])
                    if filereadlines[i][k + 1] not in ['', ' ']:
                        eachLine = eachLine + filereadlines[i][k + 1]
                    #print(eachLine)
                #print(eachLine)
            print(eachLine)
            eachcontent.append(eachLine + '\n\n')
        except:
           print('e')
        
        
    # write file
    #print(eachcontent)
    writefile(filename,eachcontent)
    
def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_file(Path(aPath)):
            removeSpan(Path(aPath))
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass