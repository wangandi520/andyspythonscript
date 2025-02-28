# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# Programmed by Andy
# 2025.02.28
# 部分函数由deepseek生成

from pathlib import Path
import sys
import unicodedata

def readfile(filename):
    # 读取文件
    with open(filename, mode='r', encoding='UTF-8') as file:
        filereadlines = file.readlines()
    for i in range(len(filereadlines)):
        filereadlines[i] = filereadlines[i].rstrip()
    return filereadlines

def writefile(filename,filereadlines):
    # 写入文件
    newfile = open(Path(filename).parent.joinpath(Path(filename).stem + '转换后.txt'), mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()
    print('完成：' + str(Path(filename).name))
    
def is_punctuation(char):
    # 判断给定字符是否为标点符号。
    if len(char) != 1:
        return False
    category = unicodedata.category(char)
    if char not in [',', '，']:
        return category.startswith('P')  
    
def convertMoonReadermrexpt(filename):
    # 读取.txt文件
    filereadlines = readfile(filename)
    print('处理：' + str(Path(filename).name))
    # 存储所有文本
    tempContent = []
    processed_lines = []
    # 去掉空白行
    for eachLine in filereadlines:
        if eachLine.strip() != '':
            tempContent.append(eachLine)
    i = 0
    while i < len(tempContent):
        current_line = tempContent[i]
        last_char = current_line[-1]
        
        # 如果当前行以标点结尾，直接保留
        if is_punctuation(last_char):
            processed_lines.append(current_line + '\n')
            i += 1
        else:
            # 合并后续所有无标点结尾的行，直到遇到标点或文件结束
            merged_line = current_line
            j = i + 1
            while j < len(tempContent):
                merged_line += tempContent[j]  # 直接拼接下一行内容
                
                # 检查合并后的新行是否以标点结尾
                stripped_merged = merged_line.rstrip()
                if stripped_merged:
                    last_char_merged = stripped_merged[-1]
                    if is_punctuation(last_char_merged):
                        j += 1  # 包含当前行j
                        break
                j += 1
            
            processed_lines.append(merged_line + '\n')
            i = j  # 跳转到下一个未处理的行

    writefile(filename,processed_lines)
    # 输出
    # outputContent = []
    # outputContent.append(myFrontMatter)
    # outputContent.append('\n\n**共' + str(len(allContentSorted)) + '条标注**\n\n---')
    # for myIndex in range(0, len(allContentSorted)):
        # outputContent.append('\n\n> ' + allContentSorted[myIndex][1] + '\n\n')
        # if len(allContentSorted[myIndex]) == 4:
            # outputContent.append('**' +allContentSorted[myIndex][2] + '**\n\n')
            # outputContent.append('*' + allContentSorted[myIndex][3] + '*\n\n')
        # elif len(allContentSorted[myIndex]) == 3:
            # outputContent.append('*' +allContentSorted[myIndex][2] + '*\n\n')
        # outputContent.append('---')
        # if myIndex == 1:
            # outputContent.append('\n\n<!-- more -->')

    # writefile(filename, outputContent)
    
def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for eachFile in Path(aPath).glob('**/*'):
                if (Path(eachFile).suffix == '.txt'):
                    convertMoonReadermrexpt(eachFile)
        if Path.is_file(Path(aPath)):
            if (Path(aPath).suffix == '.txt'):
                convertMoonReadermrexpt(aPath)
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass