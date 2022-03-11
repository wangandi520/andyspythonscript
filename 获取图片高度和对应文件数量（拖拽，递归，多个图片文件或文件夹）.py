# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip install pillow


from PIL import Image  
from pathlib import Path
import sys
    
def main(inputPath):
    
    # 显示每张图片的高度 = True， 不显示 = False
    showEachFile = True
    # 显示完整路径 = True，只显示文件名 = False
    showAllPath = True
    # 文件格式
    fileType = ['.jpg', '.png']
    
    fileHeight = {}
    filePathStorage = []
    
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if Path.is_file(file) and (file.suffix in fileType):
                    tmpImg = Image.open(file)
                    if (tmpImg.size[1] not in fileHeight):
                        if (showEachFile and showAllPath):
                            print(str(Path(file)) + ' ' + str(tmpImg.size[1]))
                            filePathStorage.append([str(Path(file)), str(tmpImg.size[1])])
                        if (showEachFile and not showAllPath):
                            print(str(Path(file.name)) + ' ' + str(tmpImg.size[1]))
                            filePathStorage.append([str(Path(file.name)), str(tmpImg.size[1])])
                        fileHeight[tmpImg.size[1]] = 1
                    elif (tmpImg.size[1] in fileHeight):
                        if (showEachFile and showAllPath):
                            print(str(Path(file)) + ' ' + str(tmpImg.size[1]))
                            filePathStorage.append([str(Path(file)), str(tmpImg.size[1])])
                        if (showEachFile and not showAllPath):
                            print(str(Path(file.name)) + ' ' + str(tmpImg.size[1]))
                            filePathStorage.append([str(Path(file.name)), str(tmpImg.size[1])])
                        fileHeight[tmpImg.size[1]] = fileHeight[tmpImg.size[1]] + 1
        if Path.is_file(Path(aPath)) and (Path(aPath).suffix in fileType):
            tmpImg = Image.open(aPath)
            if (tmpImg.size[1] not in fileHeight):
                if (showEachFile and showAllPath):
                    print(str(Path(aPath)) + ' ' + str(tmpImg.size[1]))
                    filePathStorage.append([str(Path(aPath)), str(tmpImg.size[1])])
                if (showEachFile and not showAllPath):
                    print(str(Path(aPath).name) + ' ' + str(tmpImg.size[1]))
                    filePathStorage.append([str(Path(aPath).name), str(tmpImg.size[1])])
                fileHeight[tmpImg.size[1]] = 1
            elif (tmpImg.size[1] in fileHeight):
                if (showEachFile and showAllPath):
                    print(str(Path(aPath)) + ' ' + str(tmpImg.size[1]))
                    filePathStorage.append([str(Path(aPath)), str(tmpImg.size[1])])
                if (showEachFile and not showAllPath):
                    print(str(Path(aPath).name) + ' ' + str(tmpImg.size[1]))
                    filePathStorage.append([str(Path(aPath).name), str(tmpImg.size[1])])
                fileHeight[tmpImg.size[1]] = fileHeight[tmpImg.size[1]] + 1
      
    print()
    makeChoice = {}
    count = 1
    for key in fileHeight:
        makeChoice[str(count)] = str(key)
        count = count + 1
        print('图片高度: ' + str(key) + ', 文件数量: ' + str(fileHeight[key]))
             
    print()
    print('输入数字查看对应高度的全部文件：')
    
    for key in makeChoice:
        print(key + ': ' + makeChoice[key])

    # for tmpfilePath, tmpHeight in filePathStorage:
        # print(tmpfilePath + ' ' + tmpHeight)
    print()
    getInput = input('输入回车退出: ')
    print()
    while (getInput != ''):
        print('高度' + makeChoice[getInput] + '：')
        for eachFile in filePathStorage:
            # print(eachFile[1])
            # print(makeChoice[getInput])
            # print(getInput)
            if eachFile[1] == makeChoice[getInput]:
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
