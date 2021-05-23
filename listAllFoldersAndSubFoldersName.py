# encoding:utf-8

import os

def writefile(filereadlines):
    newfile = open('listAllFoldersAndSubFoldersName.txt', mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()     
    
def main():
    allFolders = []
    for (root, dirs, files) in os.walk('.'):
        if root.startswith('.\\'):
            allFolders.append(root[2:] + '\n')
    writefile(allFolders)
    
if __name__ == '__main__':
    main()