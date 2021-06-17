# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import os
    
def main(inputPath):
    # get folder name
    del inputPath[0]
    for folder in inputPath:
        folderName = Path(folder).name
        if (Path.is_dir(Path(folder))):
            nameSplit = folderName.split('][')
            i = 2
            newFileName = '[' + nameSplit[1] + ']' + nameSplit[0] + ']'
            for i in range(2, len(nameSplit)):
                if not nameSplit[i].endswith(']'):
                    newFileName = newFileName + '[' + nameSplit[i] + ']'
                if nameSplit[i].endswith(']'):
                    newFileName = newFileName + '[' + nameSplit[i]
    
            imputCmd = 'rename "' + folder + '" "' + newFileName + '"'
            os.system(imputCmd)
    
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass