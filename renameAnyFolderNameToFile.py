# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import os
    
def writefile(filereadlines):
    newfile = open('renameAnyFolderNameToFile.txt', mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()
    
def main(inputPath):
    # get folder name
    if Path.is_dir(Path(inputPath)):
        folderName = Path(inputPath).name
        renameLastFile = False
        if folderName.endswith('完]'):
            renameLastFile = True
        if folderName.endswith('完]') or folderName.endswith('未]'):
            loc = folderName.rfind('[')
            folderName = folderName[:loc]
            
        # rename file
        cmdLog = []
        cmdLog.append('Log:\n')
        recoverLog = []
        recoverLog.append('Recover:\n')
        fileCount = 0
        lastFileName = ''
        lastFileOldName = ''
        for file in Path(inputPath).glob('**/*'):
            newFileName = folderName + 'Vol_' + str(fileCount + 1).zfill(2) + file.suffix
            imputCmd = 'rename "' + str(Path(inputPath).joinpath(file)) + '" "' + newFileName + '"'
            recoverCmd = 'rename "' + str(Path(inputPath).joinpath(newFileName)) + '" "' + file.name + '"'
            cmdLog.append(imputCmd + '\n')
            recoverLog.append(recoverCmd + '\n')
            print(file.name + '  ->  ' + newFileName)
            os.system(imputCmd)
            fileCount = fileCount + 1
            lastFileName = newFileName
            lastFileOldName = file.name
        
        # rename last file.
        if renameLastFile:
            imputCmd = 'rename "' + str(Path(inputPath).joinpath(lastFileName)) + '" "' + lastFileName[0:-4] + ' End' + newFileName[-4:] + '"'
            recoverCmd = 'rename "' + str(Path(inputPath).joinpath(lastFileName[0:-4] + ' End' + newFileName[-4:])) + '" "' + lastFileOldName + '"'
            cmdLog.append(imputCmd)
            recoverLog.append(recoverCmd)
            print(lastFileName + '  ->  ' + lastFileName[0:-4] + ' End' + newFileName[-4:])
            os.system(imputCmd)
        cmdLog.append('\n\n')
        output = cmdLog + recoverLog
        writefile(cmdLog + recoverLog)
        os.system("pause")
        
if __name__ == '__main__':
    try:
        if len(sys.argv) == 1:
            main('.')
        elif len(sys.argv) == 2:
            main(sys.argv[1])
    except IndexError:
        pass