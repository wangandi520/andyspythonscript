# encoding:utf-8
# https://github.com/wangandi520

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import QUrl
from pathlib import Path

# pip install pyqt5 pyqt5-tools pypinyin

class MyQWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('老王扩展名修改器v1.0')
        topLayout = QHBoxLayout()
        outputTLayout = QHBoxLayout()
        outputSLayout = QHBoxLayout()
        outputLetterLayout = QHBoxLayout()
        outputFirstLetterLayout = QHBoxLayout()
        helpLayout = QHBoxLayout()
        mainLayout = QVBoxLayout()
        beforeLabel = QLabel('原扩展名')
        self.beforeLineEdit = QLineEdit()
        self.switchButton = QPushButton('<=>')
        afterLabel = QLabel('新扩展名')
        self.afterLineEdit = QLineEdit()
        helpLabel = QLabel('确定好扩展名，拖拽文件或文件夹（所有文件）就会生效')

        self.setMinimumSize(100, 80)
        self.allFilePathList = []
        self.setAcceptDrops(True)
        
        self.switchButton.clicked.connect(self.doSwitch)
        
        topLayout.addWidget(beforeLabel)
        topLayout.addWidget(self.beforeLineEdit)
        topLayout.addWidget(self.switchButton)
        topLayout.addWidget(afterLabel)
        topLayout.addWidget(self.afterLineEdit)
        helpLayout.addWidget(helpLabel)
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(helpLayout)
        self.setLayout(mainLayout)
                
        # 从文件名读取参数
        theFileName = Path(sys.argv[0]).stem
        if ('=' in theFileName and '_' in theFileName):
            tempValue = theFileName.split('=')[1]
            self.beforeLineEdit.setText(tempValue.split('_')[0])
            self.afterLineEdit.setText(tempValue.split('_')[1])
            

    def dragEnterEvent(self, event):
        event.acceptProposedAction()
    
    
    def dropEvent(self, event):
        if self.beforeLineEdit.text() != '' and self.afterLineEdit.text() != '':
            for eachFile in event.mimeData().urls():
                if (eachFile.toString()[0:8] == 'file:///'):
                    filePath = Path(eachFile.toString()[8:])
                    # 原扩展名
                    beforeSuffix = '.' + self.beforeLineEdit.text()
                    # 新扩展名
                    afterSuffix = '.' + self.afterLineEdit.text()
                    
                    if Path.is_dir(filePath):
                        for file in Path(filePath).glob('**/*'):
                            if Path.is_file(file) and file.suffix == beforeSuffix:
                                file.rename(Path(file).parent.joinpath(file.stem + afterSuffix))
                                print(file.name + '  ->  ' + file.stem)
                    if Path.is_file(filePath) and filePath.suffix == beforeSuffix:
                        Path(filePath).rename(Path(filePath).parent.joinpath(Path(filePath).stem + afterSuffix))
                        print(Path(filePath).name + '  ->  ' + Path(filePath).stem)


    def doSwitch(self):
        tempText = self.beforeLineEdit.text()
        self.beforeLineEdit.setText(self.afterLineEdit.text())
        self.afterLineEdit.setText(tempText)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywidget = MyQWidget()
    mywidget.show()
    sys.exit(app.exec_())