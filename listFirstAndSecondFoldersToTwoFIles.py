# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

import os

def writefile(filereadlines, fileName):
    newfile = open(fileName, mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()     
    
def main():
    firstFoldersName = '作者'
    firstFolders = []
    secondFoldersName = '作品'
    secondFolders = []
    for (root, dirs, files) in os.walk('.'):
        newroot = root[2:]
        if newroot and not ('\\' in newroot):
            firstFolders.append(newroot + '\n')
        if newroot and ('\\' in newroot):
            loc = newroot.find('\\') + 1
            secondFolders.append(newroot[loc:] + '\n')
    writefile(firstFolders, firstFoldersName + '.txt')
    writefile(secondFolders, secondFoldersName + '.txt')
    
if __name__ == '__main__':
    main()