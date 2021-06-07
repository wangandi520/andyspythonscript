# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

import os.path

def main():
    allFiles = os.listdir('.')
    allDirs = []
    for file in allFiles:
        if (os.path.isdir(file) and len(os.listdir(file)) > 0) and file != 'cover':
            allDirs.append(file)
    
    if not os.path.exists('cover'):
        os.system('mkdir cover')
        
    for dir in allDirs:
        tempFilesName = os.listdir(dir)[0]
        imputCmd = 'copy "' + dir + '\\' + tempFilesName + '" cover\\' + dir + os.path.splitext(tempFilesName)[1]
        os.system(imputCmd)
        
if __name__ == '__main__':
    main()