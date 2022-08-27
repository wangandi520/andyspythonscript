# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys

def doAddMessageToImage(filePath):
    # typeof(filePath): Path
    # 设置文件类型
    fileType = ['.png','.jpg']
    # 需要添加的信息
    myMessage = '需要添加的信息'
    encodeMessage:bytes = myMessage.encode('utf-8')
    if filePath.suffix.lower() in fileType:
        with open(filePath, 'rb') as fileRead:
            fileReadLine = fileRead.readlines()
    if filePath.suffix.lower() == '.jpg':
        if fileReadLine[-1][-2:] == b'\xff\xd9':
            fileReadLine.append(b'\n')
            fileReadLine.append(encodeMessage)
            with open(filePath.parent.joinpath(filePath.stem + '_new' + filePath.suffix), 'wb') as fileSave:
                fileSave.writelines(fileReadLine)
        else:
            decodeMessage = fileReadLine[-1].decode('utf-8')
            print(decodeMessage)
    if filePath.suffix.lower() == '.png':
        if fileReadLine[-1][-1:] == b'\x82':
            fileReadLine.append(b'\n')
            fileReadLine.append(encodeMessage)
            with open(filePath.parent.joinpath(filePath.stem + '_new' + filePath.suffix), 'wb') as fileSave:
                fileSave.writelines(fileReadLine)
        else:
            decodeMessage = fileReadLine[-1].decode('utf-8')
            print(decodeMessage)

def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                doAddMessageToImage(file)
                
        if Path.is_file(Path(aPath)):
            doAddMessageToImage(Path(aPath))

    input('按回车键退出')

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass