# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import sqlite3

def formatFileSize(sizeBytes):
    sizeBytes = float(sizeBytes)
    result = float(abs(sizeBytes))
    suffix = "B";
    if(result>1024):
        suffix = "KB"
        mult = 1024
        result = result / 1024
    if(result > 1024):
        suffix = "MB"
        mult *= 1024
        result = result / 1024
    if (result > 1024) :
        suffix = "GB"
        mult *= 1024
        result = result / 1024
    if (result > 1024) :
        suffix = "TB"
        mult *= 1024
        result = result / 1000
    if (result > 1024) :
        suffix = "PB"
        mult *= 1024
        result = result / 1024
    return format(result,'.2f') + suffix
        
def writefile(outputFile, path):
    myConnect = sqlite3.connect(path.name + '.db')
    #myCursor = myConnect.cursor()
    myConnect.execute('''CREATE TABLE book(id INTEGER PRIMARY KEY AUTOINCREMENT, filename text, filepath text, filesize text)''')
    myConnect.executemany('INSERT INTO book(filename, filepath, filesize) VALUES (?,?,?)', outputFile)
    myConnect.commit()
    myConnect.close()   
    
def main(inputPath):
    # 绝对路径 = 1， 还是相对路径 = 0
    absolutePath = 0
    # 文件夹名显示完整的相对路径 = 1，还是只显示一层文件夹名
    showAllFolderAddr = 1
    mypath = Path(inputPath)
    # fileCount = 0
    # fileSizeCount = 0
    # folderCount = 0
    outputFile = []
    
    for file in mypath.glob('**/*'):
        loc = file.parent.joinpath(file.name)
        print(loc)
        showName = str(file.name)
        if absolutePath:
            showAddr = str(loc)
        else:
            showAddr = str(file.relative_to(mypath))  
        if Path.is_dir(file):
            #folderCount = folderCount + 1
            if showAllFolderAddr:
                showName = showAddr     
        # if Path.is_file(file):
            # fileCount = fileCount + 1
        fileSize = Path(loc).stat().st_size
        outputFile.append((showName, showAddr, formatFileSize(fileSize)))
   
    #info = [fileCount, folderCount, formatFileSize(fileSizeCount)]
    writefile(outputFile, mypath)
    
if __name__ == '__main__':
    try:
        if len(sys.argv) == 1:
            main('.')
        elif len(sys.argv) == 2:
            main(sys.argv[1])
    except IndexError:
        pass