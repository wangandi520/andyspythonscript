# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import re
import os
    
def main(inputPath):
    # get folder name
    folderName = Path(inputPath).name
    if folderName.endswith('完]'):
        loc = folderName.rfind('[')
        folderName = folderName[:loc]
        
    # rename file
    fileCount = 0
    lastFileName = ''
    for file in Path(inputPath).glob('**/*'):
        if re.search('Vol_(\d{2}).zip$',file.name[-10:]):
            newFileName = folderName + file.name[-10:]
            imputCmd = 'rename "' + str(Path(inputPath).joinpath(file)) + '" "' + newFileName + '"'
            os.system(imputCmd)
            fileCount = fileCount + 1
            lastFileName = newFileName
    # rename last file
    imputCmd = 'rename "' + str(Path(inputPath).joinpath(lastFileName)) + '" "' + lastFileName[0:-4] + ' End.zip"'
    os.system(imputCmd)
    
if __name__ == '__main__':
    try:
        if len(sys.argv) == 1:
            main('.')
        elif len(sys.argv) == 2:
            main(sys.argv[1])
    except IndexError:
        pass