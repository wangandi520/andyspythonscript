# encoding:utf-8

import os

def main():
    allFiles = os.listdir('.')
    allTXTs = []
    for file in allFiles:
        if (file != 'renameToTC.py'):
            allTXTs.append(file)
    
    oldName = allTXTs[0]
    newName = ''
    for i in oldName:
        if i == '[':
            newName = newName + '[[]'
        elif i == ']':
            newName = newName + '[]]'
        else:
            newName = newName + i
    newName = newName + 'Vol_[C]'
    os.system('rename "' + oldName + '" "' + newName + '"')
    #print(newName)
        
if __name__ == '__main__':
    main()