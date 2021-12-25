# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

import time
import datetime
import calendar

def writefile(filereadlines):
    fileName = filereadlines[0][0:5] + '.txt'
    newfile = open(fileName, mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()  
    
def main():
    setYear = 2021
    myDate = datetime.date(setYear,1,1)
    output = []
    # 2021年01月01日
    while myDate.strftime("%Y") == str(setYear):
        output.append(myDate.strftime("%Y年%m月%d日"))
        output.append('\n\n\n')
        myDate = myDate+datetime.timedelta(days =+ 1)
    writefile(output)
        
if __name__ == '__main__':
    main()