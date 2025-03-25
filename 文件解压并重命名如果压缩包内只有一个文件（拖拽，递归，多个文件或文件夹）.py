# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# by Andy
# v0.2

from pathlib import Path
import sys
import re
import zipfile
import shutil

from typing import List, Union

def validFileName(oldFileName):
    # '/ \ : * ? " < > |'
    # 替换为下划线
    validChars = r"[\/\\\:\*\?\"\<\>\|]"  
    newFileName = re.sub(validChars, "_", oldFileName)
    return newFileName
    
def writefile(fileName: Path, allFileContent: list[str]) -> None:
    try:
        with open(fileName, mode='w', encoding='UTF-8') as newfile:
            newfile.writelines(allFileContent)
    except Exception as e:
        print(f'写入文件失败：{fileName}，错误：{str(e)}')

def readfile(fileName: Path) -> list[str]:
    try:
        with open(fileName, mode='r', encoding='UTF-8') as newfile:
            return newfile.readlines()
    except Exception as e:
        print(f'读取文件失败：{fileName}，错误：{str(e)}')
        return []

def doConvert(fileName: Path) -> None:
    try:
        print(f'处理文件：{fileName}')
        # 检查是否为zip文件
        if fileName.suffix.lower() == '.zip':
            # 不创建临时目录，直接读取zip文件内容
            with zipfile.ZipFile(fileName, 'r') as zip_ref:
                # 获取zip文件中的所有文件列表
                file_list = zip_ref.namelist()
                
                # 更可靠地检查是否有文件夹（检查路径中是否包含分隔符）
                has_folder = any('/' in name or '\\' in name for name in file_list)
                
                # 如果有文件夹，跳过处理
                if has_folder:
                    print(f'压缩包内有文件夹，跳过处理')
                    return
                
                # 如果只有一个文件
                if len(file_list) == 1:
                    file_to_extract = file_list[0]
                    # 使用pathlib获取文件扩展名
                    file_extension = Path(file_to_extract).suffix
                    # 构建新文件名：zip文件名+原扩展名
                    new_file_path = fileName.parent / f"{fileName.stem}{file_extension}"
                    
                    # 直接解压到目标位置
                    with zip_ref.open(file_to_extract) as source, open(new_file_path, 'wb') as target:
                        shutil.copyfileobj(source, target)
                    
                    print(f'已解压并重命名: {new_file_path}')
                else:
                    print(f'压缩包内有多个文件，跳过处理')
    except Exception as e:
        print(f'处理文件时出错：{fileName}，错误：{str(e)}')

def main(inputPath: list[str]) -> None:
    fileType = {'.txt', '.zip'}  # 添加.zip文件类型
    try:
        for eachPath in inputPath[1:]:
            eachPath = Path(eachPath)
            if eachPath.is_dir():
                for eachFile in eachPath.glob('**/*'):
                    if eachFile.suffix.lower() in fileType:
                        doConvert(eachFile)
            elif eachPath.is_file() and eachPath.suffix.lower() in fileType:
                doConvert(eachPath)
    except Exception as e:
        print(f'程序执行出错：{str(e)}')

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
        else:
            print('请拖拽文件到本脚本，或者命令行运行时添加文件路径')
    except IndexError:
        pass