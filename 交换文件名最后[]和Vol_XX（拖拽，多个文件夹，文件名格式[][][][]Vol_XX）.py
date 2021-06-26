# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
    
def main(inputPath):
    del inputPath[0]
    
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('*'):
                folderName = Path(file).name
                leftSymbol = []
                rightSymbol = []
                if not('[' in folderName and ']' in folderName):
                    continue
                for index in range(len(folderName)):
                    if folderName[index] == '[':
                        leftSymbol.append(index)
                    if folderName[index] == ']':
                        rightSymbol.append(index)
                if (folderName[rightSymbol[-1] + 1:-6] == 'Vol_'):
                    newFileName = folderName[0:leftSymbol[-1]] + folderName[rightSymbol[-1] + 1:-4] + folderName[leftSymbol[-1]:rightSymbol[-1] + 1] + folderName[-4:]
                    Path(file).rename(Path(file).parent.joinpath(newFileName))
                if (folderName[-5] == ']'):
                    newFileName = folderName[0:rightSymbol[-2] + 1] + folderName[leftSymbol[-1]:rightSymbol[-1] + 1] + folderName[rightSymbol[-2] + 1:leftSymbol[-1]] + folderName[-4:]
                    Path(file).rename(Path(file).parent.joinpath(newFileName))
                
        if Path.is_file(Path(aPath)):
            folderName = Path(aPath).name
            leftSymbol = []
            rightSymbol = []
            if not('[' in folderName and ']' in folderName):
                continue
            for index in range(len(folderName)):
                if folderName[index] == '[':
                    leftSymbol.append(index)
                if folderName[index] == ']':
                    rightSymbol.append(index)
            if (folderName[rightSymbol[-1] + 1:-6] == 'Vol_'):
                newFileName = folderName[0:leftSymbol[-1]] + folderName[rightSymbol[-1] + 1:-4] + folderName[leftSymbol[-1]:rightSymbol[-1] + 1] + folderName[-4:]
                Path(aPath).rename(Path(aPath).parent.joinpath(newFileName))
            if (folderName[-5] == ']'):
                newFileName = folderName[0:rightSymbol[-2] + 1] + folderName[leftSymbol[-1]:rightSymbol[-1] + 1] + folderName[rightSymbol[-2] + 1:leftSymbol[-1]] + folderName[-4:]
                Path(aPath).rename(Path(aPath).parent.joinpath(newFileName))
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass