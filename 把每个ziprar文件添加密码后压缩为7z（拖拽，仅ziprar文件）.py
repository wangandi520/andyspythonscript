# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip install py7zr

from pathlib import Path
import py7zr
import sys

def doAddToEncrypted7z(filePath):
    # typeof(filePath): Path
    # 设置文件类型
    fileType = ['.zip','.rar']
    # 设置密码为1234
    myPassword = '1234'
    # 新文件名 = 密码1234_ + 旧文件名
    if filePath.suffix.lower() in fileType:
        newFileName = '密码' + myPassword + '_' + Path(filePath).stem
        print('正在处理...' + filePath.name)
        with py7zr.SevenZipFile(str(Path(filePath).parent.joinpath(newFileName)) + '.7z', 'w', password = myPassword) as archive:
            archive.write(filePath)
        print('完成')

def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                doAddToEncrypted7z(file)
                
        if Path.is_file(Path(aPath)):
            doAddToEncrypted7z(Path(aPath))

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass