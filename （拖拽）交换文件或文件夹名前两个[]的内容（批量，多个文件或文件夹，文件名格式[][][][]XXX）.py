# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
    
def main(inputPath):
    del inputPath[0]
    for file in inputPath:
        folderName = Path(file).name
        leftSymbol = []
        rightSymbol = []
        for index in range(len(folderName)):
            if folderName[index] == '[':
                leftSymbol.append(index)
            if folderName[index] == ']':
                rightSymbol.append(index)
        newFileName = folderName[leftSymbol[1]:rightSymbol[1] + 1] + folderName[leftSymbol[0]:rightSymbol[0] + 1] + folderName[rightSymbol[1] + 1:]
        Path(file).rename(Path(file).parent.joinpath(newFileName))
            
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass