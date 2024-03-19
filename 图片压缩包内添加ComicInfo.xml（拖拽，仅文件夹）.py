# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# by Andy
# v0.2

from pathlib import Path
import sys
import re
import zipfile
import os

def writefile(fileName, allFileContent):
    with open(fileName, mode='w', encoding='UTF-8') as newfile:
        newfile.writelines(allFileContent)

def doConvertComicInfo(aPath):
    # 给漫画压缩包添加ComicInfo.xml
    # 仅拖拽文件夹，文件夹内是需要添加ComicInfo.xml的压缩包
    # 符合以下条件才会运行脚本
    # 1. 文件名要求格式[书名][作者][出版社][扫者]册数.扩展名
    # 2. 压缩包内不含文件夹时，而且没有ComicInfo.xml
    # 3. 文件夹内的文件[书名][作者]都一致
    # 4. 文件扩展名fileType = ['.cbz', '.zip']
    fileType = ['.cbz', '.zip']
    # 判断是不是所有文件[书名][作者]都一致
    ifIsSorted = True
    # 所有文件名的列表
    allFilePath = []
    for eachFile in Path(aPath).glob('*'):
        if (Path(eachFile).suffix.lower() in fileType):
            allFilePath.append(eachFile)
            if eachFile.name.count('[') != 4 or eachFile.name.count(']') != 4 :
                ifIsSorted = False
    if ifIsSorted:
        # 第一个文件的书名
        bookName = re.findall("(\\[[^\\]]*\\])", allFilePath[0].name)[0]
        # 第一个文件的作者名
        bookAuthor = re.findall("(\\[[^\\]]*\\])", allFilePath[0].name)[1]
        # 第一个文件的出版社
        bookPublisher = re.findall("(\\[[^\\]]*\\])", allFilePath[0].name)[2]
        # 第一个文件的扫者
        bookScan = re.findall("(\\[[^\\]]*\\])", allFilePath[0].name)[3]
        for eachFile in allFilePath:
            if re.findall("(\\[[^\\]]*\\])", eachFile.name)[0] != bookName:
                ifIsSorted = False
            if re.findall("(\\[[^\\]]*\\])", eachFile.name)[1] != bookAuthor:
                ifIsSorted = False
    if not ifIsSorted:
        print('文件名格式不符合要求')
        os.system('pause')
    if ifIsSorted:
        for tempIndex in range(0, len(allFilePath)):
            with zipfile.ZipFile(allFilePath[tempIndex], 'a') as myzipfile:
                # 压缩包内不含文件夹时，而且没有ComicInfo.xml时，才会添加ComicInfo.xml
                noDirAndnoXml = True
                # 图片文件数
                PageCount = 0
                for eachFile in myzipfile.infolist():
                    # print(eachFile)
                    if eachFile.is_dir():
                        noDirAndnoXml = False
                    if eachFile.filename == 'ComicInfo.xml':
                        noDirAndnoXml = False
                    if not eachFile.is_dir() and Path(eachFile.filename).suffix.lower() in ['.png', '.jpg', '.jpeg']:
                        PageCount = PageCount + 1
                if noDirAndnoXml:
                    allXmlContent = []
                    allXmlContent.append('<?xml version="1.0"?>\n')
                    allXmlContent.append('<ComicInfo xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n')
                    allXmlContent.append('  <Title>' + bookName[1:-1] + '</Title>\n')
                    allXmlContent.append('  <Series>' + bookName[1:-1] + '</Series>\n')
                    allXmlContent.append('  <Number>' + str(tempIndex + 1) + '<Number>\n')
                    allXmlContent.append('  <Count>' + str(len(allFilePath)) + '</Count>\n')
                    allXmlContent.append('  <Publisher>' + bookPublisher[1:-1] + '</Publisher>\n')
                    allXmlContent.append('  <PageCount>' + str(PageCount) + '</PageCount>\n')
                    allXmlContent.append('  <ScanInformation>' + bookScan[1:-1] + '</ScanInformation>\n')
                    # 其他需要填的信息，参考
                    # https://moeshare.cc/read-htm-tid-275776.html
                    # https://anansi-project.github.io/docs/comicinfo/documentation#scaninformation
                    # allXmlContent.append('  <>' + x + '</>\n')
                    allXmlContent.append('</ComicInfo>')
                    writefile('ComicInfo.xml', allXmlContent)
                    myzipfile.write('ComicInfo.xml')
                    Path('ComicInfo.xml').unlink()
                    print('成功： ' + allFilePath[tempIndex].name)
                else:
                    print('失败： ' + allFilePath[tempIndex].name + '，压缩包内存在文件夹或ComicInfo.xml')
        os.system('pause')

def main(inputPath):
    for aPath in inputPath[1:]:
        if Path.is_dir(Path(aPath)):
            doConvertComicInfo(Path(aPath))

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass