# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import zipfile
import rarfile

def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            withSubDir = []
            noSubDir = []
            for file in Path(aPath).glob('*.rar'):
                if rarfile.is_rarfile(file):
                    rf = rarfile.RarFile(file)
                    noDir = True
                    print(rf.namelist())
                    for eachFile in rf.infolist():
                        if eachFile.is_dir():
                            noDir = False
                            if file not in withSubDir:
                                withSubDir.append(file)
                            break
                    if noDir and (file not in noSubDir):
                        noSubDir.append(file)
                    rf.close()
                                        
            for file in Path(aPath).glob('*.zip'):
                if zipfile.is_zipfile(file):
                    zf = zipfile.ZipFile(file)
                    noDir = True
                    for eachFile in zf.infolist():
                        if eachFile.is_dir():
                            noDir = False
                            if file not in withSubDir:
                                withSubDir.append(file)
                            break
                    if noDir and (file not in noSubDir):
                        noSubDir.append(file)
                    zf.close()
            
            withSubDirPath = Path(aPath).joinpath(Path('包含文件夹'))
            noSubDirPath = Path(aPath).joinpath(Path('仅包含文件'))
            if not withSubDirPath.exists() and withSubDir:
                Path.mkdir(withSubDirPath)
            if not noSubDirPath.exists() and noSubDir:
                Path.mkdir(noSubDirPath)
                
            for file in withSubDir:
                Path(file).replace(withSubDirPath.joinpath(file.name))
            for file in noSubDir:
                Path(file).replace(noSubDirPath.joinpath(file.name))
        
        if Path.is_file(Path(aPath)):
            withSubDir = []
            noSubDir = []
            file = Path(aPath)
            if rarfile.is_rarfile(file):
                rf = rarfile.RarFile(file)
                noDir = True
                print(rf.namelist())
                for eachFile in rf.infolist():
                    if eachFile.is_dir():
                        noDir = False
                        if file not in withSubDir:
                            withSubDir.append(file)
                        break
                if noDir and (file not in noSubDir):
                    noSubDir.append(file)
                rf.close()
                                        
            if zipfile.is_zipfile(file):
                zf = zipfile.ZipFile(file)
                noDir = True
                for eachFile in zf.infolist():
                    if eachFile.is_dir():
                        noDir = False
                        if file not in withSubDir:
                            withSubDir.append(file)
                        break
                if noDir and (file not in noSubDir):
                    noSubDir.append(file)
                zf.close()
            
            withSubDirPath = Path(aPath).parent.joinpath(Path('包含文件夹'))
            noSubDirPath = Path(aPath).parent.joinpath(Path('仅包含文件'))
            if not withSubDirPath.exists() and withSubDir:
                Path.mkdir(withSubDirPath)
            if not noSubDirPath.exists() and noSubDir:
                Path.mkdir(noSubDirPath)
                
            if withSubDir:
                Path(file).replace(withSubDirPath.joinpath(file.name))
            if noSubDir:
                Path(file).replace(noSubDirPath.joinpath(file.name))
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass