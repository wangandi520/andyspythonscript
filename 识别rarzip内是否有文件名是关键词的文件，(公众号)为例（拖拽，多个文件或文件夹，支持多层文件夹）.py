# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import os
import zipfile
import rarfile

def main(inputPath):
    del inputPath[0]
    # 设置你的关键词
    keyword = '公众号'
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if file.suffix.lower() == '.rar' and rarfile.is_rarfile(file):
                    rf = rarfile.RarFile(file)
                    for eachFile in rf.namelist():
                        if keyword in eachFile:
                            print(file)
                    rf.close()
                if file.suffix.lower() == '.zip' and zipfile.is_zipfile(file):
                    zf = zipfile.ZipFile(file)                        
                    for eachFile in zf.namelist():
                        try:
                            eachFile = eachFile.encode('cp437').decode('gbk')
                        except:
                            eachFile = eachFile.encode('utf-8').decode('utf-8')
                        if keyword in eachFile:
                            print(file)
                    zf.close()
                if keyword in file.name:
                    print(file)
                            
        if Path.is_file(Path(aPath)):
            file = Path(aPath)
            if file.suffix.lower() == '.rar' and rarfile.is_rarfile(file):
                rf = rarfile.RarFile(file)
                for eachFile in rf.namelist():
                    if keyword in eachFile:
                        print(file)
                rf.close()
                                        
            if file.suffix.lower() == '.zip' and zipfile.is_zipfile(file):
                zf = zipfile.ZipFile(file)
                for eachFile in zf.namelist():
                    try:
                        eachFile = eachFile.encode('cp437').decode('gbk')
                    except:
                        eachFile = eachFile.encode('utf-8').decode('utf-8')
                    if keyword in eachFile:
                        print(file)
                zf.close()
            if keyword in file.name:
                print(file)
    print('\n')
    os.system('pause')
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass