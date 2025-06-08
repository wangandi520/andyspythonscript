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
                html = f'<tr><td><a href="{href}"><span class="id">{indexStr}</span>&nbsp;<span class="fileName">{fileInfo["fileName"]}</span></a></td><td><input type="text" value="/{href}"></td><td>{fileInfo["date"]}</td></tr>\n'
                allFileToHtml.append(html)
        
        htmlHeader = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>短链接跳转</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
            table-layout: fixed;
        }
        th, td {
            padding: 3px;
            border: 1px solid #ddd;
            text-align: left;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        td:first-child {
            width: auto;
            min-width: fit-content;
        }
        td:nth-child(2) {
            width: 40%;
        }
        td:nth-child(3) {
            width: 20%;
        }
        th {
            background-color: #f5f5f5;
        }
        input {
            width: 95%;
            padding: 4px;
        }
        .table-wrapper {
            overflow-x: auto;
        }
        tbody tr:hover {
            background-color: #f8f8f8;
            transition: background-color 0.2s ease;
        }
    </style>
</head>
<body>
<div class="table-wrapper">
<table>
    <thead>
        <tr>
            <th>文章链接</th>
            <th>短链接</th>
            <th>发布日期</th>
        </tr>
    </thead>
    <tbody>'''

        htmlContent = ''.join(allFileToHtml) + '</tbody></table></div><script>' + '''document.addEventListener("DOMContentLoaded",function(){
    const queryString=window.location.search;
    const urlParams=new URLSearchParams(queryString);
    const idValue=urlParams.get("id");
    const searchValue=urlParams.get("search");
    if(searchValue){
        const links = document.querySelectorAll('a');
        for(const link of links) {
            const decodedHref = decodeURIComponent(link.href);
            if(decodedHref.includes(searchValue)) {
                const baseUrl = window.location.origin;
                window.location.href = baseUrl + link.href;
                return;
            }
        }
    }
    if(idValue){
        if(idValue.length>4){return;}
        const formattedId=idValue.padStart(4,"0");
        const spans = document.querySelectorAll('span.id');
        for(const span of spans) {
            if(span.textContent === formattedId) {
                const aElement = span.closest('a');
                if(aElement && aElement.href) {
                    window.location.href = aElement.href;
                    break;
                }
            }
        }
    }
    let currentUrl=window.location.href;
    if(currentUrl.endsWith("/")){
        currentUrl=currentUrl.slice(0,-1);
    }
    const inputs=document.querySelectorAll("td input");
    inputs.forEach(input=>{
        const tr=input.closest("tr");
        const idSpan=tr.querySelector(".id");
        if(idSpan){
            const id=idSpan.textContent;
            const idWithoutLeadingZeros=parseInt(id,10).toString();
            input.value=currentUrl+"?id="+idWithoutLeadingZeros;
        }
    });
});</script></body></html>'''
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