# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip install pillow


from PIL import Image  
from pathlib import Path
import sys
    
def main(inputPath):
    
    # 显示每张图片的宽度 = True， 不显示 = False
    showEachFile = True
    # 显示完整路径 = True，只显示文件名 = False
    showAllPath = False
    # 文件格式
    fileType = ['.jpg', '.png']
    
    fileWidth = {}
    filePathStorage = []
    
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if Path.is_file(file) and (file.suffix in fileType):
                    tmpImg = Image.open(file)
                    if (tmpImg.size[0] not in fileWidth):
                        if (showEachFile and showAllPath):
                            print(str(Path(file)) + ' ' + str(tmpImg.size[0]))
                            filePathStorage.append([str(Path(file)), str(tmpImg.size[0])])
                        if (showEachFile and not showAllPath):
                            print(str(Path(file.name)) + ' ' + str(tmpImg.size[0]))
                            filePathStorage.append([str(Path(file.name)), str(tmpImg.size[0])])
                        fileWidth[tmpImg.size[0]] = 1
                    elif (tmpImg.size[0] in fileWidth):
                        if (showEachFile and showAllPath):
                            print(str(Path(file)) + ' ' + str(tmpImg.size[0]))
                            filePathStorage.append([str(Path(file)), str(tmpImg.size[0])])
                        if (showEachFile and not showAllPath):
                            print(str(Path(file.name)) + ' ' + str(tmpImg.size[0]))
                            filePathStorage.append([str(Path(file.name)), str(tmpImg.size[0])])
                        fileWidth[tmpImg.size[0]] = fileWidth[tmpImg.size[0]] + 1
        if Path.is_file(Path(aPath)) and (Path(aPath).suffix in fileType):
            tmpImg = Image.open(aPath)
            if (tmpImg.size[0] not in fileWidth):
                if (showEachFile and showAllPath):
                    print(str(Path(aPath)) + ' ' + str(tmpImg.size[0]))
                    filePathStorage.append([str(Path(aPath)), str(tmpImg.size[0])])
                if (showEachFile and not showAllPath):
                    print(str(Path(aPath).name) + ' ' + str(tmpImg.size[0]))
                    filePathStorage.append([str(Path(aPath).name), str(tmpImg.size[0])])
                fileWidth[tmpImg.size[0]] = 1
            elif (tmpImg.size[0] in fileWidth):
                if (showEachFile and showAllPath):
                    print(str(Path(aPath)) + ' ' + str(tmpImg.size[0]))
                    filePathStorage.append([str(Path(aPath)), str(tmpImg.size[0])])
                if (showEachFile and not showAllPath):
                    print(str(Path(aPath).name) + ' ' + str(tmpImg.size[0]))
                    filePathStorage.append([str(Path(aPath).name), str(tmpImg.size[0])])
                fileWidth[tmpImg.size[0]] = fileWidth[tmpImg.size[0]] + 1
      
    print()
    for key in fileWidth:
        print('图片宽度: ' + str(key) + ', 文件数量: ' + str(fileWidth[key]))       
    print()
    print('输入数字查看对应宽度的全部文件：')
    for index, key in enumerate(fileWidth, start=1):
        print(str(index) + '：' + str(key))
    print()
    getInput = input('输入回车退出: ')
    print()
    
    while (getInput != ''): 
        if int(getInput) <= len(fileWidth):
            getInput = int(getInput) - 1
            tmpHeight = list(fileWidth.keys())[getInput]
            print('宽度' + str(tmpHeight) + '：')
            for eachFile in filePathStorage:
                if eachFile[1] == str(tmpHeight):
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
