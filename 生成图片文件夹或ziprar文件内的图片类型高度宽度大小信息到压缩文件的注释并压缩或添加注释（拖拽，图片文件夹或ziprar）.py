# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip install pillow

from PIL import Image  
from pathlib import Path
import sys
import datetime
import zipfile
import rarfile
   
def formatFileSize(sizeBytes):
    sizeBytes = float(sizeBytes)
    result = float(abs(sizeBytes))
    suffix = "B";
    if(result > 1024):
        suffix = "KB"
        mult = 1024
        result = result / 1024
    if(result > 1024):
        suffix = "MB"
        mult *= 1024
        result = result / 1024
    if (result > 1024) :
        suffix = "GB"
        mult *= 1024
        result = result / 1024
    if (result > 1024) :
        suffix = "TB"
        mult *= 1024
        result = result / 1000
    if (result > 1024) :
        suffix = "PB"
        mult *= 1024
        result = result / 1024
    return format(result,'.2f') + suffix


def writeFile(myPath, filereadlines):
    newfile = open(myPath, mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close() 
    
    
def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        # 文件格式
        fileType = ['.jpg', '.png']
        # 图片宽度统计，size[0]
        fileWidth = {}
        # 图片高度统计，size[1]
        fileHeight = {}
        # 图片长度宽度统计，[size[0],，size[1]]
        fileWidthAndHeight = {}
        # 图片类型统计
        numberOfFileType = {}
        # 文件夹大小
        allFileSize = 0
        # 文件夹文件数量
        allFileCount = 0
        # 输出
        outputFile = []
        # 文件路径
        allFilelist = []
        # 是否覆盖zip文件的注释
        writeToZipComment = True
        
        if Path.is_file(Path(aPath)):
            if rarfile.is_rarfile(Path(aPath)):
                with rarfile.RarFile(Path(aPath), 'a') as rf:
                    fileNameList = []
                    for eachFile in rf.infolist():
                        if not eachFile.is_dir():
                            fileNameList.append(eachFile.filename)
                    allFileCount = len(fileNameList)
                    for fileName in fileNameList:
                        if Path(fileName).suffix in fileType:
                            with rf.open(fileName) as readImage:
                                tmpImg = Image.open(readImage)
                                if Path(fileName).suffix not in numberOfFileType:
                                    numberOfFileType[Path(fileName).suffix] = 1
                                else:
                                    numberOfFileType[Path(fileName).suffix] = numberOfFileType[Path(fileName).suffix] + 1
                                if (tmpImg.size[1] not in fileHeight):
                                    fileHeight[tmpImg.size[1]] = 1
                                elif (tmpImg.size[1] in fileHeight):
                                    fileHeight[tmpImg.size[1]] = fileHeight[tmpImg.size[1]] + 1
                                if (tmpImg.size[0] not in fileWidth):
                                    fileWidth[tmpImg.size[0]] = 1
                                elif (tmpImg.size[0] in fileWidth):
                                    fileWidth[tmpImg.size[0]] = fileWidth[tmpImg.size[0]] + 1
                                if ((tmpImg.size[0],tmpImg.size[1]) not in fileWidthAndHeight):
                                    fileWidthAndHeight[(tmpImg.size[0],tmpImg.size[1])] = 1
                                elif ((tmpImg.size[0],tmpImg.size[1]) in fileWidthAndHeight):
                                    fileWidthAndHeight[(tmpImg.size[0],tmpImg.size[1])] = fileWidthAndHeight[(tmpImg.size[0],tmpImg.size[1])] + 1
                    for key in sorted(numberOfFileType):
                        print('类型：' + key[1:] + '，数量: ' +  str(numberOfFileType[key]))
                        outputFile.append('类型：' + key[1:] + '，数量: ' +  str(numberOfFileType[key]) + '\n')
                    for key in fileHeight:
                        print('高度：' + str(key) + ', 数量: ' + str(fileHeight[key]))
                        outputFile.append('高度：' + str(key) + ', 数量: ' + str(fileHeight[key]) + '\n')    
                    for key in fileWidth:
                        print('宽度：' + str(key) + ', 数量: ' + str(fileWidth[key]))
                        outputFile.append('宽度：' + str(key) + ', 数量: ' + str(fileWidth[key]) + '\n')      
                    for key in fileWidthAndHeight:
                        print('宽度和高度：' + str(key) + ', 数量: ' + str(fileWidthAndHeight[key]))
                        outputFile.append('宽度和高度：' + str(key) + ', 数量: ' + str(fileWidthAndHeight[key]) + '\n')      
                    print('文件数量：' + str(allFileCount))
                    print('文件大小：' + formatFileSize(Path(aPath).stat().st_size))
                    print('文件创建时间：' + datetime.datetime.fromtimestamp(Path(aPath).stat().st_ctime).strftime('%Y-%m-%d %H:%M:%S'))
                    print('文件修改时间：' + datetime.datetime.fromtimestamp(Path(aPath).stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S'))
                    outputFile.append('文件数量：' + str(allFileCount)+ '\n')
                    outputFile.append('文件大小：' + formatFileSize(Path(aPath).stat().st_size) + '\n')
                    outputFile.append('文件创建时间：' + datetime.datetime.fromtimestamp(Path(aPath).stat().st_ctime).strftime('%Y-%m-%d %H:%M:%S') + '\n')
                    outputFile.append('文件修改时间：' + datetime.datetime.fromtimestamp(Path(aPath).stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S') + '\n')
                    
                    writeFile(Path(aPath).name + '.txt', outputFile)
                
            if zipfile.is_zipfile(Path(aPath)):
                with zipfile.ZipFile(Path(aPath), 'a') as zf:
                    fileNameList = []
                    for eachFile in zf.infolist():
                        if not eachFile.is_dir():
                            fileNameList.append(eachFile.filename)
                    allFileCount = len(fileNameList)
                    for fileName in fileNameList:
                        if Path(fileName).suffix in fileType:
                            with zf.open(fileName) as readImage:
                                tmpImg = Image.open(readImage)
                                if Path(fileName).suffix not in numberOfFileType:
                                    numberOfFileType[Path(fileName).suffix] = 1
                                else:
                                    numberOfFileType[Path(fileName).suffix] = numberOfFileType[Path(fileName).suffix] + 1
                                if (tmpImg.size[1] not in fileHeight):
                                    fileHeight[tmpImg.size[1]] = 1
                                elif (tmpImg.size[1] in fileHeight):
                                    fileHeight[tmpImg.size[1]] = fileHeight[tmpImg.size[1]] + 1
                                if (tmpImg.size[0] not in fileWidth):
                                    fileWidth[tmpImg.size[0]] = 1
                                elif (tmpImg.size[0] in fileWidth):
                                    fileWidth[tmpImg.size[0]] = fileWidth[tmpImg.size[0]] + 1
                                if ((tmpImg.size[0],tmpImg.size[1]) not in fileWidthAndHeight):
                                    fileWidthAndHeight[(tmpImg.size[0],tmpImg.size[1])] = 1
                                elif ((tmpImg.size[0],tmpImg.size[1]) in fileWidthAndHeight):
                                    fileWidthAndHeight[(tmpImg.size[0],tmpImg.size[1])] = fileWidthAndHeight[(tmpImg.size[0],tmpImg.size[1])] + 1
                    for key in sorted(numberOfFileType):
                        print('类型：' + key[1:] + '，数量: ' +  str(numberOfFileType[key]))
                        outputFile.append('类型：' + key[1:] + '，数量: ' +  str(numberOfFileType[key]) + '\n')
                    for key in fileHeight:
                        print('高度：' + str(key) + ', 数量: ' + str(fileHeight[key]))
                        outputFile.append('高度：' + str(key) + ', 数量: ' + str(fileHeight[key]) + '\n')    
                    for key in fileWidth:
                        print('宽度：' + str(key) + ', 数量: ' + str(fileWidth[key]))
                        outputFile.append('宽度：' + str(key) + ', 数量: ' + str(fileWidth[key]) + '\n')      
                    for key in fileWidthAndHeight:
                        print('宽度和高度：' + str(key) + ', 数量: ' + str(fileWidthAndHeight[key]))
                        outputFile.append('宽度和高度：' + str(key) + ', 数量: ' + str(fileWidthAndHeight[key]) + '\n')      
                    print('文件数量：' + str(allFileCount))
                    print('文件大小：' + formatFileSize(Path(aPath).stat().st_size))
                    print('文件创建时间：' + datetime.datetime.fromtimestamp(Path(aPath).stat().st_ctime).strftime('%Y-%m-%d %H:%M:%S'))
                    print('文件修改时间：' + datetime.datetime.fromtimestamp(Path(aPath).stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S'))
                    outputFile.append('文件数量：' + str(allFileCount)+ '\n')
                    outputFile.append('文件大小：' + formatFileSize(Path(aPath).stat().st_size) + '\n')
                    outputFile.append('文件创建时间：' + datetime.datetime.fromtimestamp(Path(aPath).stat().st_ctime).strftime('%Y-%m-%d %H:%M:%S') + '\n')
                    outputFile.append('文件修改时间：' + datetime.datetime.fromtimestamp(Path(aPath).stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S') + '\n')
                    
                    writeFile(Path(aPath).name + '.txt', outputFile)
                    if writeToZipComment:
                        zf.comment = ''.join(outputFile).encode('utf-8')
        
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if Path.is_file(file) and (file.suffix in fileType):
                    allFileSize = allFileSize + file.stat().st_size
                    allFileCount = allFileCount + 1
                    #allFilelist.append(file.relative_to(Path(aPath).parent))
                    allFilelist.append(file)
                    tmpImg = Image.open(file)
                    if file.suffix not in numberOfFileType:
                        numberOfFileType[file.suffix] = 1
                    else:
                        numberOfFileType[file.suffix] = numberOfFileType[file.suffix] + 1
                    if (tmpImg.size[1] not in fileHeight):
                        fileHeight[tmpImg.size[1]] = 1
                    elif (tmpImg.size[1] in fileHeight):
                        fileHeight[tmpImg.size[1]] = fileHeight[tmpImg.size[1]] + 1
                    if (tmpImg.size[0] not in fileWidth):
                        fileWidth[tmpImg.size[0]] = 1
                    elif (tmpImg.size[0] in fileWidth):
                        fileWidth[tmpImg.size[0]] = fileWidth[tmpImg.size[0]] + 1
                    if ((tmpImg.size[0],tmpImg.size[1]) not in fileWidthAndHeight):
                        fileWidthAndHeight[(tmpImg.size[0],tmpImg.size[1])] = 1
                    elif ((tmpImg.size[0],tmpImg.size[1]) in fileWidthAndHeight):
                        fileWidthAndHeight[(tmpImg.size[0],tmpImg.size[1])] = fileWidthAndHeight[(tmpImg.size[0],tmpImg.size[1])] + 1
            folderName = Path(aPath).name
            if folderName[0] == '[':
                letterCount = 0
                for eachLetter in folderName:
                    if eachLetter in ['[', ']']:
                        letterCount = letterCount + 1
                # 文件夹格式[书名][作者][出版]Vol01
                if letterCount == 6:
                    folderName = folderName
                    print('书名：' + folderName.split('][')[0][1:])
                    print('作者：' + folderName.split('][')[1])
                    outputFile.append('书名：' + folderName.split('][')[0][1:] + '\n')
                    outputFile.append('作者：' + folderName.split('][')[1] + '\n')
                    if folderName[-1] != ']' and folderName.split('][')[2].find(']'):
                        print('出版：' + folderName.split('][')[2].split(']')[0])
                        print('册数：' + folderName.split('][')[2].split(']')[1])
                        outputFile.append('出版：' + folderName.split('][')[2].split(']')[0] + '\n')
                        outputFile.append('册数：' + folderName.split('][')[2].split(']')[1] + '\n')
                    elif folderName[-1] == ']':
                        print('扫者：' + folderName.split('][')[2][:-1])
                        outputFile.append('扫者：' + folderName.split('][')[2][:-1] + '\n')
                # 文件夹格式[书名][作者][出版][扫者]Vol01
                if letterCount == 8:
                    folderName = folderName
                    print('书名：' + folderName.split('][')[0][1:])
                    print('作者：' + folderName.split('][')[1])
                    print('出版：' + folderName.split('][')[2])
                    outputFile.append('书名：' + folderName.split('][')[0][1:] + '\n')
                    outputFile.append('作者：' + folderName.split('][')[1] + '\n')
                    outputFile.append('出版：' + folderName.split('][')[2] + '\n')
                    if folderName[-1] != ']' and folderName.split('][')[3].find(']'):
                        print('扫者：' + folderName.split('][')[3].split(']')[0])
                        print('册数：' + folderName.split('][')[3].split(']')[1])
                        outputFile.append('扫者：' + folderName.split('][')[3].split(']')[0] + '\n')
                        outputFile.append('册数：' + folderName.split('][')[3].split(']')[1] + '\n')
                    elif folderName[-1] == ']':
                        print('扫者：' + folderName.split('][')[3][:-1])
                        outputFile.append('扫者：' + folderName.split('][')[3][:-1] + '\n')
            for key in sorted(numberOfFileType):
                print('类型：' + key[1:] + '，数量: ' +  str(numberOfFileType[key]))
                outputFile.append('类型：' + key[1:] + '，数量: ' +  str(numberOfFileType[key]) + '\n')
            for key in fileHeight:
                print('高度：' + str(key) + ', 数量: ' + str(fileHeight[key]))
                outputFile.append('高度：' + str(key) + ', 数量: ' + str(fileHeight[key]) + '\n')      
            for key in fileWidth:
                print('宽度：' + str(key) + ', 数量: ' + str(fileWidth[key]))
                outputFile.append('宽度：' + str(key) + ', 数量: ' + str(fileWidth[key]) + '\n')   
            for key in fileWidthAndHeight:
                print('宽度和高度：' + str(key) + ', 数量: ' + str(fileWidthAndHeight[key]))
                outputFile.append('宽度和高度：' + str(key) + ', 数量: ' + str(fileWidthAndHeight[key]) + '\n')      
            print('文件数量：' + str(allFileCount))
            print('文件夹大小：' + formatFileSize(allFileSize))
            print('文件夹创建时间：' + datetime.datetime.fromtimestamp(Path(aPath).stat().st_ctime).strftime('%Y-%m-%d %H:%M:%S'))
            print('文件夹修改时间：' + datetime.datetime.fromtimestamp(Path(aPath).stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S'))
            outputFile.append('文件数量：' + str(allFileCount)+ '\n')
            outputFile.append('文件夹大小：' + formatFileSize(allFileSize) + '\n')
            outputFile.append('文件夹创建时间：' + datetime.datetime.fromtimestamp(Path(aPath).stat().st_ctime).strftime('%Y-%m-%d %H:%M:%S') + '\n')
            outputFile.append('文件夹修改时间：' + datetime.datetime.fromtimestamp(Path(aPath).stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S') + '\n')
                    
            zf = zipfile.ZipFile(str(Path(aPath).parent.joinpath(Path(aPath).name)) + '.zip', 'w', zipfile.ZIP_STORED)
            print(str(Path(aPath).parent.joinpath(Path(aPath).name)) + '.zip')
            for file in allFilelist:
                zf.write(file, str(file)[len(aPath) - len(Path(aPath).name):])
            zf.comment = ''.join(outputFile).encode('utf-8')
            zf.close()
        
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass
