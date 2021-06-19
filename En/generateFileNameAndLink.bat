@echo off
setlocal enabledelayedexpansion

:: https://github.com/wangandi520/andyspythonscript

echo ^<html^>^<head^>^<title^>index.html^</title^>^<meta charset="gb2312"^>> index.html
echo ^<style^>body{width:90%%;}table,td{border:1px solid #000000;table-layout:fixed;border-collapse:collapse;}a{color:#000000;text-decoration: none;}td{width:10%%;}table tr td:first-child{width:80%%;}table tr:first-child{background-color:#eee;}tr:hover{background-color:#eee;}^</style^>>> index.html
echo ^<script type="text/javascript" language="JavaScript"^>function onSearch(){searchContent = document.getElementById("mySearch").value;var storeId = document.getElementById("allFileTable");var rowsLength = storeId.rows.length;for(var i=1;i^<rowsLength;i^+^+){var searchText = storeId.rows[i].cells[0].innerHTML;if(searchText.match(searchContent) ^|^| searchText.toUpperCase().match(searchContent.toUpperCase())){storeId.rows[i].style.display="";}else{storeId.rows[i].style.display="none";}}}^</script^>>> index.html
echo ^</head^>^<body^>^<div^>^<table id="allFileTable"^>>> index.html
echo ^<tr^>^<td^>^<span id="fileNameID"^>Name ^</span^>^<input type="text" id="mySearch" onkeyup="onSearch()" placeholder="搜索..."^>^</td^>^</tr^>>> index.html
set str=%~dp0%
:next
if not "%str%"=="" (
	set /a num+=1
	set "str=%str:~1%"
	goto next
)
(for /f "eol=.tokens=* delims=" %%i in ('dir /b/s/a-d') do (
set m=%%i
echo ^<tr^>^<td^>^<a href=^"!m:~%num%!^"^>!m:~%num%!^</a^>^</td^>^</tr^>
))>>index.html
echo ^</table^>^</div^>^</body^>^</html^>>> index.html