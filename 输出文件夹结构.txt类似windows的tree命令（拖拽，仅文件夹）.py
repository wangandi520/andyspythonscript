# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# by Andy
# v0.1

from pathlib import Path
import sys
import re

from typing import List, Union

# 把可以更改的设置都放在这里
CONFIG = {
    # 参数，True = 只输出文件夹，False = 输出文件和文件夹
    'onlyFolders': False,
    # 当onlyFolders = False时，设置文件后缀，为空则不限制
    'fileSuffix': {},
    # 第一行显示完整路径，True = 显示完整路径，False = 只显示文件夹名
    'showFullPath': False
}

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
    print(f"当前设置：{'只输出文件夹' if CONFIG['onlyFolders'] else '输出文件夹和文件'}{'' if CONFIG['onlyFolders'] else '，文件类型限制为' + str(CONFIG['fileSuffix']) if CONFIG['fileSuffix'] else '，不限制文件类型'}")
    try:
        # 创建一个列表来存储文件结构
        tree_output = []
        tree_output.append(f"{str(folderName) if CONFIG['showFullPath'] else folderName.name}\n")
        
        # 递归生成文件结构
        def generate_tree(path, prefix="", is_last=True, level=0):
            # 获取目录下的所有项目（文件和文件夹）
            items = list(path.iterdir())
            # 按文件夹在前，文件在后排序
            items.sort(key=lambda x: (not x.is_dir(), x.name))
            
            # 遍历所有项目
            for i, item in enumerate(items):
                is_last_item = i == len(items) - 1
                # 确定当前项目的前缀
                if level == 0:
                    current_prefix = "├── " if not is_last_item else "└── "
                else:
                    current_prefix = prefix + ("├── " if not is_last_item else "└── ")
                
                # 如果是文件夹
                if item.is_dir():
                    tree_output.append(f"{current_prefix}{item.name}\n")
                    # 确定下一级的前缀
                    next_prefix = prefix + ("│   " if not is_last_item else "    ")
                    # 递归处理子文件夹
                    generate_tree(item, next_prefix, is_last_item, level + 1)
                # 如果是文件且不是只输出文件夹模式
                elif not CONFIG['onlyFolders']:
                    # 检查文件后缀
                    if not CONFIG['fileSuffix'] or any(item.name.endswith(suffix) for suffix in CONFIG['fileSuffix']):
                        tree_output.append(f"{current_prefix}{item.name}\n")
        
        # 开始生成树形结构
        generate_tree(folderName)
        # 写入文件
        writefile(str(folderName) + '.txt', tree_output)
        
    except Exception as e:
        print(f'处理文件时出错：{folderName}，错误：{str(e)}')
    input('完成，按回车键退出')

def main(inputPath: list[str]) -> None:
    try:
        for eachPath in inputPath[1:]:
            eachPath = Path(eachPath)
            if eachPath.is_dir():
                doConvert(eachPath)  # 默认显示文件和文件夹
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