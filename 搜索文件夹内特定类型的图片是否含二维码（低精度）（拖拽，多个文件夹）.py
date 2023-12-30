# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
from PIL import Image
from pyzbar import pyzbar
import sys
import os

def searchQRCodeInFile(filePath):
    # 读取文件
    with open(filePath, mode='rb') as file:
        image = Image.open(file)
        print('正在扫描' + filePath.name, end = '\r')
        for barcode in pyzbar.decode(image,symbols=[pyzbar.ZBarSymbol.QRCODE]):   
            barcodeData = barcode.data.decode("utf-8")
            print(barcodeData + '    ' + str(filePath))
    
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
            main(sys.argv)
    except IndexError:
        pass