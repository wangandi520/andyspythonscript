# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
from PIL import Image
from pyzbar import pyzbar
import matplotlib.pyplot as plt
import sys
import os
import zipfile

def myPrint(string, padding = 80):
    padding = ' ' * (padding - len(string)) if padding else ''
    print(string + padding, end = '\r')
    
def doKindleunpack(allFilePath):
    # KindleUnpack下载地址https://github.com/kevinhendricks/KindleUnpack
    # 填写kindleunpack.py的地址，注意使用\\代替\
    myCMD = 'D:\\KindleUnpack-083\\lib\\kindleunpack.py'
    for eachFilePath in allFilePath:
        if eachFilePath.suffix == '.azw3':
            print('正在处理azw3：' + eachFilePath.name)
            cmd = myCMD + ' "' + str(eachFilePath) + '"'
            os.system(cmd)
        
def unzipEachFile(allFilePath):
    for eachFilePath in allFilePath:
        # 创建ZipFile对象并打开zip文件
        if eachFilePath.suffix == '.epub':
            print('正在处理epub：' + eachFilePath.name)
            try:
                with zipfile.ZipFile(eachFilePath, 'r') as myzipfile:
                    # 获取所有文件列表
                    newZipFilePath = eachFilePath.parent.joinpath(eachFilePath.stem)
                    # 新建文件夹
                    if not newZipFilePath.exists():
                        Path.mkdir(newZipFilePath)
                    # 将文件从zip文件中提取到指定目录
                    print(f'开始解压 {eachFilePath.name} 到 {newZipFilePath}')
                    myzipfile.extractall(newZipFilePath)
                    print(f'完成解压 {eachFilePath.name}')
            except zipfile.BadZipFile:
                print(f'错误: {eachFilePath.name} 不是有效的zip/epub文件')
            except Exception as e:
                print(f'处理 {eachFilePath.name} 时出错: {str(e)}')
            
def doChangeSuffix(filePath):
    # type(filePath): Path
    newFileName = Path(filePath).parent.joinpath(Path(filePath).stem + '.epub')
    if not newFileName.exists():
        Path(filePath).rename(newFileName)
        print(Path(filePath).name + '  ->  ' + Path(filePath).stem + '.zip')
        
def searchKeywordInFile(filePath, keyword):
    # 读取文件
    # 如果搜索的关键词前后10个字含有这些关键词，就不输出
    # excludeKeyword = ['关键词01', '关键词02']
    excludeKeyword = ['译文', '译林', 'shanghaiwenyi', 'yilinpr', '企鹅图书', 'stphbooks', 'shijiwenjing2002','果麦文化']
    with open(filePath, mode='r', encoding='UTF-8') as file:
        filereadlines = file.readlines()
    myPrint('正在扫描' + filePath.name)
    for i in range(len(filereadlines)):
        filereadlines[i] = filereadlines[i].rstrip()
        for eachKeyword in keyword:
            getKeywordLocation = filereadlines[i].lower().find(eachKeyword)
            if getKeywordLocation > -1:
                toShow = True
                for eachExcludeKeyword in excludeKeyword:
                    if eachExcludeKeyword in filereadlines[i][getKeywordLocation - 10:getKeywordLocation + 10].lower():
                        toShow = False
                if toShow:
                    print(filereadlines[i][getKeywordLocation - 10:getKeywordLocation + 10] + '    ' + str(i + 1) + '    ' + str(filePath.name) + '    ' + str(filePath))

def searchQRCodeInFile(filePath):
    # 读取文件
    with open(filePath, mode='rb') as file:
        image = Image.open(file)
        myPrint('正在扫描' + filePath.name)
        for barcode in pyzbar.decode(image,symbols=[pyzbar.ZBarSymbol.QRCODE]):   
            barcodeData = barcode.data.decode("utf-8")
            print(barcodeData + '    ' + str(filePath))
            # 是否显示含二维码的图片
            if True:
                plt.figure(str(filePath))
                plt.title(str(filePath.name), fontproperties='SimHei')
                plt.imshow(image)
                plt.show()
        
            
def main(inputPath):
    del inputPath[0]
    allFilePath = []
    # unzip解压缩epub文件，kindleunpack解压azw3文件
    # 搜索是否含有关键词和二维码图片
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if file.suffix in ['.epub', '.azw3']:
                    allFilePath.append(file) 
        if Path.is_file(Path(aPath)):
            if file.suffix in ['.epub', '.azw3']:
                allFilePath.append(Path(aPath))
    unzipEachFile(allFilePath)
    doKindleunpack(allFilePath)    
    
    # 要搜索关键词的文件的扩展名
    mySuffix01 = ['.html', '.xhtml', '.opf', '.txt']
    # 要搜索的关键词
    myKeywords = ['coay.com', '微信', '公众号', 'epubw', '三秋君', '窃蓝书房', 'tianlangbooks', '七彩友书', 'sobooks', 'cj5', 'chenjin5', 'elib.', '红心读书','booker527']
    print('\n搜索关键词：' + '，'.join(myKeywords))
    print('内容 行数 文件名 文件路径')
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if file.suffix.lower() in mySuffix01:
                    searchKeywordInFile(file, myKeywords)      
    print('\n搜索关键词完成\n')
    
    # 要搜索二维码的文件的扩展名
    mySuffix02 = ['.jpeg', '.jpg', '.png', '.gif']
    print('二维码扫描结果 文件路径')
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if file.suffix in mySuffix02:
                    searchQRCodeInFile(file)      
    print('\n搜索二维码完成\n')
    os.system('pause')
   
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass