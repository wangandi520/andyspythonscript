# encoding:utf-8

import os

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
        
def writefile(filereadlines):
    newfile = open('index.html', mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()     
    
def main():
    # 是否显示文件大小，show file size = 1, no file size = 0
    showFileSize = 1
    # 显示完整地址还是只显示文件名，show all address = 1, only show file name = 0
    showAllAddress = 1
    # 第一栏的宽度，first column width
    columnWidth = 550
    # 显示边框，show table border = 1, no border = 0
    showTableBorder = 1
    # 显示第一行，show first line = 1, no first line = 0(file name, sha1, file size)
    showFirstLine = 1
    # 是否显示处理过程
    showProcessDetails = 1
    
    outputFile = '<html><head><title>index.html</title><style>table,td{border:' + str(showTableBorder) +'px solid #000000;table-layout:fixed;border-collapse:collapse;}a{text-decoration: none;}td{width:100px;}table tr td:first-child{width:' + str(columnWidth) +'px}tr:hover{background-color:#eee;}</style><script type="text/javascript" language="JavaScript">function onSearch(){searchContent = document.getElementById(\'mySearch\').value;var storeId = document.getElementById(\'allFileTable\');var rowsLength = storeId.rows.length;for(var i=1;i<rowsLength;i++){var searchText = storeId.rows[i].cells[0].innerHTML;if(searchText.match(searchContent) || searchText.toUpperCase().match(searchContent.toUpperCase())){storeId.rows[i].style.display=\'\';}else{storeId.rows[i].style.display=\'none\';}}}</script></head><body><div>\n<table id="allFileTable">'
    if showFirstLine:
        if showFileSize:
            outputFile = outputFile + '<tr><td><span id="fileNameID"></span><input type="text" id="mySearch" onkeyup="onSearch()" placeholder="搜索..."></td><td>Size</td></tr>'
        else:
            outputFile = outputFile + '<tr><td>File name:<input type="text" id="mySearch" onkeyup="onSearch()" placeholder="搜索..."></td></tr>'
    fileCount = 0
    fileSizeCount = 0
    folderCount = 0
    for root, dirs, files in os.walk(".", topdown=False):
        for eachdir in dirs:
            folderCount = folderCount + 1
        for name in files:
            fileCount = fileCount + 1
            loc = os.path.join(root, name)[2:]
            if showProcessDetails:
                print(loc)
            if showAllAddress:
                showName = loc
            else:
                showName = name
            if showFileSize:
                fileSize = formatFileSize(os.path.getsize(loc))
                fileSizeCount = fileSizeCount + os.path.getsize(loc)
                outputFile = outputFile + '<tr><td><a href="' + loc + '">' + showName + '</td><td>' + fileSize + '</a></tr>\n'
            else:
                outputFile = outputFile + '<tr><td><a href="' + loc + '">' + loc + '</a></td></tr>\n'
    outputFile = outputFile + '</td></table></div></body></html>'
    outputFile = outputFile + '<script type="text/javascript" language="JavaScript">document.getElementById("fileNameID").innerHTML = "Name (' + str(fileCount) + ' files in ' + str(folderCount) + ' folders'
    if showFileSize:
        outputFile = outputFile + ', '+ formatFileSize(fileSizeCount)
    outputFile = outputFile +  ') ";</script>'
    writefile(outputFile)
    
if __name__ == '__main__':
    main()