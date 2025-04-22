# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# by Andy
# v0.2

from pathlib import Path
import sys
import re

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

def doConvert(folderName: Path) -> None:
    fileType = {'.md'}  # 使用集合而不是列表，查找更快
    try:
        print(f'处理中：{folderName}')
        
        for eachFile in folderName.glob('**/*'):
            if eachFile.suffix.lower() in fileType:
                allLines = readfile(eachFile)
                title = ''
                
                # 获取不带扩展名的文件名
                filename_without_ext = eachFile.stem
                
                for eachLine in allLines:
                    # 处理每一行
                    eachLine = eachLine.strip()
                    if eachLine.startswith('title:'):
                        title = eachLine[6:].strip()
                        # 如果找到title就可以比较了
                        if title and title != filename_without_ext:
                            print(f'文件名与标题不一致: {eachFile}')
                            print(f'文件名: {filename_without_ext}')
                            print(f'标题: {title}\n')
                        break

    except Exception as e:
        print(f'处理文件时出错：{folderName}，错误：{str(e)}')
    input('按回车键继续...')
    
def main(inputPath: list[str]) -> None:
    try:
        for eachPath in inputPath[1:]:
            eachPath = Path(eachPath)
            if eachPath.is_dir():
                if eachPath.name != '_posts':
                    print('需要处理的文件夹可能不是hexo\\_posts，但程序仍然会继续')
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