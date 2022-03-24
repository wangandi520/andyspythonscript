# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript


from pathlib import Path
from hashlib import sha1

import sys
import zipfile
import rarfile
import datetime

# pip install rarfile, zipfile

def formatFileSize(sizeBytes):
    # 格式化文件大小
    sizeBytes = float(sizeBytes)
    result = float(abs(sizeBytes))
    suffix = "B"
    if(result > 1024):
        suffix = "KB"
        mult = 1024
        result = result / 1024
    if(result > 1024):
        suffix = "MB"
        mult *= 1024
        result = result / 1024
    if (result > 1024):
        suffix = "GB"
        mult *= 1024
        result = result / 1024
    if (result > 1024):
        suffix = "TB"
        mult *= 1024
        result = result / 1000
    if (result > 1024):
        suffix = "PB"
        mult *= 1024
        result = result / 1024
    return format(result, '.2f') + suffix
    
    
def getSha1(filename):
    # 计算sha1
    sha1Obj = sha1()
    try:
        with open(filename, 'rb') as f:
            sha1Obj.update(f.read())
    except FileNotFoundError:
        print(str(filename) + '文件不存在')
    return sha1Obj.hexdigest()
    
    
def writeFile(aPath, filereadlines):
    # 写入md文件
    # 放在文件夹外面
    #newfile = open(aPath.parent.joinpath(aPath.name + '.md'), mode='w', encoding='UTF-8')
    # 放在文件夹里面，html格式
    newfile = open(aPath, mode='w', encoding='UTF-8')
    # markdown格式
    newfile = open(aPath, mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()  


def readFile(filename):
    # 读取文件
    try:
        with open(filename, mode='r', encoding='UTF-8') as file:
            filereadlines = file.readlines()
        for i in filereadlines:
        # 去掉空行
            if i == '\n':
                filereadlines.remove(i)
        # remove '\n' in line end
        for i in range(len(filereadlines)):
            filereadlines[i] = filereadlines[i].rstrip()
        return filereadlines 
    except FileNotFoundError:
        print(str(filename) + '文件不存在')
    
def arrayFormatToHTML(myArray):
    # 转换成html格式
    returnFileInfo = []
    returnFileInfo.append('<html><head><title>文件信息</title><style>table{width:auto;}table,td{border:1px solid #000000;table-layout:fixed;border-collapse:collapse;}table td:first-child{width:auto;}table td{min-width:100px;}a{text-decoration: none;}table tr:first-child{background-color:#eee;}tr:hover{background-color:#eee;}</style></head><body><table id="allFileTable"><tr><td>文件名</td><td>文件类型</td><td>文件大小</td><td>修改时间</td><td>压缩包内文件数量</td><td>压缩包内文件夹数量</td><td>扩展名对应的文件数量</td><td>SHA1校验码</td></tr>')
    
    for eachInfo in myArray:
        newContent = '<tr>'
        for eachString in eachInfo:
            newContent = newContent + '<td>' + str(eachString) + '</td>'
        returnFileInfo.append(newContent + '</tr>')
    returnFileInfo.append('</table></body></html>')
    return returnFileInfo
    
    
def arrayFormatToMD(myArray):
    # 转换成markdown格式
    returnFileInfo = []
    returnFileInfo.append('|文件夹名|文件类型|文件大小|修改时间|压缩包内文件数量|压缩包内文件夹数量|扩展名对应的文件数量|SHA1校验码|\n')
    returnFileInfo.append('| --- | --- | --- | --- | --- | --- | --- | --- |\n')
    
    for eachInfo in myArray:
        newContent = '|'
        for eachString in eachInfo:
            newContent = newContent + str(eachString) + '|'
        returnFileInfo.append(newContent + '\n')
    return returnFileInfo
    
def getFileInfo(directoryPath, filePath):
    # Path(filePath)
    eachFileInfo = []
    dirCount = 0
    fileCount = 0
    fileType = {}
    
    if zipfile.is_zipfile(filePath):
        zf = zipfile.ZipFile(filePath)
        for eachFile in zf.infolist():
            if eachFile.is_dir():
                dirCount = dirCount + 1
            else:
                fileCount = fileCount + 1
                if (Path(eachFile.filename).suffix not in fileType):
                    fileType[Path(eachFile.filename).suffix] = 1
                else:
                    fileType[Path(eachFile.filename).suffix] = fileType[Path(eachFile.filename).suffix] + 1
        zf.close()
    if rarfile.is_rarfile(filePath):
        rf = rarfile.RarFile(filePath)
        for eachFile in rf.infolist():
            if eachFile.is_dir():
                dirCount = dirCount + 1
            else:
                fileCount = fileCount + 1
                if (Path(eachFile.filename).suffix not in fileType):
                    fileType[Path(eachFile.filename).suffix] = 1
                else:
                    fileType[Path(eachFile.filename).suffix] = fileType[Path(eachFile.filename).suffix] + 1
        rf.close()
        
    #eachFileInfo.append(str(filePath.parent.joinpath(filePath.name)))
    eachFileInfo.append(str(filePath.relative_to(directoryPath)))
    eachFileInfo.append(filePath.suffix[1:])
    eachFileInfo.append(formatFileSize(filePath.stat().st_size))
    #eachFileInfo.append(datetime.datetime.strptime(filePath.stat().st_mtime, "%Y-%m-%d %H:%M:%S.%f"))
    eachFileInfo.append(datetime.datetime.fromtimestamp(filePath.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S'))
    
    eachFileInfo.append(fileCount)
    eachFileInfo.append(dirCount)
    tempFileType = ''
    for key in sorted(fileType):
        tempFileType = tempFileType + key[1:] + '=' + str(fileType[key]) + ', '
    eachFileInfo.append(tempFileType[:-2])
    eachFileInfo.append(getSha1(filePath))
    print(eachFileInfo)
    return eachFileInfo
    

def checkSha1(filePath):
    # 当前文件夹名内有文件夹.sha1的话，就开始校验
    fileName = ''
    getFileContent = ''
    if (Path(filePath)) == (Path.cwd()):
        getFileContent = readFile(Path.cwd().name + '.sha')
    else:
        getFileContent = readFile(Path(filePath).joinpath(Path(filePath).name + '.sha'))
    print()
    for eachFile in getFileContent:
        tempSha1 = eachFile.split(' *')[0]
        tempFileName = eachFile.split(' *')[1]
        if (getSha1(Path(filePath).joinpath(tempFileName)) == tempSha1):
            print('校验成功 ' + tempFileName)
        else:
            print('!校验失败 ' + tempFileName)

def main(inputPath): 
    del inputPath[0]
    if (len(inputPath) == 0):
        inputPath = [Path.cwd()]
    # 所有信息
    # 每个文件的信息：|文件夹名|文件类型|文件大小|压缩包内文件数量|压缩包内文件夹数量|扩展名对应的文件数量|SHA1校验码
    allFileInfo = []
    allFileSha1 = []
    #转换成html = True, markdown = False
    fileType = True
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'): 
                if Path.is_file(Path(file)):
                    tempFileInfo = getFileInfo(Path(aPath), file)
                    allFileInfo.append(tempFileInfo)
                    allFileSha1.append(tempFileInfo[7] + ' *' + tempFileInfo[0] + '\n')  
            writeFile(Path(aPath).joinpath(Path(aPath).name + '.sha'), allFileSha1)
            if fileType:
                writeFile(Path(aPath).joinpath(Path(aPath).name + '.html'), arrayFormatToHTML(allFileInfo))
            else:
                writeFile(Path(aPath).joinpath(Path(aPath).name + '.md'), arrayFormatToMD(allFileInfo))
            
            sha1FileExisted = False
            for fileName in allFileInfo:
                if (Path(aPath).name + '.sha' in fileName[0]) :
                    sha1FileExisted = True
                    break
            if sha1FileExisted:
                checkSha1(aPath)
      
        
        if Path.is_file(Path(aPath)) and Path(aPath).suffix == '.sha':
            
            getFileContent = readFile(Path(aPath))
            
            for eachFile in getFileContent:
                tempSha1 = eachFile.split(' *')[0]
                tempFileName = eachFile.split(' *')[1]
                if (getSha1(Path(aPath).parent.joinpath(tempFileName)) == tempSha1):
                    print('校验成功 ' + tempFileName)
                else:
                    print('!校验失败 ' + tempFileName)
                    
    print()
    print('发布网址 https://github.com/wangandi520/andyspythonscript')
    input('按回车退出')
    
if __name__ == '__main__':
    try:
        main(sys.argv)
        # if len(sys.argv) >= 2:
            # main(sys.argv)
        # else:
            # checkSha1(Path(sys.argv[0]).parent)
    except IndexError:
        pass