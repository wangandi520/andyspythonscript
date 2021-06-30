## 几个python脚本

## 说明：

### copyEachFoldersFirstFile.py

会把同级目录下的所有文件夹的第一个文件复制到cover文件夹内

用途：复制出漫画封面

### copyEachZIPsFirstFile.py

会把同级目录下的所有zip的第一个文件复制到cover文件夹内

用途：复制出漫画封面

### renameToTC.py

会把[换成[[]，]换成[]]
例如
[頭文字D_InitialD][重野秀一][尖端]
变成
[[]頭文字D_InitialD[]][[]重野秀一[]][[]尖端[]]Vol_[C]

用途：total commander 中ctrl+m批量重命名多卷漫画使用

输入输出都在renameToTC.txt里

### allFolderFilesRename.py

同级目录下有数个文件夹，每个文件夹里数个文件，没有二级文件夹。

重命名的格式，会自动识别扩展名:

第一个文件夹的文件夹01_001.jpg，到01_030.jpg，如果一共30个文件，扩展名是jpg的话

第二个文件夹的文件夹02_001.jpg，到02_030.jpg，如果一共30个文件，扩展名是jpg的话

以此类推

如果把allFolderFilesRename.py改名其他名字，如123_.py，那文件名就是123_01_01.jpg

第一个文件夹的数字，请修改dirCount

### classifyIfSubDirInZIPRAR.py

如果压缩文件夹rar，zip里包含仅一个文件夹，就移动压缩文件到withSubDir文件夹

如果不包含文件夹，就移动到noSubDir文件夹

### listAllFoldersAndSubFoldersName.py

把和py文件当前目录下所有文件夹和子文件夹的名字输出到listAllFoldersAndSubFoldersName.txt中

### listFirstAndSecondFoldersToTwoFIles.py

把和py文件当前目录的同级文件夹名字，输出到firstFoldersName.txt中
把和py文件当前目录的所有子文件夹名字，输出到secondFoldersName.txt中

## generateFileNameAndLink.py

当前目录下所有文件，生成文件夹名.html，可搜索，点击Name回到首页

main()函数前几行可以进行一些自定义设置

文件夹名加粗显示，支持只显示文件夹名

可进行的设置：显示完整地址还是只显示文件名，第一栏的宽度，是否显示边框，是否显示第一行，是否显示处理过程，键盘按键抬起立刻搜索还是按回车搜索，相对路径还是绝对路径，显示文件夹和文件还是只显示文件夹，是否显示文件大小，点击文件夹是搜索包含这个文件夹名的所有路径还是跳转到这个文件夹

generateFileNameAndLink(Support Simplified Chinese and Traditional Chinese Searching).py，自动搜索中文简体和繁体

支持拖拽文件夹到py文件

## renameEFolderNameToFile.py

使用前请备份，不符合以下格式的不能用

文件夹可以是以"完]"结尾的，或其他，比如"[名字][作者][出版社][扫者][10完]"

文件名结尾必须是"Vol_两位数字.zip"这样的格式，比如"ABCDEVol_01.zip"

只支持拖拽操作，把文件夹拖到py文件上

## 把文件夹内的文件重命名成文件夹名+Vol_序号的格式（拖拽，仅多个文件夹）.py

使用前请备份，不符合以下格式的不能用

文件夹可以是以"完]"结尾的，或其他，比如"[名字][作者][出版社][扫者][10完]"

以"完]"结尾，最后一个文件名会加上" End"

文件名无要求

只支持拖拽操作，把文件夹拖到py文件上

文件夹里可以是文件，或者文件夹，不支持混合

会生成日志和恢复文件名的bat文件，不过不想生成，就修改文件里的createLogAndRecover = False

## 交换文件或文件夹名前两个[]的内容（拖拽，多个文件或文件夹）.py

把文件夹或文件名字中前两个[]的内容交换位置，支持多个文件夹或文件一起拖拽

## 交换文件名最后[]和Vol_XX（拖拽，多个文件夹，文件名格式[][][][]Vol_XX）.py

把文件夹或文件名字中最后[]和Vol_XX的内容交换位置，文件名格式[][][][]Vol_XX，支持多个文件夹或文件一起拖拽

## remove.1234FileInFolder.py

把文件夹内后缀名是.1234文件，去掉.1234，支持多个文件夹或文件一起拖拽

## removeFilenameBefore-.py

文件夹名是 xxx - xxx.xxx的格式时，删除前面的xxx和 - ，只剩后面的xxx.xxx，拖拽文件夹到py上运行

## 文件夹和二级文件名简体转繁体（拖拽，多个文件或文件夹）.py
## 文件夹和二级文件名繁体转简体（拖拽，多个文件或文件夹）.py

拖拽文件或文件夹到py上，被拖拽的文件夹和里面的二级目录的文件夹和文件名都会被转换

需要pip install opencc-python-reimplemented

## 文件和文件夹夹繁体转简体，不转换二级目录（拖拽，仅文件夹）.py
## 文件和文件夹名简体转繁体，不转换二级目录（拖拽，仅文件夹）.py

拖拽文件或文件夹到py上，二级目录的文件夹和文件名不会被转换

需要pip install opencc-python-reimplemented

## 解压双重分割打包的RAR（拖拽，仅多个文件夹，需要UnRAR.exe）.py

识别两层rar的文件结尾.part1.rar

# 使用前请备份，防止文件名不符合你的需求