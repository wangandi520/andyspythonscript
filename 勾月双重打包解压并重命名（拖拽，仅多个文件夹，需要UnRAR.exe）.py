# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# 需要UnRAR.exe 或 pip3 install unrar

from pathlib import Path
import sys
import os
import rarfile

def rename(aPath):
    # get folder name
    if Path.is_dir(Path(aPath)):
        # first boox start index，第一本书的序号
        startIndex = 1
        folderName = Path(aPath).name
        renameLastFile = False
        # remove [XX完] or [XX未]
        if folderName.endswith('完]'):
            renameLastFile = True
        if folderName.endswith('完]') or folderName.endswith('未]'):
            loc = folderName.rfind('[')
            folderName = folderName[:loc]
            
        # rename all file
        lastFileName = ''
        lastFileOldName = ''
        for file in Path(aPath).glob('*'):
            newFileName = folderName + 'Vol_' + str(startIndex).zfill(2)
            # get file suffix
            if Path.is_file(file):
                newFileName = newFileName + file.suffix
            # to do
            imputCmd = 'rename "' + str(Path(aPath).joinpath(file)) + '" "' + newFileName + '"'
            # .bat
            recoverCmd = 'rename "' + str(Path(aPath).joinpath(newFileName)) + '" "' + file.name + '"'
            # output
            print(file.name + '  ->  ' + newFileName)
            os.system(imputCmd)
            startIndex = startIndex + 1
            lastFileName = newFileName
            lastFileOldName = file.name
            
        # rename last file.
        if renameLastFile:
            if Path.is_dir(Path(aPath).joinpath(lastFileName)):
                imputCmd = 'rename "' + str(Path(aPath).joinpath(lastFileName)) + '" "' + lastFileName + ' End'
                print(lastFileName + '  ->  ' + lastFileName + ' End')
            if Path.is_file(Path(aPath).joinpath(lastFileName)):
                imputCmd = 'rename "' + str(Path(aPath).joinpath(lastFileName)) + '" "' + lastFileName[0:-4] + ' End' + lastFileName[-4:] + '"'
                print(lastFileName + '  ->  ' + lastFileName[0:-4] + ' End' + lastFileName[-4:])
            os.system(imputCmd)
                
def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        tmpPath = ''
        doRARName = ''
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('*.part1.rar'):
                doRARName = file 
                tmpPath = Path(aPath).joinpath(doRARName)
            print('UnRAR: ' + str(tmpPath))
            rar = rarfile.RarFile(tmpPath)
            print(aPath)
            rar.extractall(Path(aPath), pwd = '1234')
            rar.close()
            for file in Path(aPath).glob('*.part1.rar'):
                if file.name != doRARName:
                    doRARName = file.name 
                    tmpPath = Path(aPath).joinpath(doRARName)
            print('UnRAR: ' + str(tmpPath))
            rar = rarfile.RarFile(tmpPath)
            rar.extractall(Path(aPath), pwd = '1234')
            rar.close()
            fileList = rar.namelist()
            print('Done: ')
            for file in fileList:
                print(file)
            newFolderName = Path(aPath).name
            print('mkdir ' + str(Path(aPath).joinpath(newFolderName)))
            os.system('mkdir ' + str(Path(aPath).joinpath(newFolderName)))
            for file in fileList:
                os.system('move ' + str(Path(aPath).joinpath(file)) + ' ' + str(Path(aPath).joinpath(newFolderName)))
            rename(Path(aPath).joinpath(Path(newFolderName)))
            #os.system('pause')

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass