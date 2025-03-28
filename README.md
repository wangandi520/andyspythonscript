## 使用前请备份，防止不符合你的需求

## Please  backup, make sure it is your need.

## 相关博客文章

[舒适阅读电子书和漫画](https://andi.wang/2021/03/16/%E8%88%92%E9%80%82%E9%98%85%E8%AF%BB%E7%94%B5%E5%AD%90%E4%B9%A6%E5%92%8C%E6%BC%AB%E7%94%BB)

## 注意事项

仅在windows下使用，only works in Windows

请先备份你的文件，使用后确实符合你的要求后再批量应用

安装所有需要的pip包：pip install -r requirement.txt

更新pip包：pip install --upgrade

拖拽：拖文件或文件到这个py文件上

递归：脚本对文件夹和所有子文件和文件夹都有效

部分脚本PyQt版[https://github.com/wangandi520/andyspyqtscript](https://github.com/wangandi520/andyspyqtscript)

## 说明：

使用前请先安装python[https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe](https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe)

官方网站[https://www.python.org/](https://www.python.org/)

别在baidu搜索或别的不明网站下载，谨防流氓软件


### 根据rarzip文件是否包含文件夹分类（拖拽，多个文件或文件夹）.py

sort .rar and .zip into two type:

1.contain one or more folders. 2.only contain files

把zip，rar文件分成2类并放入对应的文件夹里

1.包含一个或多个二级文件夹。2.仅包含文件的。

需要，pip install rarfile

### 生成所有子文件目录到文件夹名.txt（拖拽，仅多个文件夹）.py

get all file names in .txt 

把和py文件当前目录下所有文件夹和子文件夹的名字（默认相对路径，可选绝对路径）输出到文件夹名.txt中

### 生成目录.html，支持搜索，简繁转换（拖拽，仅一个文件夹）.py

generate .html file of all file in folders

适用于搜索，分享，查看所有的库存资源

拖拽文件夹到py文件，被拖拽的目录下的所有文件，生成文件夹名.html，可搜索，点击Name回到首页

main()函数前几行可以进行一些自定义设置，文件夹名加粗显示

可进行的设置：显示完整地址还是只显示文件名，是否显示处理过程，键盘按键抬起立刻搜索还是按回车搜索，相对路径还是绝对路径，显示文件夹和文件还是只显示文件夹，是否显示文件大小，点击文件夹是搜索包含这个文件夹名的所有路径还是跳转到这个文件夹

自动搜索中文简体和繁体，可显示搜索结果的文件和文件夹的数量和总大小

html后加?search=关键词，打开网页时后自动显示搜索结果，例如1.html?search=伊藤润二

支持排除关键词，文件名中有关键词的文件不会写到html里，文件45行，keyWords = ['关键词1','关键词2','关键词3']

同类软件推荐[Snap2HTML](https://rlvision.com/snap2html/about.php)

### 文件名重命名成文件夹名+Vol_序号的格式（拖拽，仅多个文件夹）.py

rename files in folder

**适用于已排序好的需要重命名的文件，拖拽文件夹拖到py文件上**

使用把文件夹内的文件重命名成文件夹名+Vol_序号的格式（拖拽，仅多个文件夹）.py

文件夹名的格式要符合"[书名][作者][出版社][扫者][10完]"，里面的文件会重命名成"[书名][作者][出版社][扫者]Vol_XX.XXX"的形式

以"完]"或"全]"结尾的，最后一个文件名会加上" End"，以"未]"结尾或其他结尾的则不加

按文件夹名批量重命名已排序好的文件，文件名无要求，但顺序要对

01,02,03......09,10可以。1,2,3......9,10这样顺序会出错

文件夹里可以是文件，或者文件夹，不支持混合

会生成日志和恢复文件名的bat文件，不过不想生成，就修改文件里的createLogAndRecover = False

### 文件名前两个[]的内容交换（拖拽，多个文件或文件夹）.py

switch two [] content in file names

文件（夹）名格式[书名][作者][出版社][扫者]Vol_XX，会重命名成"[书名][作者][出版社]Vol_XX[扫者]"

支持多个文件夹或文件一起拖拽

### 文件名最后[]和Vol_XX交换（拖拽，多个文件夹，文件名格式[][][][]Vol_XX）.py

switch Vol_xx and last []

**把[扫者]放在Vol之后，适用于多个扫者的情况下卷的顺序错乱的情况，拖拽文件（夹）拖到py文件上**

把文件（夹）名中最后[]的内容和Vol_XX交换位置

适用于多个扫者的情况下卷的顺序错乱的情况

把文件夹或文件名字中最后[]和Vol_XX的内容交换位置，文件名格式[][][][]Vol_XX，支持多个文件夹或文件一起拖拽

### 文件名结尾的.1234删除（拖拽，多个文件或文件夹）.py

remove .1234 in file name

把文件夹内后缀名是.1234文件，去掉.1234，支持多个文件夹或文件一起拖拽

### 文件名简繁体转换（拖拽，递归，多个文件或文件夹）.py.py

rename file between simplfied chinese and tradition chinese

拖拽文件或文件夹到py上，被拖拽的文件夹和里面所有的文件夹和文件名都会被转换

文件内设置简繁转换方向

需要pip install opencc-python-reimplemented

### 文件名识别作品名作者名并新建文件夹移动文件（拖拽，仅多个文件夹，文件夹名格式[作品][作者]XX）.py

mkdir folder/subfolder in old folder name [subfolder][folder]

文件名格式[书名][作者]XX.XX，新建文件夹名是作者（无方括号），二级文件夹名是书名（无方括号），被拖拽的文件会被移动到作品名文件夹里

### 文件名识别作品名作者名并新建文件夹移动文件（拖拽，仅多个文件夹，可简繁转换，文件夹名格式[作品][作者]XX）.py

mkdir folder/subfolder in old folder name [subfolder][folder], rename file between simplfied chinese and tradition chinese

文件夹名格式[书名][作者]XX，新建文件夹名是作者（无方括号），二级文件夹名是书名（无方括号），被拖拽的文件夹里的文件会被移动到作品名文件夹里

需要pip install opencc-python-reimplemented

### 文件名识别作品名作者名并新建文件夹移动文件（拖拽，仅多个文件，文件名格式[作品][作者]XX）.py

mkdir folder/subfolder in old file name [subfolder][folder]

文件夹名格式[书名][作者]XX，新建文件夹名是作者（无方括号），二级文件夹名是书名（无方括号）

被拖拽的文件夹里的文件会被移动到作品名文件夹里

### 文件名识别作品名作者名并新建文件夹移动文件（拖拽，仅多个文件，可简繁转换，文件名格式[作品][作者]XX）.py

mkdir folder/subfolder in old file name [subfolder][folder], rename file between simplfied chinese and tradition chinese

文件名格式[书名][作者]XX.XX，新建文件夹名是作者（无方括号），二级文件夹名是书名（无方括号），被拖拽的文件会被移动到作品名文件夹里

可识别文件名以[Comic]开头

需要pip install opencc-python-reimplemented

### 复制出RAR或ZIP文件中的第一个文件（拖拽，多个文件或文件夹）.py

copy first file in .rar or .zip

需要同级目录下UnRAR.exe 或 pip install unrar

常用于提取漫画封面

支持压缩包里有一层或两层文件夹的情况

### 文件重命名为翻转的形式（拖拽，多个文件或文件夹，包含二级目录文件）.py

reverse file name

例12345.txt会重命名成54321.txt

如果拖拽文件夹，文件夹名和里面的文件名都会翻转

### 识别rarzip内是否有文件名是关键词的文件，(公众号)为例（拖拽，多个文件或文件夹，支持多层文件夹）.py

search file name in .rar or .zip

如果压缩包里有文件夹包含"公众号"3个字，就会显示出这个压缩包的名字

### 计算文件sha1（拖拽，多个文件或文件夹）.py

cal sha1

拖拽文件或文件夹到py上，生成的.txt在和文件同级目录，在文件夹目录内

可选项：.txt还是其他格式，是否显示文件大小

### 根据漫画补档网址，生成帖子名.txt包含网址发布时间一楼内容.py

get manhuabudang.com content

修改py内的url，获取漫画补档的某个帖子内容

### tampermonkey moeshare帖子内按a每层评分1活跃度.js

add huoyue in moeshare.cc

chrome或edge浏览器安装油猴子插件tampermonkey，新建并复制进去，在水区帖子立按a开始评分。

### 文件名原扩展名后添加新扩展名，rar为例（拖拽，多个文件或文件夹）.py

add new suffix to file

文件名原扩展名后添加新扩展名

### 文件名中文改成拼音或拼音首字母（拖拽，多个文件或文件夹）.py

rename file name to pinyin

需要pip install pypinyin

文件里设置全拼或首字母

英文不转换

### 高度和对应文件数量信息获取（拖拽，递归，多个文件或文件夹）.py

get image's height and file count

需要pip install pillow

文件内设置显示方式

### 搜索sha1相同的文件（拖拽，递归，多个文件或文件夹）.py

search same sha1 file

文件内设置显示方式

### 获取文件夹内文件的压缩文件多少大小类型sha1（拖拽，仅文件夹）.py

get folder's file's type, count, size

用于显示文件各种信息，整理

需要同级目录下UnRAR.exe 或 pip install unrar

如果直接运行，存在文件夹名.sha文件的话，就开始校验文件

拖文件夹或.sha文件到脚本上，也可以校验

### 图片信息和颜色表或Photoshop .act文件信息获取（拖拽，多个文件或文件夹）.py

get color table of image and photoshop .act

获取图片的宽度高度模式和颜色表，并输出到文件

读取Photoshop颜色表

### 图片高度按比例修改（拖拽，多个文件或文件夹）.py

resize image for height

需要pip install pillow

按比例修改图片高度，文件里填写需要的高度

### 图片旋转角度使用ImageMagick的convert（拖拽，多个文件或文件夹）.py

change image's degree

需要同级目录下convert.exe

旋转，文件内修改角度

### 图片无损压缩使用pingo（拖拽，多个文件或文件夹）.py

需要pip install piexif

需要同级目录下pingo.exe

注意备份，压缩的图片会覆盖原图

loseless compress image

压缩图片

### 图片按左右分割成两张图（拖拽，多个文件或文件夹）.py

divide image into two

裁剪分割图片，文件内设置参数

### 图片按坐标裁剪（拖拽，多个文件或文件夹）.py

cut image file for (x,y)

文件内设置新图片的坐标

### 图片水平分割成两张图使用ImageMagick的convert（拖拽，多个文件或文件夹）.py

divide image into two

需要同级目录下convert.exe

拖拽文件夹到py上运行

### 图片每两张水平合并使用ImageMagick的convert（拖拽，仅文件夹）.py

combine two image into one

需要同级目录下convert.exe

拖拽文件夹到py上运行

文件夹内的第一张图如果不是单页，在文件内的setFirstSinglePage设置，比如第一张是单页，setFirstSinglePage = 0，第五张是单页，设置setFirstSinglePage = 4，会读取这页的宽度来判断哪些已经是双页的

### 图片文件夹或ziprar文件内的图片类型高度宽度大小信息生成.txt（拖拽，文件夹或ziprar）.py

get image's height,width, support zip and rar

支持zip,rar压缩包

需要pip install pillow

**适用于添加到压缩文件注释**

生成.txt文件包含信息：书名、作者、出版、扫者、类型数量、高度数量、文件数量、文件夹大小、文件夹创建时间、文件夹修改时间

### 图片文件夹或ziprar文件内的图片类型高度宽度大小信息生成到压缩文件的注释并压缩或添加注释（拖拽，文件夹或ziprar）.py

get image's height and put it into .zip file

需要pip install pillow

生成文件包含信息：书名、作者、出版、扫者、类型数量、高度数量、文件数量、文件夹大小、文件夹创建时间、文件夹修改时间

并创建zip文件，把上面的信息添加到注释里，压缩方式：存储

相当于上一个py脚本加上压缩文件这步整合起来

zip压缩包会添加注释，rar不会

### 文件名重命名.epub文件使用epub元数据的书名（拖拽，多个文件或文件夹）.py

rename .epub file by epub metadata 

使用epub元数据的书名重命名.epub文件

### 文件名识别文件真正的扩展名并修改（拖拽，多个文件或文件夹）.py

get real suffix and rename

需要pip install fleep

默认只显示信息不修改扩展名，如果需要修改扩展名请把第14行改为renameToRealSuffix = True

有多个可能时，强行修改成第N个扩展名，forceRenameToRealSuffixIndex = -1，改成第1个 = 0，改成第2个 = 1

### 文件扩展名修改，txt改zip为例=txt_zip（拖拽，多个文件或文件夹）.py

change file suffix

设置选项：
任何旧扩展名都改成新扩展名
没有扩展名的文件添加新扩展名
需要修改的话，把文件夹名=后面改成自己需要的，原扩展名_新扩展名，例如
文件扩展名修改，txt改zip为例=zip_pdf（拖拽，多个文件或文件夹）.py

### 文件名重命名.flac文件使用flac元数据的歌名歌手（拖拽，多个文件或文件夹）.py

rename .flac by meta data

需要pip install tinytag

rename .flac file by flac metadata 

使用flac元数据的歌名歌手重命名.flac文件

### 图片损坏检测（拖拽，多个文件或文件夹）.py

search broke images

需要pip install pillow

检测图片损坏

使用pillow verify() 

### 使用mupdf包中的mutool提取pdf图片和字体（拖拽，多个文件或文件夹）.py

get pdf's image and font

需要同级目录下mutool.exe，下载地址https://mupdf.com/downloads/archive/mupdf-1.20.0-windows.zip

提取pdf图片和字体

### 图片末尾添加一行信息，如果已添加则显示信息（拖拽，多个文件或文件夹）.py

add info in image

图片末尾添加一行信息，如果已添加则显示信息.

### 文件名纯数字前补0或去0（拖拽，多个文件或文件夹）.py

number filename add 0 or del 0

纯数字文件名前补0或去0

### 图片文件夹转成pdf文件使用ImageMagick的convert（拖拽，仅文件夹）.py

make pdf

需要同级目录下convert.exe

### tampermonkey moeshare萌享帖子里按s保存帖子1楼信息.js

浏览器安装tampermonkey，新建脚本复制进去，帖子里按s保存成html

### 文件夹内的文件名重命名成递增的纯数字（拖拽，仅多个文件夹）.py

rename filename by number

文件夹内的文件名重命名成递增的纯数字

可以设置开始序号和数字位数

### 文件夹的最后一个文件删除（拖拽，递归，多个文件夹）.py

del last file in folder

处理被拖拽的文件夹的文件，和每个子文件夹内的文件

### 图片垂直或水平合并成一张图使用ImageMagick的convert（拖拽，仅多个文件）.py

image merge

把多张图片拖拽到文件上，生成新的合并后的图片，可以设置压缩比例和垂直或水平合并

### 把多个文件当作脚本的参数（拖拽，递归，多个文件或文件夹）.py

unpack .epub or .azw3

可以配合kindleunpack解包电子书

### 搜索文件夹内特定类型的文件内容是否含关键词（拖拽，多个文件夹）.py

search keywork in file

搜索关键词

### 搜索文件夹内特定类型的图片是否含二维码（低精度）（拖拽，多个文件夹）.py

search qrcode in image

搜索图片有没有二维码

### 统计中文字数（拖拽，递归，多个文件或文件夹）.py

get work count

拖拽的是文件夹，就统计里面所有符合扩展名类型的文件的中文字数

拖拽的是文件，只统计这个文件内的中文字数

支持epub文件

可以设置是否修改文件名，在最后添加字数

### 统计含数字的文件名可能的缺失情况（拖拽，递归，仅文件夹）.py

如果image001.jpg后是image003.jpg，则输出可能缺失的文件image002.jpg

支持文件夹和zip格式

### 文件名重命名以某个扩展名的文件名命名其他文件（拖拽，多个文件）.py

文件名重命名以某个扩展名的文件名命名其他文件

相同的扩展名的文件有2个或以上时，不会执行重命名

比如同时拖拽1.html，2.mp3，3.jpg，在setRenameFileType设置成'.html'，那么3个文件会以.html文件名命名，结果是1.html，1.mp3，1.jpg

### 每个文件夹（包含）压缩成zip文件压缩方式存储（拖拽，多个文件夹）.py

每个文件夹压缩成zip文件，包含这个文件夹，zip文件=文件夹名，压缩方式：存储（速度最快）

### 中文注音使用html上标注音格式ruby和rt（拖拽，递归，多个文件或文件夹）.py

需要pip install pypinyin

可设置每行是否在每行首尾添加<p></p>

是否只注音生僻字

把不含p标签的结果直接复制到.md文件里，适用于hexo博客

已经存在的文件名.html不会被覆盖

### 日语平假名括号注音转换成html上标注音格式ruby和rt（拖拽，递归，多个文件或文件夹）.py

需要自己注音

可以把形(かたち)转换成<ruby>形<rt>かたち</rt></ruby>，在html中，形字上面注音的形式

把不含p标签的结果直接复制到.md文件里，适用于hexo博客

已经存在的文件名.html不会被覆盖

### 日语注音使用html上标注音格式ruby和rt（拖拽，递归，多个文件或文件夹）.py

需要pip install pykakasi

把不含p标签的结果直接复制到.md文件里，适用于hexo博客

不需要自己注音，直接转换汉字到平假名

已经存在的文件名.html不会被覆盖

### 复制出epub的封面图片（拖拽，递归，多个文件或文件夹）.py

复制出封面图片cover.jpg或cover.jpeg，可以设置封面图片复制到的位置

### neeview一键保存当前图片命名为书名加图片名.nvjs

[https://andi.wang/2024/03/07/neeview一键保存当前图片/](https://andi.wang/2024/03/07/neeview一键保存当前图片/)

### 图片压缩包内添加ComicInfo.xml（拖拽，仅文件夹）.py

给漫画压缩包添加ComicInfo.xml
仅拖拽文件夹，文件夹内是需要添加ComicInfo.xml的压缩包
符合以下条件才会运行脚本
1. 文件名要求格式[书名][作者][出版社][扫者]册数.扩展名
2. 压缩包内不含文件夹时，而且没有ComicInfo.xml
3. 文件夹内的文件[书名][作者]都一致
4. 文件扩展名fileType = ['.cbz', '.zip']

### 文本文件每行结尾不是标点符号就和下一行合并（拖拽，递归，多个文件或文件夹）.py

用于处理一些txt小说

借助deepseek编写

### 文本文件每行日期的日和月前补0（拖拽，递归，多个文件或文件夹）.py

处理笔记中日期不统一的情况

使用deepseek协助编写

### 删除html文件内class名是test的span标签（拖拽，递归，多个文件或文件夹）.py

用于处理html文件

### 文件判断压缩文件是否加密（拖拽，递归，多个文件或文件夹）.py

需要pip install py7zr rarfile

如果压缩文件有密码，就输出文件名

使用trae协助编写

### 文件epub转zip（拖拽，递归，多个epub或文件夹）.py

源脚本来源https://moeshare.cc/read-htm-tid-328398.html

使用trae协助编写

### 文件判断压缩文件是否包含文件夹（拖拽，递归，多个文件或文件夹）.py

压缩包内包含或不包含文件夹，都会显示

使用trae协助编写

### vscode插件将当前行中的日期更新为今天的日期update-date-to-today.zip

vscode插件，将当前行中的日期更新为今天的日期

https://andi.wang/2025/03/28/vscode%E6%8F%92%E4%BB%B6%E5%B0%86%E5%BD%93%E5%89%8D%E8%A1%8C%E4%B8%AD%E7%9A%84%E6%97%A5%E6%9C%9F%E6%9B%B4%E6%96%B0%E4%B8%BA%E4%BB%8A%E5%A4%A9%E7%9A%84%E6%97%A5%E6%9C%9F/

在vscode中，点击左侧扩展按钮Ctrl+Shift+X，扩展窗口右上角三个点，从vsix安装，选择update-date-to-today-0.0.1.vsix

重启vscode，把光标放到需要修改的行，按下Ctrl+Shift+D快捷键，日期就会被修改了。

使用trae协助编写