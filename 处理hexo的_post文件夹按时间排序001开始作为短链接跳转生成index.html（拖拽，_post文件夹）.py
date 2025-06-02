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
        print(f'处理中')
        
        # 存储所有文件信息的列表
        allFiles = []
        
        for eachFile in folderName.glob('**/*'):
            if eachFile.suffix.lower() in fileType:
                allLines = readfile(eachFile)
                title = ''
                date = ''
                for eachLine in allLines:
                    # 处理每一行
                    eachLine = eachLine.strip()
                    if eachLine.startswith('date:'):
                        date = eachLine[5:].strip()
                    if title and date:  # 如果都找到了就提前退出
                        break
                
                # 将文件信息添加到列表中，只包含title和date
                allFiles.append({
                    # hexo网址的名字是文件名，不是title名
                    'fileName': eachFile.stem,  # 使用 stem 获取不带扩展名的文件名
                    'date': date
                })
        # 按日期排序
        allFilesSorted = sorted(allFiles, key=lambda x: x['date'])
        
        # 创建HTML格式的数据
        allFileToHtml = []
        for index, fileInfo in enumerate(allFilesSorted, 1):
            # 生成四位数索引，例如0001, 0002...
            indexStr = str(index).zfill(4)
            fileInfo['index'] = indexStr
            
            # 从日期中提取年月日
            date_parts = fileInfo['date'].split('-')
            if len(date_parts) >= 3:
                year, month, day = date_parts[0], date_parts[1], date_parts[2].split()[0]
                # 构建href链接
                href = f"/{year}/{month}/{day}/{fileInfo['fileName']}"
                # 构建HTML
                html = f'<p id="{indexStr}"><a href="{href}"><span class="id">{indexStr}</span>&nbsp<span class="fileName">{fileInfo["fileName"]}</span></a>&nbsp;<span><input type="text" value="/{href}"></span>&nbsp;<span class="date">{fileInfo["date"]}</span></p>\n'
                allFileToHtml.append(html)
        # 设置HTML模板并将所有HTML元素写入同一行（不使用换行符）
        htmlHeader = '<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>短链接跳转</title></head><body>'
        htmlContent = ''.join(allFileToHtml) + '<script>document.addEventListener("DOMContentLoaded",function(){const queryString=window.location.search;const urlParams=new URLSearchParams(queryString);const idValue=urlParams.get("id");if(idValue){if(idValue.length>4){return;}const formattedId=idValue.padStart(4,"0");const pElement=document.getElementById(formattedId);if(pElement){const aElement=pElement.querySelector("a");if(aElement&&aElement.href){window.location.href=aElement.href;}}}let currentUrl=window.location.href;if(currentUrl.endsWith("/")){currentUrl=currentUrl.slice(0,-1);}const inputs=document.querySelectorAll("body p input");inputs.forEach(input=>{const parentP=input.closest("p");if(parentP&&parentP.id){const idWithoutLeadingZeros=parseInt(parentP.id,10).toString();input.value=currentUrl+"?id="+idWithoutLeadingZeros}else{input.value=currentUrl}});});</script></body></html>'
        newHtmlFile = htmlHeader + '\n' + htmlContent
        if not Path('index.html').exists():
            writefile('index.html', [newHtmlFile])
            print('index.html已生成。')
        else:
            print('index.html已存在，未覆盖。')
                
    except Exception as e:
        print(f'处理文件时出错：{folderName}，错误：{str(e)}')
    input('按回车键继续...或者直接关闭本窗口')

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