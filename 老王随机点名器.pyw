# encoding:utf-8
# https://github.com/wangandi520

import sys
import random
import pandas

# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *

from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QCheckBox, QLabel, QSlider, QStatusBar, QListWidget, QShortcut, QFileDialog, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import QDir, QTimer, QDateTime, Qt
from PyQt5 import QtWidgets, QtCore
from pathlib import Path

# pip install pyqt5 pyqt5-tools pyinstaller pandas openpyxl

'''
老王随机点名器v1.1

运行python脚本，需要 pip install pyqt5 pyqt5-tools pyinstaller pandas openpyxl

1.1版更新：
支持xls,xlsx

1.0版更新：
改用PyQt5重写
暂时不支持xls文件

0.42版更新：
更新捐赠二维码

0.41版更新：
添加速度调节
修复bug
可快速捐赠

0.4版更新：
支持模板的xls文件

0.3版更新：
增加了重置列表按钮
更改了文件切换时重新读取文件的设计
修改缺席名单的命名方式
添加缺席按钮
修正取消打开文件而添加文件的错误

0.2版更新：
修正了时间闪烁的问题
修改状态栏显示
增加打开文件后自动选择的功能
增加了字体大小调节
调整了内部设计，修复了剩余数量显示错误
修复文件删除后仍能点名的错误
添加清空列表按钮
'''


class MyQWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle('老王随机点名器v1.1')
        topLayout = QHBoxLayout()
        bottomLayout = QHBoxLayout()
        buttonLayout = QHBoxLayout()
        bottomLeftLayout = QVBoxLayout()
        bottomRightLayout = QVBoxLayout()
        mainLayout = QVBoxLayout()
        
        self.allOpenFileNameList = []
        self.allOpenFileContentList = []
        self.tempShowNameLabel = ''
        self.setWeekConfig = '1'
        self.setMarkConfig = 'X'
        
        self.openFileButton = QPushButton("打开文件")
        self.clearButton = QPushButton("清空列表")
        self.setButton = QPushButton("设置")
        self.donateButton = QPushButton("捐赠")
        self.startButton = QPushButton("开始")
        self.absentButton = QPushButton("缺席")
        self.reloadButton = QPushButton("重新载入")
        self.uploadButton = QPushButton("上传")
        self.repeatCheckBox = QCheckBox("不重复点名")
        
        # 设置开始停止按钮快捷键为空格键
        self.startButton.setShortcut(Qt.Key_Space)
        self.absentButton.setShortcut(Qt.Key_B)
       
        
        self.repeatCheckBox.setChecked(True)
        self.fileListMessageLabel = QLabel("文件列表")
        self.showNameLabel = QLabel('')
        self.showNameLabel.setFont(QFont("WenQuanYi Micro Hei", 90))
        self.showNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resetNameLabel = QLabel("剩余数量0")
        self.fileStatus = QLabel(QDir.currentPath())
        self.fileListWidget = QListWidget()
        
        self.fileListWidget.setMinimumWidth(200)
        
        self.currentTime = QLabel()
        currentClockTimer = QTimer(self)
        currentClockTimer.start(1000)
        currentClockTimer.timeout.connect(self.showNowTime)
        
        self.changNameLabelTimer = QTimer(self)
        
        # 设置字体尺寸范围
        self.fontSizeLabel = QLabel("字号: 100")
        self.fontSizeSlider = QSlider()
        self.fontSizeSlider.setOrientation(Qt.Horizontal)
        self.fontSizeSlider.setValue(100)
        self.fontSizeSlider.setRange(20, 600)
        self.fontSizeSlider.setSingleStep(5)
        
        self.speedLabel = QLabel("速度(毫秒): 50")
        self.speedSlider = QSlider()
        self.speedSlider.setOrientation(Qt.Horizontal)
        self.speedSlider.setValue(50)
        self.speedSlider.setRange(10, 5000)
        self.speedSlider.setSingleStep(10)
        status = QStatusBar()

        # setUploadAddressLabel = QLabel("设置文件上传路径")
        # setWeekLabel = QLabel("设置点名周")
        # setMarkLabel = QLabel("设置标记（例X为缺席，O为已到，只对xls有效）")
        # setWidgetLayout = QVBoxLayout()
        # setWidgetButtonLayout  = QHBoxLayout()
        # setWidget = QWidget()
        # setUploadAddress = QLineEdit("NULL")
        # setWeek = QLineEdit("1")
        # setMark = QLineEdit("X")
        # writeOldFileCheckBox = QCheckBox("缺席名单写到原文件中（xls默认选中）")
        # writeOldFileCheckBox.setChecked(False)

        # #setWidget.setAttribute(Qt.WA_QuitOnClose, False)
        # setOkButton = QPushButton("确定")
        # setCancelButton = QPushButton("取消")
        # setWidgetButtonLayout.addWidget(setOkButton)
        # setWidgetButtonLayout.addWidget(setCancelButton)
        # setWidgetLayout.addWidget(setWeekLabel)
        # setWidgetLayout.addWidget(setWeek)
        # setWidgetLayout.addWidget(setMarkLabel)
        # setWidgetLayout.addWidget(setMark)
        # setWidgetLayout.addWidget(writeOldFile)
        # setWidgetLayout.addLayout(setWidgetButtonLayout)
        # setWidget.setLayout(setWidgetLayout)
        # setWidget.setFixedWidth(300)
        
        # 信号
        self.startButton.clicked.connect(self.getStartButtonConnect)
        self.absentButton.clicked.connect(self.addAbsentList)
        self.setButton.clicked.connect(self.configWindow)
        self.openFileButton.clicked.connect(self.setOpenFileName)
        self.reloadButton.clicked.connect(self.reloadFileList)
        self.donateButton.clicked.connect(self.donateWindow)
        self.clearButton.clicked.connect(self.clearAll)
        self.fileListWidget.currentRowChanged.connect(self.changeFileCountForCurrentRow)
        self.fontSizeSlider.valueChanged.connect(self.setFontSize)
        self.speedSlider.valueChanged.connect(self.setSpeed)
        
        # 信号和槽的连接
        # self.connect(startShortCut, SIGNAL(activated()), startButton, SLOT(click()))
        # self.connect(absentShortCut, SIGNAL(activated()), absentButton, SLOT(click()))
        # self.connect(donateButton, SIGNAL(clicked()), this, SLOT(donateWindows()))
        # self.connect(startButton, SIGNAL(clicked()), this, SLOT(nameChange()))
        # self.connect(openFileButton, SIGNAL(clicked()), this, SLOT(setOpenFileName()))
        # self.connect(clearButton, SIGNAL(clicked()), this, SLOT(clearAll()))
        # self.connect(absentButton, SIGNAL(clicked()), this, SLOT(absentAdd()))
        # self.connect(fontSize, SIGNAL(valueChanged(int)), this, SLOT(setFont(int)))
        # self.connect(speed, SIGNAL(valueChanged(int)), this, SLOT(setSpeed(int)))
        # self.connect(currentClockTimer, SIGNAL(timeout()), this, SLOT(clockChange()))
        # self.connect(reloadButton, SIGNAL(clicked()), this, SLOT(reloadFileList()))

        # self.connect(setButton, SIGNAL(clicked()), setWidget, SLOT(show()))
        # self.connect(setButton, SIGNAL(clicked()), this, SLOT(readConfig()))
        # self.connect(setOk, SIGNAL(clicked()), this, SLOT(writeConfig()))
        # self.connect(setCancel, SIGNAL(clicked()), setWidget, SLOT(close()))

        # 按钮设置为不可用
        self.clearButton.setDisabled(True)
        self.reloadButton.setDisabled(True)
        self.startButton.setDisabled(True)
        self.absentButton.setDisabled(True)
        # 设置鼠标悬停提醒
        self.startButton.setToolTip("快捷键：空格")
        # startButton.setMaximumWidth(300)
        self.absentButton.setToolTip("快捷键：B")
        # absentButton.setMaximumWidth(300)
        self.openFileButton.setToolTip("支持文件：一行一个名字的txt文件")
        self.reloadButton.setToolTip("重新读取文件列表中的所有文件")
        self.clearButton.setToolTip("清空列表中的文件")

        # 设置状态栏
        status.addWidget(self.fileStatus, 100)
        status.addWidget(self.currentTime,35)
        # 窗口大小
        self.setMinimumSize(1000, 600)

        # Layout设置
        topLayout.addWidget(self.openFileButton)
        topLayout.addWidget(self.reloadButton)
        topLayout.addWidget(self.clearButton)
        topLayout.addWidget(self.setButton)
        topLayout.addWidget(self.repeatCheckBox)
        topLayout.addWidget(self.resetNameLabel)
        topLayout.addWidget(self.fontSizeLabel)
        topLayout.addWidget(self.fontSizeSlider)
        topLayout.addWidget(self.speedLabel)
        topLayout.addWidget(self.speedSlider)
        topLayout.addWidget(self.donateButton)
        bottomLeftLayout.addWidget(self.fileListMessageLabel)
        bottomLeftLayout.addWidget(self.fileListWidget)
        bottomRightLayout.addWidget(self.showNameLabel)
        bottomRightLayout.addLayout(buttonLayout)
        bottomRightLayout.setAlignment(QtCore.Qt.AlignHCenter)
        buttonLayout.addWidget(self.startButton)
        buttonLayout.addWidget(self.absentButton)
        buttonLayout.setStretchFactor(self.startButton,1)
        buttonLayout.setStretchFactor(self.absentButton,1)
        bottomLayout.addLayout(bottomLeftLayout)
        bottomLayout.addLayout(bottomRightLayout)
        bottomLayout.setStretch(1,4)
        bottomLayout.setStretchFactor(bottomLeftLayout,1)
        bottomLayout.setStretchFactor(bottomRightLayout,4)
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(bottomLayout)
        mainLayout.addWidget(status)
        self.setLayout(mainLayout)

    def donateWindow(self):
        # 捐赠窗口
        donateMes = QMessageBox()
        donateAlipayImg = QPixmap("donate.png")
        donateAlipayImg = donateAlipayImg.scaled(800, 800, Qt.KeepAspectRatio)
        donateMes.setIconPixmap(donateAlipayImg)
        donateMes.setWindowTitle("感谢捐赠支持。")
        donateMes.setText('支付宝：30204977@qq.com')
        yesButton = donateMes.addButton("关闭",QMessageBox.YesRole)
        donateMes.exec()
        if (donateMes.clickedButton() == yesButton):
                donateMes.close()
        
    def showNowTime(self):
        # 右下角显示时间
        self.currentTime.setText(QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss ddd"))
        
    def configWindow(self):
        # 设置窗口
        # setUploadAddressLabel = QLabel("设置文件上传路径")
        self.configWidget = QWidget()
        setWeekLabel = QLabel("设置点名周（数字）")
        setMarkLabel = QLabel("设置标记（例X为缺席，O为已到）")
        setOkButton = QPushButton("确定")
        setCancelButton = QPushButton("取消")
        setWidgetLayout = QVBoxLayout()
        setWidgetButtonLayout  = QHBoxLayout()
        self.configWidget.setWindowTitle('设置（仅对Excel有效）')
        setUploadAddress = QLineEdit("NULL")
        self.setWeekConfigLineEdit = QLineEdit(self.setWeekConfig)
        self.setMarkConfigLineEdit = QLineEdit(self.setMarkConfig)
        setCancelButton.clicked.connect(self.configWidget.close)
        self.configWidget.setAttribute(Qt.WA_QuitOnClose, False)
        setWidgetButtonLayout.addWidget(setOkButton)
        setWidgetButtonLayout.addWidget(setCancelButton)
        setWidgetLayout.addWidget(setWeekLabel)
        setWidgetLayout.addWidget(self.setWeekConfigLineEdit)
        setWidgetLayout.addWidget(setMarkLabel)
        setWidgetLayout.addWidget(self.setMarkConfigLineEdit)
        setWidgetLayout.addLayout(setWidgetButtonLayout)
        self.configWidget.setLayout(setWidgetLayout)
        self.configWidget.setFixedWidth(300)
        self.configWidget.show()
        setOkButton.clicked.connect(self.saveConfig)
        
    def saveConfig(self):
        self.setWeekConfig = self.setWeekConfigLineEdit.text()
        self.setMarkConfig = self.setMarkConfigLineEdit.text()
        self.configWidget.close()
        
    def setOpenFileName(self):
        # 打开文件
        openFileName = []
        openFileType = []
        # TXT必须是UTF-8编码
        tempName = QFileDialog.getOpenFileName(self,  "打开文件", ".", "文本文件(*.txt *.xls *.xlsx)")
        if (tempName[0] == ''):
            return
        self.fileStatus.setText(tempName[0])
        if (len(openFileName) == 0 and not (tempName[0] in self.allOpenFileNameList)):
            # 当前选中的行的索引
            # getSelectedIndex = self.fileListWidget.currentRow()
            # 当前选中的文件的路径
            try:
                with open(tempName[0], mode='r', encoding='UTF-8') as file:
                    currentFileContent = []
                    if Path(tempName[0]).suffix == '.txt':
                        currentFileContent = file.readlines()
                        for i in currentFileContent:
                            if i == '\n':
                                currentFileContent.remove(i)      
                        for i in range(len(currentFileContent)):
                            currentFileContent[i] = currentFileContent[i].rstrip()
                    if Path(tempName[0]).suffix in ['.xls', '.xlsx']:
                        readExcelFile = pandas.read_excel(tempName[0], skiprows = 1)
                        # 行数量
                        readExcelColumnsCount = readExcelFile.shape[0]
                        # 列数量
                        readExcelRowsCount = readExcelFile.shape[1]
                        # 所有名字
                        readAllNames = readExcelFile.iloc[0:readExcelColumnsCount, 0]
                        
                        # 第一个名字，第二周
                        #print(readExcelFile.iloc[1,2])
                        # 除了第一行
                        # newExcelData = readExcelFile.iloc[1:,0:]
                        #print(readExcelFile.loc['第一周','一灯大师'])
                        #print(readExcelFile.loc['一灯大师':'马钰'])
                        #print(readExcelFile.loc['一灯大师':'马钰','第一周'])
                        # print(readExcelFile.iloc[0,1])
                        # print(readExcelFile.iloc[0,2])
                        # print(readExcelFile.iloc[0,3])
                        # print(readExcelFile.iloc[1,0])
                        # print(readExcelFile.iloc[2,0])
                        # print(readExcelFile.iloc[3,0])
                        
                        
                        
                        for i in range(1, readExcelColumnsCount):
                            currentFileContent.append(readAllNames[i])
                    if len(currentFileContent) != 0:
                        self.allOpenFileContentList.append(currentFileContent)
                        self.allOpenFileNameList.append(tempName[0])
                        self.fileListWidget.addItem(Path(tempName[0]).name)
                        self.fileListWidget.item(self.fileListWidget.count() - 1).setSelected(True)
            except UnicodeDecodeError:
                QMessageBox.warning(self, "错误", "TXT文件必须是UTF-8编码，尝试记事本打开后另存为下方更改编码。",  QMessageBox.Ok)
        elif (tempName[0] in self.allOpenFileNameList):
            QMessageBox.warning(self, "错误", "文件已打开",  QMessageBox.Ok)
        if (len(self.allOpenFileNameList) > 0):
            self.clearButton.setEnabled(True)
            self.reloadButton.setEnabled(True)
            self.startButton.setEnabled(True)
            self.absentButton.setEnabled(True)
        # 设置焦点在开始按钮
        self.startButton.setFocus()
        self.changeFileCountForCurrentRow()
    
    
    def changeFileCountForCurrentRow(self):
        # 更新文件数量和名字数量
        if (len(self.allOpenFileNameList) != 0):
            self.showNameLabel.setText('')
            self.fileListMessageLabel.setText("文件列表(" + str(len(self.allOpenFileNameList)) + ")")
            self.resetNameLabel.setText("剩余数量" + str(len(self.allOpenFileContentList[self.fileListWidget.currentRow()])))
            self.fileStatus.setText(self.allOpenFileNameList[self.fileListWidget.currentRow()])


    def getStartButtonConnect(self):
        # 连接开始按钮事件
        if (len(self.allOpenFileNameList) == 0):
            return;
        if (self.startButton.text() == "开始" and self.allOpenFileContentList[self.fileListWidget.currentRow()] != 0):
            #connect(timer, SIGNAL(timeout()), this, SLOT(randomName()));
            #self.changNameLabelTimer = QTimer(self)
            self.changNameLabelTimer.start(100)
            self.changNameLabelTimer.timeout.connect(self.showRandomName)
            self.startButton.setText("停止");
            self.absentButton.setDisabled(True)
            # 删除被点过的名字
            if (len(self.showNameLabel.text()) != 0):
                self.tempShowNameLabel = self.showNameLabel.text()
                self.allOpenFileContentList[self.fileListWidget.currentRow()].remove(self.showNameLabel.text())
                self.changeFileCountForCurrentRow()
        elif self.startButton.text() == "停止":
            self.changNameLabelTimer.timeout.disconnect(self.showRandomName)
            self.absentButton.setDisabled(False)
            self.startButton.setText("开始");
            
            
    def showRandomName(self):
        # 中间标签显示切换
        if (self.startButton.text() == "停止" and len(self.allOpenFileContentList[self.fileListWidget.currentRow()]) != 0):
            randNumber = random.randint(0, len(self.allOpenFileContentList[self.fileListWidget.currentRow()]) - 1)
            self.showNameLabel.setText(self.allOpenFileContentList[self.fileListWidget.currentRow()][randNumber])
           

    def setFontSize(self):
        # 调整字体大小
        self.showNameLabel.setFont(QFont("WenQuanYi Micro Hei", self.fontSizeSlider.value()))
        self.fontSizeLabel.setText('字号: ' + str(self.fontSizeSlider.value()))


    def setSpeed(self):
        # 调整切换速度
        self.changNameLabelTimer.start(self.speedSlider.value())
        self.speedLabel.setText('速度(毫秒): ' + str(self.speedSlider.value()))


    def addAbsentList(self):
        # 缺席人员名单导出
        if (len(self.allOpenFileNameList) == 0 and self.showNameLabel.text() != ''):
            return
        myCurrentSelectedFileName = self.allOpenFileNameList[self.fileListWidget.currentRow()]
        myCurrentSelectedFileSuffix = Path(myCurrentSelectedFileName).suffix
        if (self.showNameLabel.text() != '' and myCurrentSelectedFileSuffix == ".txt"):
            newfile = open(Path(myCurrentSelectedFileName).stem + '缺席名单' + QDateTime.currentDateTime().toString("yyyy-MM-dd") + '.txt', mode='a+', encoding='UTF-8')
            # show file location
            writeContent = []
            writeContent.append(QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss") + '\n')
            writeContent.append(self.showNameLabel.text() + '\n\n')
            newfile.writelines(writeContent)
            newfile.close()
            if (self.repeatCheckBox.isChecked() and len(self.showNameLabel.text()) != 0):
                self.allOpenFileContentList[self.fileListWidget.currentRow()].remove(self.showNameLabel.text())
                self.changeFileCountForCurrentRow()
                
        if (self.showNameLabel.text() != '' and myCurrentSelectedFileSuffix in ['.xls', '.xlsx']):  
            #readExcelFile = pandas.read_excel(tempName[0])
            readExcelFile = pandas.read_excel(myCurrentSelectedFileName, skiprows = 1, index_col = '姓名日期')
            # 行数量
            readExcelColumnsCount = readExcelFile.shape[0]
            # 列数量
            readExcelRowsCount = readExcelFile.shape[1]
            
            
            allWeeks = ['第零周', '第一周', '第二周', '第三周', '第四周', '第五周', '第六周', '第七周', '第八周', '第九周', '第十周', '第十一周', '第十二周', '第十三周', '第十四周', '第十五周', '第十六周', '第十七周', '第十八周', '第十九周', '第二十周', '第二十一周', '第二十二周', '第二十三周', '第二十四周', '第二十五周']

            getWeek = self.setWeekConfig
            getMark = self.setMarkConfig
            
            print(getWeek)
            
            print(readExcelFile.loc[self.showNameLabel.text(),allWeeks[int(getWeek)]])
        
            writeExcelFile = pandas.to_excel(myCurrentSelectedFileName)
            
            if (self.repeatCheckBox.isChecked() and len(self.showNameLabel.text()) != 0):
                self.allOpenFileContentList[self.fileListWidget.currentRow()].remove(self.showNameLabel.text())
                self.changeFileCountForCurrentRow()
                        # print(readExcelFile.iloc[0,1])
                        # print(readExcelFile.iloc[0,2])
                        # print(readExcelFile.iloc[0,3])
                        # print(readExcelFile.iloc[1,0])
                        # print(readExcelFile.iloc[2,0])
                        # print(readExcelFile.iloc[3,0])
            # for i in range(1, readExcelColumnsCount):
                # currentFileContent.append(readAllNames[i])
        
            # QFile file(currentFile)
            # file.open(QFile.Append | QIODevice.Text)
            # QTextStream write(&file)

            # write << endl
            # write << QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss") << endl
            # write << showNameLabel.text() << endl
            # write << endl
            # file.close()
           
        # elif (tailSave(currentFile).contains("xls")):
            # ExcelEngine excel
            # excel.Open(currentFile)
            # excel.SetCellData(randN, setWeek.text().toInt() + 1, setMark.text())
            # excel.Save()
            # excel.Close()


        self.showNameLabel.setText('')

    def reloadFileList(self):
        self.startButton.setText("开始")
        if (len(self.allOpenFileNameList) == 0):
            return
        # 清空内容后重新载入
        self.allOpenFileContentList.clear()
        for eachFileName in self.allOpenFileNameList:
            eachFileContent = []
            with open(eachFileName, mode='r', encoding='UTF-8') as file:
                eachFileContent = file.readlines()
            for i in eachFileContent:
                if i == '\n':
                    eachFileContent.remove(i)      
            for i in range(len(eachFileContent)):
                eachFileContent[i] = eachFileContent[i].rstrip()
            self.allOpenFileContentList.append(eachFileContent)
        self.changeFileCountForCurrentRow()


    def clearAll(self):
        # 清空全部
        self.showNameLabel.setText('')
        self.startButton.setText("开始")
        self.resetNameLabel.setText("剩余数量0")
        self.fileListMessageLabel.setText("文件列表")
        self.fileStatus.setText(QDir.currentPath()) 
        self.allOpenFileNameList.clear()
        self.allOpenFileContentList.clear()
        self.fileListWidget.clear()
        self.clearButton.setDisabled(True)
        self.reloadButton.setDisabled(True)
        self.startButton.setDisabled(True)
        self.absentButton.setDisabled(True)


    def readConfig():
        # QFile file("config.ini")
        # file.open(QIODevice.ReadOnly)
        # QTextStream in(&file)
        # QString line
        # configList.push_back("NULL")
        # while (!in.atEnd())
        # {
            # line = in.readLine()
            # if (line != "")
            # {
                # configList[0] = line
            # }
        # }
        # file.close()

        # QString.iterator temp = configList[0].begin()
        # QString.iterator flag = configList[0].begin()
        # int size = 0
        # for (QString.iterator i = configList[0].begin() i != configList[0].end() ++i)
        # {
            # if (*i == '=')
                # temp = i
        # }
        # flag = temp
        # while (*temp != '\0')
        # {
            # ++temp
            # ++size
        # }
        # QString temps(flag + 1,  size - 1)
        # setUploadAddress.setText(temps)
        print('readConfig')

    def writeConfig():
        # QFile file("config.ini")
        # file.open(QIODevice.WriteOnly | QIODevice.Text)
        # QTextStream write(&file)
        # write << "uploadPath=" + setUploadAddress.text()
        # file.close()
        # setWidget.close()
        print('writeConfig')

    def uploadFile(fileName):
        print('uploadFile')
        # if (fileName == ""):
            # return -1

        # QNetworkRequest req(configList[0])
        # QByteArray boundary = "-------------------------87142694621188"
        # QFile file(fileName)
        # if (!file.open(QIODevice.ReadOnly))
        # {
            # return -1
        # }
        # QByteArray fileContent(file.readAll())

        # QByteArray data = "--" + boundary + "\r\n"
        # data += "Content-Disposition: form-data name=\"file\" filename=\"" + fileName +"\"\r\n"
        # # add picture to data
        # data += "Content-Type: text/plain\r\n\r\n" + fileContent + "\r\n"


        # data += "--" + boundary + "\r\n"
        # data += "Content-Disposition: form-data name=\"id\"\r\n\r\n"


        # data += "--" + boundary + "--"

        # req.setRawHeader("Content-Type", "multipart/form-data boundary=" + boundary)
        # req.setRawHeader("Content-Length", QString.number(data.size()).toLatin1())
        # file.close()
        # QNetworkAccessManager *networkManager = QNetworkAccessManager(this)
        # QNetworkReply *reply = networkManager.post(req, data)
        # if (!reply.error())
            # return -1
        # return 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('random.ico'))
    mywidget = MyQWidget()
    mywidget.show()
    sys.exit(app.exec_())