# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import os
import zipfile
        
def checkFileNameIndex(filePath):
    # 如果image001.jpg后是image003.jpg，则输出可能缺失的文件image002.jpg
    # 如果是zip文件，修改上面函数的设置
    # 设置文件名最后几位是序号，image001是3
    getIndexNumber = 3
    # 第一个文件的序号
    getFirstIndex = 1
    # 文件夹
    allFilePath = []
    getFlag = True
    if Path.is_dir(Path(filePath)):
        for eachFilePath in Path(filePath).glob('*'):
            if Path.is_file(eachFilePath):
                allFilePath.append(eachFilePath)
    if Path.is_file(Path(filePath)) and Path(filePath).suffix == '.zip':
        with zipfile.ZipFile(Path(filePath), 'a') as zf:
            for eachFile in zf.infolist():
                if not eachFile.is_dir():
                    allFilePath.append(Path(eachFile.filename))
    if len(allFilePath) != 0:
        # 推测文件名数字序号位数
        # getGuessIndex = 0
        # for tempIndex in range(-1, -6, -1):
            # if str(allFilePath[0].stem[tempIndex]).isdigit():
                # getGuessIndex = getGuessIndex + 1
            # else:
                # break
        # if getGuessIndex != getIndexNumber:
            # 去掉下一行的#，直接使用程序推测的数字位数
            # getIndexNumber = getGuessIndex
            #print('程序文件名序号位数应是' + str(getGuessIndex) + '，请修改第13行')
        # 符合这几个条件才继续执行脚本：文件夹不包含子文件夹，所有文件名长度相同，扩展名相同
        firstFileLength = len(allFilePath[0].stem)
        firstFileSuffix = allFilePath[0].suffix
        for eachFilePath in allFilePath:
            if len(eachFilePath.stem) != firstFileLength:
                print('错误，文件名长度不一致')
                getFlag = False
                break
            if eachFilePath.suffix != firstFileSuffix:
                print('错误，文件扩展名不一致')
                getFlag = False
                break
            if Path.is_dir(eachFilePath):
                print('错误，文件，文件夹混杂')
                getFlag = False
                break
        if getFlag:
            # 只显示可能缺失的文件名
            firstFileStem = allFilePath[0].name[0 : firstFileLength - getIndexNumber]
            # 这个文件夹的文件名序号
            myFileNameIndex = []
            for eachIndex in allFilePath:
               myFileNameIndex.append(eachIndex.name[firstFileLength - getIndexNumber : firstFileLength])
            # 不缺文件的情况下的文件序号
            allFileNameIndex = []
            for tempIndex in range(getFirstIndex, int(allFilePath[-1].name[firstFileLength - getIndexNumber : firstFileLength]) + 1):
                allFileNameIndex.append(str(tempIndex).zfill(getIndexNumber))
            for tempIndex in allFileNameIndex:
                if tempIndex not in myFileNameIndex:
                    # 输出格式：可能缺失的文件名  上级文件夹名
                    print(firstFileStem + tempIndex + firstFileSuffix + '          ' + str(filePath.name))
                    # 输出格式：可能缺失的文件名  上上级文件夹名
                    #print(firstFileStem + tempIndex + firstFileSuffix + '          ' + str(filePath.parent.name))
                    # 输出格式：可能缺失的文件名
                    #print(firstFileStem + tempIndex + firstFileSuffix)

def main(inputPath):
    del inputPath[0]
    allFilePath = []
    for aPath in inputPath:
        if Path.is_file(Path(aPath)) and Path(aPath).suffix == '.zip':
            allFilePath.append(Path(aPath))
        if Path.is_dir(Path(aPath)):
            allFilePath.append(Path(aPath))
            for eachPath in Path(aPath).glob('**/*'):
                if Path.is_dir(eachPath):
                    allFilePath.append(Path(eachPath))
    for eachFilePath in allFilePath:
        checkFileNameIndex(eachFilePath)
    print('程序结束，如果没有输出说明可能没有缺失的文件。')
    os.system('pause')

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass