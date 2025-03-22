# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip install py7zr rarfile

import sys
import zipfile
import py7zr
import rarfile
import os
from pathlib import Path

def ifZipEncrypted(filePath):
    # 只显示加密的压缩文件名
    try:
        suffix = Path(filePath).suffix.lower()
        if suffix == '.zip':
            with zipfile.ZipFile(filePath) as zip_file:
                for zip_info in zip_file.infolist():
                    if zip_info.flag_bits & 0x1:
                        print(Path(filePath).name)
                        return
        elif suffix == '.7z':
            with py7zr.SevenZipFile(filePath, mode='r') as z:
                if z.needs_password():
                    print(Path(filePath).name)
        elif suffix == '.rar':
            with rarfile.RarFile(filePath) as rar_file:
                if rar_file.needs_password():
                    print(Path(filePath).name)
    except Exception as e:
        pass

def main(inputPath):
    fileType = {'.zip','.7z','.rar'}  # 使用集合而不是列表，查找更快
    try:
        for eachPath in inputPath[1:]:
            eachPath = Path(eachPath)
            if eachPath.is_dir():
                for eachFile in eachPath.glob('**/*'):
                    if eachFile.suffix.lower() in fileType:
                        ifZipEncrypted(eachFile)
            elif eachPath.is_file() and eachPath.suffix.lower() in fileType:
                ifZipEncrypted(eachPath)
    except Exception as e:
        print(f'程序执行出错：{str(e)}')    
    os.system('pause')
    
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass