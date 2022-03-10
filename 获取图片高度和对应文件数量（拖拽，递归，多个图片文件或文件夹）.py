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
    showAllLocation = False
    # 文件格式
    fileType = ['.jpg', '.png']
    
    fileHeight = {}
    
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if Path.is_file(file) and (file.suffix in fileType):
                    tmpImg = Image.open(file)
                    if (tmpImg.size[1] not in fileHeight):
                        if (showEachFile and showAllLocation):
                            print(str(Path(file)) + ' ' + str(tmpImg.size[1]))
                        if (showEachFile and not showAllLocation):
                            print(str(Path(file.name)) + ' ' + str(tmpImg.size[1]))
                        fileHeight[tmpImg.size[1]] = 1
                    elif (tmpImg.size[1] in fileHeight):
                        if (showEachFile and showAllLocation):
                            print(str(Path(file)) + ' ' + str(tmpImg.size[1]))
                        if (showEachFile and not showAllLocation):
                            print(str(Path(file.name)) + ' ' + str(tmpImg.size[1]))
                        fileHeight[tmpImg.size[1]] = fileHeight[tmpImg.size[1]] + 1
                
        if Path.is_file(Path(aPath)) and (Path(aPath).suffix in fileType):
            tmpImg = Image.open(aPath)
            if (tmpImg.size[1] not in fileHeight):
                if (showEachFile and showAllLocation):
                    print(str(Path(aPath)) + ' ' + str(tmpImg.size[1]))
                if (showEachFile and not showAllLocation):
                    print(str(Path(aPath).name) + ' ' + str(tmpImg.size[1]))
                fileHeight[tmpImg.size[1]] = 1
            elif (tmpImg.size[1] in fileHeight):
                if (showEachFile and showAllLocation):
                    print(str(Path(aPath)) + ' ' + str(tmpImg.size[1]))
                if (showEachFile and not showAllLocation):
                    print(str(Path(aPath).name) + ' ' + str(tmpImg.size[1]))
                fileHeight[tmpImg.size[1]] = fileHeight[tmpImg.size[1]] + 1
    
    print()
    for key in fileHeight:
        print('图片高度: ' + str(key) + ', 文件数量: ' + str(fileHeight[key]))
        
    print()
    input('按回车退出')
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass
