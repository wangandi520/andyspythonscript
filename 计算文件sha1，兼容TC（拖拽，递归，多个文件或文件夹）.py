# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
from hashlib import sha1
import sys

def getSha1(filename):
    sha1Obj = sha1()
    with open(filename, 'rb') as f:
        sha1Obj.update(f.read())
    return sha1Obj.hexdigest()

def formatFileSize(sizeBytes):
    sizeBytes = float(sizeBytes)
    result = float(abs(sizeBytes))
    suffix = "B";
    if(result>1024):
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

def writefile(filereadlines, inputPath):
    # 文件名是.txt格式还是其他
    fileSuffix = '.sha'
    # txt放到这个文件外面 = 1 还是里面 = 0
    setFileLocation = 0
    
    if setFileLocation:
        newfile = open(Path(inputPath).parent.joinpath(inputPath.name + fileSuffix), mode='a', encoding='UTF-8')
    else:
        newfile = open(Path(inputPath).joinpath(inputPath.name + fileSuffix), mode='a', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()   
    
def main(inputPath):
    # 是否显示文件大小，True，False
    showOrNoFileSize = False
    
    del inputPath[0]
    for aPath in inputPath:
        allFileInfo = []
        if Path.is_file(Path(aPath)):
            fileSha1 = getSha1(aPath)
            fileSize = Path(aPath).stat().st_size
            fileName = Path(aPath).name
            showFileSize = formatFileSize(fileSize)
            if showOrNoFileSize:
                allFileInfo.append(fileSha1 +  ' ' + fileName + ' ' + showFileSize + '\n')
            else:
                allFileInfo.append(fileSha1 +  ' ' + fileName + '\n')
            writefile(allFileInfo, Path(aPath).parent)
            
        if Path.is_dir(Path(aPath)):
            allDirInfo = []
            for aFile in Path(aPath).glob('**/*'): 
                if Path.is_file(aFile):
                    fileSha1 = getSha1(aFile)
                    fileSize = Path(aFile).stat().st_size
                    fileName = Path(aFile).name
                    showFileSize = formatFileSize(fileSize)
                    if showOrNoFileSize:
                        allDirInfo.append(fileSha1 +  ' *' + fileName + ' ' + showFileSize + '\n')
                    else:
                        allDirInfo.append(fileSha1 +  ' *' + fileName + '\n')
            writefile(allDirInfo, Path(aPath))
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass