# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
from PIL import Image
from pyzbar import pyzbar
import matplotlib.pyplot as plt
import sys
import os

def myPrint(string, padding = 80):
    padding = ' ' * (padding - len(string)) if padding else ''
    print(string + padding, end = '\r')

def searchQRCodeInFile(filePath):
    # 读取文件
    with open(filePath, mode='rb') as file:
        image = Image.open(file)
        myPrint('正在扫描' + filePath.name)
        for barcode in pyzbar.decode(image,symbols=[pyzbar.ZBarSymbol.QRCODE]):   
            barcodeData = barcode.data.decode("utf-8")
            print(barcodeData + '    ' + str(filePath))
            # 是否显示含二维码的图片
            if False:
                plt.figure(str(filePath))
                plt.title(str(filePath.name), fontproperties='SimHei')
                plt.imshow(image)
                plt.show()
    
def main(inputPath):
    del inputPath[0]
    # 要搜索的文件的扩展名
    mySuffix = ['.jpeg', '.jpg', '.png']
    print('二维码扫描结果 文件路径')
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if file.suffix in mySuffix:
                    searchQRCodeInFile(file)      
    print('\n搜索完成\n')
    os.system('pause')
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            print('共拖拽' + str(len(sys.argv) - 1) + '个文件（夹），未包含子文件（夹）')
            main(sys.argv)
    except IndexError:
        pass