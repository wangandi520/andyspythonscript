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
    # 生成日志文件 = True, 不生成 = False
    createLogAndRecover = True
    # 显示窗口 = True, 不显示 = False
    showCMDwindows = True
    # 文件名数字从几开始
    startIndex = 1
    # 文件名数字位数
    digitLength = 3
    for aPath in inputPath[1:]:
        if Path.is_file(Path(aPath)):
            print("请拖拽文件夹，终止程序。")
            os.system("pause")
            sys.exit()
        if Path.is_dir(Path(aPath)):
            # 如果文件夹内还有文件夹就终止程序
            inFile = False
            inFolder = False
            for file in Path(aPath).glob('*'):
                if Path.is_file(file):
                    inFile = True
                if Path.is_dir(file):
                    inFolder = True
            if inFile and inFolder:
                print("不支持文件和文件夹的在同一个文件夹，终止程序。")
                os.system("pause")
                sys.exit()
                
            # 如果文件夹内的文件名长度不一致就终止程序
            fileNameLength = {}
            for file in Path(aPath).glob('*'):
                if len(file.stem) not in fileNameLength:
                    fileNameLength[len(file.stem)] = 1
                else:
                    fileNameLength[len(file.stem)] = fileNameLength[len(file.stem)] + 1
            if len(fileNameLength) > 1:
                print("文件名长度不一致，终止程序。")
                os.system("pause")
                sys.exit()
                
            # 处理
            cmdLog = []
            recoverLog = []
            for file in Path(aPath).glob('*'):
                newFileName = str(startIndex).zfill(digitLength)
                if Path.is_file(file):
                    newFileName = newFileName + file.suffix
                # 命令
                imputCmd = 'rename "' + str(Path(aPath).joinpath(file)) + '" "' + newFileName + '"'
                # 恢复文件
                recoverCmd = 'rename "' + str(Path(aPath).joinpath(newFileName)) + '" "' + file.name + '"'
                cmdLog.append(imputCmd + '\n')
                recoverLog.append(recoverCmd + '\n')
                # 输出
                print(file.name + '  ->  ' + newFileName)
                os.system(imputCmd)
                startIndex = startIndex + 1

            if createLogAndRecover:
                writefile('Log.txt', cmdLog)
                writefile('Recover.bat', recoverLog)
                
    if showCMDwindows:
        print("处理完成。")
        os.system("pause")
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass