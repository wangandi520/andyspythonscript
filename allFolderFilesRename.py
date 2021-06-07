# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

import os.path
import sys

def main(fileName):
    filePrefix = ''
    if (os.path.basename(fileName) == 'allFolderFilesRename.py'):
        filePrefix = ''
    else:
        filePrefix = os.path.basename(fileName)[0:-3]
    allFiles = os.listdir('.')
    allDirs = []
    for file in allFiles:
        if (os.path.isdir(file)):
            allDirs.append(file)
    
    dirCount = 1
    for dir in allDirs:
        tempFilesName = os.listdir(dir)
        fileCount = 1
        for fileName in tempFilesName:
            imputCmd = 'rename "' + dir + '\\' + fileName + '" ' + filePrefix + str(dirCount).zfill(2) + '_' + str(fileCount).zfill(3) + os.path.splitext(fileName)[1]
            print(imputCmd)
            os.system(imputCmd)
            fileCount = fileCount + 1
        dirCount = dirCount + 1
if __name__ == '__main__':
    main(sys.argv[0])