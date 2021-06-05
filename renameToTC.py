# encoding:utf-8

import os

def readfile():
    with open('renameToTC.txt', mode='r', encoding='UTF-8') as file:
        filereadlines = file.readlines()
    output = []
    for i in filereadlines:
        if not i.startswith('[[]') and not i == '\n':
            output.append(i)
    for i in range(len(output)):
        output[i] = output[i].rstrip()
    return output
    
def writefile(filereadlines):
    newfile = open('renameToTC.txt', mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()
    
def main():
    readTxts = readfile()
    outTxts = []
    print(readTxts)
    for txt in readTxts:
        oldName = txt
        newName = ''
        outTxts.append(oldName + '\n\n')
        for i in oldName:
            if i == '[':
                newName = newName + '[[]'
            elif i == ']':
                newName = newName + '[]]'
            else:
                newName = newName + i
        if i.startswith('[[]'):
            newName = newName + 'Vol_[C]'
        outTxts.append(newName + '\n\n')
    writefile(outTxts)
        
if __name__ == '__main__':
    main()