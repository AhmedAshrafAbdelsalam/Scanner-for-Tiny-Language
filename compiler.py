from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5.QtCore import pyqtSignal
import scanner

class TextEdit(QtWidgets.QTextEdit):
    clicked = pyqtSignal()
    def mousePressEvent(self, event):
            self.clicked.emit()

class LineEdit(QtWidgets.QLineEdit):
    clicked = pyqtSignal()
    def mousePressEvent(self, event):
            self.clicked.emit()

class Ui_MainWindow(QDialog):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(770, 442)
        MainWindow.setWindowTitle("CodeScanner")
        
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.border = QtWidgets.QGroupBox(self.centralwidget)
        self.border.setObjectName("border")
        self.border.setGeometry(QtCore.QRect(30, 90, 731, 321))
        
        self.fileDirectory = LineEdit(self.border)
        self.fileDirectory.setObjectName("fileDirectory")
        self.fileDirectory.setText("Type file directory here ...")
        self.fileDirectory.setGeometry(QtCore.QRect(175, 30, 431, 31))
        self.fileDirectory.setFocus(False)
        self.fileDirectory.setStyleSheet("color: grey;")

        self.uploadOption = QtWidgets.QRadioButton(self.border)
        self.uploadOption.setObjectName("uploadOption")
        self.uploadOption.setText("Upload File")
        self.uploadOption.setGeometry(QtCore.QRect(20, 25, 141, 41))
        self.uploadOption.setIconSize(QtCore.QSize(40, 40))
        self.uploadOption.setChecked(True)
        
        self.browseButton = QtWidgets.QPushButton(self.border)
        self.browseButton.setObjectName("browseButton")
        self.browseButton.setText("Browse")
        self.browseButton.setGeometry(QtCore.QRect(610, 30, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.browseButton.setFont(font)
        
        self.writeCodeOption = QtWidgets.QRadioButton(self.border)
        self.writeCodeOption.setObjectName("writeCodeOption")
        self.writeCodeOption.setText("Enter Code Snippet")
        self.writeCodeOption.setGeometry(QtCore.QRect(20, 65, 231, 31))
        self.writeCodeOption.setFocus(True)

        self.inputMethodOptions = QtWidgets.QButtonGroup(self.border)
        self.inputMethodOptions.addButton(self.uploadOption)
        self.inputMethodOptions.addButton(self.writeCodeOption)

#       self.cppOption = QtWidgets.QRadioButton(self.border)
#       self.cppOption.setObjectName("cppOption")
#       self.cppOption.setText("C++")
#       self.cppOption.setGeometry(QtCore.QRect(650, 70, 60, 31))

#       self.tinyOption = QtWidgets.QRadioButton(self.border)
#       self.tinyOption.setObjectName("tinyOption")
#       self.tinyOption.setText("TINY")
#       self.tinyOption.setGeometry(QtCore.QRect(560, 70, 60, 31))
#       self.tinyOption.setChecked(True)


#       self.inputTypeOptions = QtWidgets.QButtonGroup(self.border)
#       self.inputTypeOptions.addButton(self.cppOption)
#       self.inputTypeOptions.addButton(self.tinyOption)
        
        self.scanButton = QtWidgets.QPushButton(self.border)
        self.scanButton.setObjectName("scanButton")
        self.scanButton.setText("Scan")
        self.scanButton.setGeometry(QtCore.QRect(500, 260, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.scanButton.setFont(font)
        
        self.codeSnippet = TextEdit(self.border)
        self.codeSnippet.setObjectName("codeSnippet")
        self.codeSnippet.setGeometry(QtCore.QRect(20, 110, 691, 141))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.codeSnippet.setFont(font)
        self.codeSnippet.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.codeSnippet.setEnabled(False)
        self.codeSnippet.setStyleSheet("color: grey;")

        self.saveButton = QtWidgets.QPushButton(self.border)
        self.saveButton.setObjectName("saveButton")
        self.saveButton.setText("Save")
        self.saveButton.setGeometry(QtCore.QRect(610, 260, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.saveButton.setFont(font)
        self.saveButton.setEnabled(False)
        
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setObjectName("title")
        self.result.setGeometry(QtCore.QRect(50, 350, 470, 41))
        self.result.setStyleSheet("border :1px solid grey;")
        self.result.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(30)
        self.result.setFont(font)

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setObjectName("title")
        self.title.setText("Scanner")
        self.title.setGeometry(QtCore.QRect(30, 50, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.writeCodeOption.clicked.connect(self.enableCodeInput)
        self.uploadOption.clicked.connect(self.enableFileInput)
#       self.cppOption.clicked.connect(self.scanCPP)
#       self.tinyOption.clicked.connect(self.scanTINY)
        self.codeSnippet.clicked.connect(self.firstPressedCodeInput)
        self.fileDirectory.clicked.connect(self.firstPressedFileInput)
        self.browseButton.clicked.connect(self.browseFiles)
        self.scanButton.clicked.connect(self.scanCode)
        self.saveButton.clicked.connect(self.saveFile)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def browseFiles(self):
        fileName = QFileDialog.getOpenFileName(self ,'Open C++ File', self.fileDirectory.text(),'C++ files (*.cpp)')
        inputFile = open(fileName[0],'r')
        self.inputData = inputFile.read().replace('\n',' ')
        inputFile.close()
        self.fileDirectory.setStyleSheet("color: black;")
        self.fileDirectory.setText(fileName[0])
        self.fileDirectory.clicked.disconnect()

    def scanCode(self):
        if self.writeCodeOption.isChecked() == True:
            self.inputData = self.codeSnippet.toPlainText()
        Ui_MainWindow.data = scanner.Scanner(self.inputData)
        self.saveButton.setEnabled(True)
        self.result.setText("Scanning succeded ...")


    def saveFile(self):
        fileName = QFileDialog.getSaveFileName(self ,'Save Results',"res.cpp",'C++ files (*.cpp)')
        outputFile = open(fileName[0],'w')
        for element in Ui_MainWindow.data.result:
            outputFile.write(str(element) + "\n")
        outputFile.close()

    def enableCodeInput(self):
        self.fileDirectory.setEnabled(False)
        self.browseButton.setEnabled(False)
        self.codeSnippet.setEnabled(True)
        self.uploadOption.lower()
        self.saveButton.setEnabled(False)
        self.result.setText("")
        self.codeSnippet.setStyleSheet("color: grey;")
        self.codeSnippet.clicked.connect(self.firstPressedCodeInput)
        self.codeSnippet.setText("Type your code here ...")
        self.fileDirectory.setText("")

    def enableFileInput(self):
        self.fileDirectory.setEnabled(True)
        self.browseButton.setEnabled(True)
        self.codeSnippet.setEnabled(False)
        self.writeCodeOption.lower()
        self.saveButton.setEnabled(False)
        self.result.setText("")
        self.fileDirectory.setStyleSheet("color: grey;")
        self.fileDirectory.clicked.connect(self.firstPressedFileInput)
        self.fileDirectory.setText("Type file directory here ...")
        self.codeSnippet.setText("")

#   def scanCPP(self):
#       self.tinyOption.lower()

#   def scanTINY(self):
#       self.cppOption.lower()

    def firstPressedFileInput(self):
        self.fileDirectory.setStyleSheet("color: black;")
        self.fileDirectory.clear()
        self.fileDirectory.clicked.disconnect()

    def firstPressedCodeInput(self):
        self.codeSnippet.setStyleSheet("color: black;")
        self.codeSnippet.clear()
        self.codeSnippet.clicked.disconnect()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
