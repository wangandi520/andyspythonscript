# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import os
import re
    
def main(inputPath):
    del inputPath[0]
    for folder in inputPath:
        folderName = Path(folder).name
        nameParts = re.findall("(\\[[^\\]]*\\])", folderName)
        lastSymbol = folderName.rfind(']') + 1
        fileSuffix = folderName[lastSymbol:]
        nameParts[1], nameParts[0] = nameParts[0], nameParts[1]
        newFileName = ''
        for part in nameParts:
            newFileName = newFileName + part
        newFileName = newFileName + fileSuffix
        imputCmd = 'rename "' + folder + '" "' + newFileName + '"'
        os.system(imputCmd)
            
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass