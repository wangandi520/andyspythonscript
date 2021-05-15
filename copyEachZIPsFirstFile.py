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
            zf.extract(tempFile01,'cover')
        else:
            print('Not support subdir.')
            # tempFile02 = sorted(zf.namelist())[1]
            # print(sorted(zf.namelist())[0].encode('cp437').decode('gbk'))
            # print(sorted(zf.namelist())[1].encode('cp437').decode('gbk'))
            # print(os.path.basename(tempFile02))
            # newFileName = os.path.splitext(onezip)[0] + os.path.splitext(os.path.basename(tempFile02))[1]
            # zf.extract(tempFile02,'cover')
            # os.system('rename ' + tempFile02.encode('cp437').decode('gbk') + newFileName)
            # print('rename "' + tempFile02.encode('cp437').decode('gbk') + '" ' + newFileName)
    
        
if __name__ == '__main__':
    main()