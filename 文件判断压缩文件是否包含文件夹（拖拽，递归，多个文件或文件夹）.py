# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip install py7zr rarfile

import sys
import zipfile
import py7zr
import rarfile
import os
from pathlib import Path

CONFIG = {
    'onlyShowNoFolder': True,  # True: 只显示不包含文件夹的压缩包名，False: 全部显示
}

def ifZipContainsFolder(filePath):
    try:
        suffix = Path(filePath).suffix.lower()
        containsFolder = False
        
        if suffix == '.zip':
            with zipfile.ZipFile(filePath) as zip_file:
                for zip_info in zip_file.infolist():
                    # 同时检查正斜杠和反斜杠
                    if zip_info.filename.endswith('/') or '/' in zip_info.filename or '\\' in zip_info.filename:
                        if not CONFIG['onlyShowNoFolder']:
                            print(f"{Path(filePath).name} 包含文件夹")
                        containsFolder = True
                        break
        elif suffix == '.7z':
            with py7zr.SevenZipFile(filePath, mode='r') as z:
                file_list = z.getnames()
                for file_path in file_list:
                    # 同时检查正斜杠和反斜杠
                    if '/' in file_path or '\\' in file_path:
                        if not CONFIG['onlyShowNoFolder']:
                            print(f"{Path(filePath).name} 包含文件夹")
                        containsFolder = True
                        break
        elif suffix == '.rar':
            with rarfile.RarFile(filePath) as rar_file:
                for info in rar_file.infolist():
                    # 同时检查正斜杠和反斜杠
                    if info.isdir() or '/' in info.filename or '\\' in info.filename:
                        if not CONFIG['onlyShowNoFolder']:
                            print(f"{Path(filePath).name} 包含文件夹")
                        containsFolder = True
                        break
                        
        # 如果不包含文件夹，打印提示信息
        if not containsFolder:
            print(f"{Path(filePath).name} 不包含文件夹")
            
    except Exception as e:
        print(f"处理 {Path(filePath).name} 时出错: {str(e)}")

def main(inputPath):
    fileType = {'.zip','.7z','.rar'}  # 使用集合而不是列表，查找更快
    try:
        for eachPath in inputPath[1:]:
            eachPath = Path(eachPath)
            if eachPath.is_dir():
                for eachFile in eachPath.glob('**/*'):
                    if eachFile.suffix.lower() in fileType:
                        ifZipContainsFolder(eachFile)
            elif eachPath.is_file() and eachPath.suffix.lower() in fileType:
                ifZipContainsFolder(eachPath)
    except Exception as e:
        print(f'程序执行出错：{str(e)}')    
    os.system('pause')
    
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass