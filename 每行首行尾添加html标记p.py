# encoding:utf-8
# Programmed by Andy

from pathlib import Path
import sys
import time

def readfile(filename):
    # readfile
    with open(filename, mode='r', encoding='UTF-8') as file:
        filereadlines = file.readlines()
    return filereadlines

def writefile(filename,filereadlines):
    # write file
    newfile = open('new ' + Path(filename).stem + '.txt', mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()
    
def convertHTML(filename):
    # readfile
    filereadlines = readfile(filename)
    # bookname,author style
    eachcontent = []
    for eachLine in filereadlines:
        eachLine2 = eachLine.strip().replace('\n', '').replace('\t', '').replace('\r', '').strip()
        eachLine3 = '<p>' + eachLine2 + '</p>\n'
        if eachLine3 == '<p></p>\n':
            eachLine3 = '\n'
        eachcontent.append(eachLine3)
    
    # write file
    writefile(filename,eachcontent)
    
def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('*.txt'):
                convertHTML(file)
        if Path.is_file(Path(aPath)):
            if (Path(aPath).suffix == '.txt'):
                convertHTML(aPath)
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass