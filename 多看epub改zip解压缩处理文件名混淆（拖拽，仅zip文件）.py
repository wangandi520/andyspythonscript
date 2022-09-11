# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

import sys
import io
import zipfile
from pathlib import Path

# 半成品，xhtml文件内文件名未改

def doDKunzip(filePath):
    # type(filePath): Path
    # 把epub文件备份后的扩展名改成zip
    if zipfile.is_zipfile(filePath):
        zf = zipfile.ZipFile(filePath)
        allFileNameList = []
        print('文件名: ' + filePath.name)
        for eachFile in zf.infolist():
            if not eachFile.is_dir():
                allFileNameList.append(eachFile.filename)
                
        # 新建文件夹 = zip文件名
        newFolderPath = filePath.parent.joinpath(filePath.stem)
        if not newFolderPath.exists():
            Path.mkdir(newFolderPath)
            
        # 通过toc.ncx确定正常的正文顺序
        oldXhtmlFileName = []
        newXhtmlFileName = []
        with zf.open('OEBPS/toc.ncx') as readFile:
            for line in io.TextIOWrapper(readFile, 'utf-8'):
                if '.xhtml' in repr(line):
                    tempIndex01 = repr(line).find('<content src="') + 14
                    tempIndex02 = repr(line).find('.xhtml') + 6
                    oldXhtmlFileName.append('OEBPS/' + repr(line)[tempIndex01:tempIndex02])
        
        # 解压正文Text
        for tempIndex in range(0, len(oldXhtmlFileName)):
            #print(oldXhtmlFileName[tempIndex])
            Path(zf.extract(oldXhtmlFileName[tempIndex], path = newFolderPath)).rename(newFolderPath.joinpath(Path(oldXhtmlFileName[tempIndex]).parent.joinpath(str(tempIndex).zfill(4) + '.xhtml')))
            newXhtmlFileName.append(Path(oldXhtmlFileName[tempIndex]).parent.joinpath(Path(str(tempIndex).zfill(4) + '.xhtml')))
        for each in newXhtmlFileName:
            print(each)
            
        # 解压图片Images
        oldImageFileName = []
        newImageFileName = []
        for eachFile in allFileNameList:
            if 'Image' in eachFile:
                oldImageFileName.append(eachFile)
        for tempIndex in range(0, len(oldImageFileName)):
            #print(oldImageFileName[tempIndex])
            Path(zf.extract(oldImageFileName[tempIndex], path = newFolderPath)).rename(newFolderPath.joinpath(Path(oldImageFileName[tempIndex]).parent.joinpath(str(tempIndex).zfill(4) + Path(oldImageFileName[tempIndex]).suffix)))
            newImageFileName.append(Path(oldImageFileName[tempIndex]).parent.joinpath(Path(str(tempIndex).zfill(4) + '.xhtml')))
            
        # 解压Styles
        oldStylesFileName = []
        newStylesFileName = []
        for eachFile in allFileNameList:
            if 'Styles' in eachFile:
                oldStylesFileName.append(eachFile)
        for tempIndex in range(0, len(oldStylesFileName)):
            #print(oldStylesFileName[tempIndex])
            Path(zf.extract(oldStylesFileName[tempIndex], path = newFolderPath)).rename(newFolderPath.joinpath(Path(oldStylesFileName[tempIndex]).parent.joinpath(str(tempIndex).zfill(4) + Path(oldStylesFileName[tempIndex]).suffix)))
            newStylesFileName.append(Path(oldStylesFileName[tempIndex]).parent.joinpath(Path(str(tempIndex).zfill(4) + '.xhtml')))
        
        # 解压字体Fonts
        oldFontsFileName = []
        newFontsFileName = []
        for eachFile in allFileNameList:
            if 'Fonts' in eachFile:
                oldFontsFileName.append(eachFile)
        for tempIndex in range(0, len(oldFontsFileName)):
            #print(oldFontsFileName[tempIndex])
            Path(zf.extract(oldFontsFileName[tempIndex], path = newFolderPath)).rename(newFolderPath.joinpath(Path(oldFontsFileName[tempIndex]).parent.joinpath(str(tempIndex).zfill(4) + Path(oldFontsFileName[tempIndex]).suffix)))
            newFontsFileName.append(Path(oldFontsFileName[tempIndex]).parent.joinpath(Path(str(tempIndex).zfill(4) + '.xhtml')))
        
        # 解压其他
        # otherFileName = ['mimetype', 'META-INF/encryption.xml', 'META-INF/container.xml', 'OEBPS/toc.ncx', 'OEBPS/content.opf']
        otherFileName = ['mimetype', 'META-INF/container.xml', 'OEBPS/toc.ncx', 'OEBPS/content.opf']
        for each in otherFileName:
            zf.extract(each, path = newFolderPath)
            
            
def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        # 文件格式
        fileType = ['.zip']
        
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                doDKunzip(file)

        if Path.is_file(Path(aPath)):
            doDKunzip(Path(aPath))
            
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass