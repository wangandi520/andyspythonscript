# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
    
def main(inputPath):
    
    # 显示完整路径 = True，只显示文件名 = False
    showAllPath = False
    
    fileSuffix = {}
    filePathStorage = []
    
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if Path.is_file(file):
                    if (file.suffix not in fileSuffix):
                        if (showAllPath):
                            #print(str(Path(file)))
                            filePathStorage.append([str(Path(file)), str(Path(file).suffix)])
                        if (not showAllPath):
                            #print(str(Path(file.name)))
                            filePathStorage.append([str(Path(file.name)), str(Path(file).suffix)])
                        fileSuffix[file.suffix] = 1
                    elif (file.suffix in fileSuffix):
                        if (showAllPath):
                            #print(str(Path(file)))
                            filePathStorage.append([str(Path(file)), str(Path(file).suffix)])
                        if (not showAllPath):
                            #print(str(Path(file.name)))
                            filePathStorage.append([str(Path(file.name)), str(Path(file).suffix)])
                        fileSuffix[file.suffix] = fileSuffix[file.suffix] + 1
        if Path.is_file(Path(aPath)):
            if (Path(aPath).suffix not in fileSuffix):
                if (showAllPath):
                    #print(str(Path(aPath)))
                    filePathStorage.append([str(Path(aPath)), str(Path(aPath).suffix)])
                if (not showAllPath):
                    #print(str(Path(aPath).name))
                    filePathStorage.append([str(Path(aPath).name), str(Path(aPath).suffix)])
                fileSuffix[file.suffix] = 1
            elif (Path(aPath).suffix in fileSuffix):
                if (showAllPath):
                    #print(str(Path(aPath)))
                    filePathStorage.append([str(Path(aPath)), str(Path(aPath).suffix)])
                if (not showAllPath):
                    #print(str(Path(aPath).name))
                    filePathStorage.append([str(Path(aPath).name), str(Path(aPath).suffix)])
                fileSuffix[file.suffix] = fileSuffix[file.suffix] + 1
      
    print()
    for key in fileSuffix:
        print('文件扩展名: ' + str(key)[1:] + ', 文件数量: ' + str(fileSuffix[key]))       
    print()
    print('输入数字查看对应扩展名的全部文件：')
    for index, key in enumerate(fileSuffix, start=1):
        print(str(index) + '：' + str(key)[1:])
    print()
    getInput = input('输入回车退出: ')
    print()
    
    while (getInput != ''): 
        if int(getInput) <= len(fileSuffix):
            getInput = int(getInput) - 1
            tmpSuffix = list(fileSuffix.keys())[getInput]
            print('扩展名' + str(tmpSuffix) + '：')
            for eachFile in filePathStorage:
                if eachFile[1] == str(tmpSuffix):
                    print(eachFile[0])
            print()
            getInput = input('输入回车退出: ')
            print()
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass
