## python处理脚本几个

### 说明：

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

### allFolderFilesRename.py

同级目录下有数个文件夹，每个文件夹里数个文件，没有二级文件夹。

重命名的格式，会自动识别扩展名:

第一个文件夹的文件夹01_001.jpg，到01_030.jpg，如果一共30个文件，扩展名是jpg的话

第二个文件夹的文件夹02_001.jpg，到02_030.jpg，如果一共30个文件，扩展名是jpg的话

以此类推

如果把allFolderFilesRename.py改名其他名字，如123_.py，那文件名就是123_01_01.jpg

第一个文件夹的数字，请修改dirCount

### 使用前请备份，防止文件名不符合你的需求