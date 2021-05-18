# encoding:utf-8

import os
import zipfile
import rarfile

def main():
    allFiles = os.listdir('.')
    allZIPs = []
    allRARs = []
    for file in allFiles:
        if (os.path.splitext(file)[1] == '.zip'):
            allZIPs.append(file)
        if (os.path.splitext(file)[1] == '.rar'):
            allRARs.append(file)    
            
    if not os.path.exists('noSubDir'):
        os.system('mkdir noSubDir')
    if not os.path.exists('withSubDir'):
        os.system('mkdir withSubDir')
            
    for onezip in allZIPs:
        zf = zipfile.ZipFile(onezip, 'r')
        if zf.namelist()[0].endswith('/'):
            zf.close()
            inputCMD = 'move "' + onezip + '" withSubDir'
            os.system(inputCMD)
        else:
            zf.close()
            inputCMD = 'move "' + onezip + '" noSubDir'
            os.system(inputCMD)
            
    for onerar in allRARs:
        rf = rarfile.RarFile(onerar, 'r')
        if rf.namelist()[-1].endswith('/'):
            rf.close()
            inputCMD = 'move "' + onerar + '" withSubDir'
            os.system(inputCMD)
        else:
            rf.close()
            inputCMD = 'move "' + onerar + '" noSubDir'
            os.system(inputCMD)

if __name__ == '__main__':
    main()