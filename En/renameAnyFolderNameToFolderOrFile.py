# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import os
    
def writefile(filename, filereadlines):
    newfile = open(filename, mode='w', encoding='ANSI')
    newfile.writelines(filereadlines)
    newfile.close()
    
def main(inputPath):
    # get folder name
    # create log and recover file = True, don't create = False
    # 如果不想生成日志和恢复文件，下面这行改成createLogAndRecover = False
    createLogAndRecover = False
    # show window，如果不想显示处理窗口，showCMDwindows = False
    showCMDwindows = True
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            folderName = Path(aPath).name
            renameLastFile = False
            # remove [XX完] or [XX未]
            if folderName.endswith('完]'):
                renameLastFile = True
            if folderName.endswith('完]') or folderName.endswith('未]'):
                loc = folderName.rfind('[')
                folderName = folderName[:loc]
                
            # if folder and file mix, exit
            inFile = False
            inFolder = False
            for file in Path(aPath).glob('*'):
                if Path.is_file(file):
                    inFile = True
                if Path.is_dir(file):
                    inFolder = True
            if inFile and inFolder:
                print("Sorry, Not support folders and files in same folder.")
                print("抱歉，暂时不支持文件和文件夹的在同一个文件夹。")
                os.system("pause")
                sys.exit()
                
            # rename all file
            cmdLog = []
            recoverLog = []
            fileCount = 0
            lastFileName = ''
            lastFileOldName = ''
            for file in Path(aPath).glob('*'):
                newFileName = folderName + 'Vol_' + str(fileCount + 1).zfill(2)
                # get file suffix
                if Path.is_file(file):
                    newFileName = newFileName + file.suffix
                # to do
                imputCmd = 'rename "' + str(Path(aPath).joinpath(file)) + '" "' + newFileName + '"'
                # .bat
                recoverCmd = 'rename "' + str(Path(aPath).joinpath(newFileName)) + '" "' + file.name + '"'
                cmdLog.append(imputCmd + '\n')
                recoverLog.append(recoverCmd + '\n')
                # output
                print(file.name + '  ->  ' + newFileName)
                os.system(imputCmd)
                fileCount = fileCount + 1
                lastFileName = newFileName
                lastFileOldName = file.name
                
            # rename last file.
            if renameLastFile:
                if Path.is_dir(Path(aPath).joinpath(lastFileName)):
                    imputCmd = 'rename "' + str(Path(aPath).joinpath(lastFileName)) + '" "' + lastFileName + ' End'
                    recoverCmd = 'rename "' + str(Path(aPath).joinpath(lastFileName + ' End')) + '" "' + lastFileOldName + '"'
                    print(lastFileName + '  ->  ' + lastFileName + ' End')
                if Path.is_file(Path(aPath).joinpath(lastFileName)):
                    imputCmd = 'rename "' + str(Path(aPath).joinpath(lastFileName)) + '" "' + lastFileName[0:-4] + ' End' + lastFileName[-4:] + '"'
                    recoverCmd = 'rename "' + str(Path(aPath).joinpath(lastFileName[0:-4] + ' End' + newFileName[-4:])) + '" "' + lastFileOldName + '"'
                    print(lastFileName + '  ->  ' + lastFileName[0:-4] + ' End' + lastFileName[-4:])
                cmdLog.append(imputCmd)
                recoverLog.append(recoverCmd)
                os.system(imputCmd)
            
            if createLogAndRecover:
                writefile('Log ' + folderName + '.txt', cmdLog)
                writefile('Recover ' + folderName + '.bat', recoverLog)
    if showCMDwindows:
        os.system("pause")
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass