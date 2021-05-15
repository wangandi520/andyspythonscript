# encoding:utf-8

import os
import zipfile
from pathlib import Path

def main():
    allFiles = os.listdir('.')
    allZIPs = []
    for file in allFiles:
        if (os.path.splitext(file)[1] == '.zip'):
            allZIPs.append(file)
    
    if not os.path.exists('cover'):
        os.system('mkdir cover')
            
    for onezip in allZIPs:
        zf = zipfile.ZipFile(onezip, 'r')
        if not (sorted(zf.namelist())[0]).endswith('/'):
            tempFile01 = sorted(zf.namelist())[0]
            newFileName = os.path.splitext(onezip)[0] + os.path.splitext(os.path.basename(tempFile01))[1]
            zf.extract(tempFile01,'cover')
            os.system('rename cover\\' + tempFile01 + ' ' + newFileName)
        else:
            tempFile02 = sorted(zf.namelist())[1]
            if tempFile02.endswith('.db'):
                tempFile02 = sorted(zf.namelist())[2]
            zf.extract(tempFile02,'cover')
            tempFiles = os.listdir('cover')
            tempAllDirs = []
            for file in tempFiles:
                if (os.path.isdir(os.path.join('cover', file))):
                    tempAllDirs.append(file)
            tempFileName = os.listdir('cover\\' + tempAllDirs[0])
            newFileName = os.path.splitext(onezip)[0] + os.path.splitext(os.path.basename(tempFile02))[1]
            tempCmd01 = 'rename "cover\\' + tempAllDirs[0] + '\\' + tempFileName[0] + '" ' + newFileName
            os.system(tempCmd01)
            tempCmd02 = 'move cover\\"' + tempAllDirs[0] + '\\' + newFileName + '" cover\\'
            os.system(tempCmd02)
            os.system('rmdir cover\\"' + tempAllDirs[0])

if __name__ == '__main__':
    main()