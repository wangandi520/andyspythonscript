# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

# https://stackoverflow.com/questions/48873754/how-to-read-photoshop-act-files-with-python/48873783#48873783

import sys
from pathlib import Path
from codecs import encode

def writeToFile(filename, filereadlines):
    newfile = open(filename + '.txt', mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()
    
def main(inputPath):

    #是否输出到文件
    outputToFile = True
    
    allFileInfo = []
    
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('*.act'):
                print('文件名： ' + str(file.name))
                allFileInfo.append('文件名： ' + str(file.name) + '\n')
                with open(file, 'rb') as actFile:
                    rawData = actFile.read()
                hexData = encode(rawData, 'hex')
                totalColorsCount = (int(hexData[-7:-4], 16))
                misterious_count = (int(hexData[-4:-3], 16))
                allColors = [hexData[i:i+6].decode() for i in range(0, totalColorsCount*6, 6)]
                allColors = ['#'+i for i in allColors if len(i)]
                print('颜色表： ' + str(allColors))
                print('数量： ' + str(totalColorsCount))
                print()
                allFileInfo.append('颜色表： ' + str(allColors) + '\n')
                allFileInfo.append('数量： ' + str(totalColorsCount) + '\n\n')
            
        if Path.is_file(Path(aPath)) and Path(aPath).suffix == '.act':
            print('文件名： ' + str(Path(aPath).name))
            allFileInfo.append('文件名： ' + str(Path(aPath).name) + '\n')
            with open(Path(aPath), 'rb') as actFile:
                rawData = actFile.read()
            hexData = encode(rawData, 'hex')
            totalColorsCount = (int(hexData[-7:-4], 16))
            misterious_count = (int(hexData[-4:-3], 16))
            allColors = [hexData[i:i+6].decode() for i in range(0, totalColorsCount*6, 6)]
            allColors = ['#'+i for i in allColors if len(i)]
            print('颜色表： ' + str(allColors))
            print('数量： ' + str(totalColorsCount))
            print()
            allFileInfo.append('颜色表： ' + str(allColors) + '\n')
            allFileInfo.append('数量： ' + str(totalColorsCount) + '\n\n')
    if outputToFile:
        writeToFile(allFileInfo[0][4:-1], allFileInfo)
    input('按回车键退出')
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass