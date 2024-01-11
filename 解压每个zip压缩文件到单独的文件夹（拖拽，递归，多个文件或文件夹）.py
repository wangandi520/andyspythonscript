# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import os
import zipfile

def unzipEachFile(eachFilePath):
    print('正在解压缩：' + eachFilePath.name)
    # 创建ZipFile对象并打开zip文件
    with zipfile.ZipFile(eachFilePath, 'r') as myzipfile:
        # 获取所有文件列表
        eachFileList = myzipfile.namelist()
        for eachFile in eachFileList:
            newZipFilePath = eachFilePath.parent.joinpath(eachFilePath.stem)
            # 新建文件夹
            if not newZipFilePath.exists():
                Path.mkdir(newZipFilePath)
            # 将文件从zip文件中提取指定目录
            myzipfile.extractall(newZipFilePath)

def main(inputPath):
    del inputPath[0]
    # 只解压缩zip格式
    mySuffix = ['.zip']
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for eachFilePath in Path(aPath).glob('**/*'):
                if eachFilePath.suffix.lower() in mySuffix:
                    unzipEachFile(eachFilePath)    
        if Path.is_file(Path(aPath)):
            if Path(aPath).suffix.lower() in mySuffix:
                unzipEachFile(Path(aPath))  

        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            print('共拖拽' + str(len(sys.argv) - 1) + '个文件（夹），未包含子文件（夹）')
            main(sys.argv)
    except IndexError:
        pass