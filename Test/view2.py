
from PyQt5 import QtCore, QtGui, QtWidgets


class AddWordsWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("PopUpWindow")
        self.resize(675, 503)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_main = QtWidgets.QLabel(self.centralwidget)
        self.label_main.setGeometry(QtCore.QRect(130, 30, 411, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_main.setFont(font)
        self.label_main.setFrameShape(QtWidgets.QFrame.Box)
        self.label_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_main.setLineWidth(5)
        self.label_main.setAlignment(QtCore.Qt.AlignCenter)
        self.label_main.setObjectName("label_main")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(40, 170, 611, 350))
        self.stackedWidget.setObjectName("stackedWidget")
        self.add = QtWidgets.QWidget()
        self.add.setObjectName("add")
        self.lineEdit_addWord = QtWidgets.QLineEdit(self.add)
        self.lineEdit_addWord.setGeometry(QtCore.QRect(20, 60, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_addWord.setFont(font)
        self.lineEdit_addWord.setObjectName("lineEdit_addWord")
        self.btn_add = QtWidgets.QPushButton(self.add)
        self.btn_add.setGeometry(QtCore.QRect(410, 60, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_add.setFont(font)
        self.btn_add.setObjectName("btn_add")
        self.btn_done = QtWidgets.QPushButton(self.add)
        self.btn_done.setGeometry(QtCore.QRect(220, 190, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_done.setFont(font)
        self.btn_done.setObjectName("btn_done")
        self.stackedWidget.addWidget(self.add)
        self.remove = QtWidgets.QWidget()
        self.remove.setObjectName("remove")
        self.listWidget = QtWidgets.QListWidget(self.remove)
        self.listWidget.setGeometry(QtCore.QRect(0, 80, 591, 221))
        self.listWidget.setObjectName("listWidget")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.listWidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(570, 80, 16, 221))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.btn_delete = QtWidgets.QPushButton(self.remove)
        self.btn_delete.setGeometry(QtCore.QRect(170, 20, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_delete.setFont(font)
        self.btn_delete.setObjectName("btn_delete")
        self.stackedWidget.addWidget(self.remove)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 675, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.label_main.setText("Spelling Words")
        self.btn_add.setText("ADD")
        self.btn_done.setText("Done")
        self.btn_delete.setText("Delete")
        self.stackedWidget.setCurrentIndex(1)
        #QtCore.QMetaObject.connectSlotsByName(self)    
        
        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 858)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_speak = QtWidgets.QPushButton(self.centralwidget)
        self.btn_speak.setGeometry(QtCore.QRect(140, 80, 371, 121))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.btn_speak.setFont(font)
        self.btn_speak.setObjectName("btn_speak")
        self.btn_speak.setStyleSheet("background : lightblue;")
        self.btn_validate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_validate.setGeometry(QtCore.QRect(620, 80, 371, 121))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.btn_validate.setFont(font)
        self.btn_validate.setObjectName("btn_validate")
        self.btn_validate.setStyleSheet("background : lightblue;")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 220, 1121, 581))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_scramble = QtWidgets.QWidget()
        self.tab_scramble.setObjectName("tab_scramble")
        self.label_1 = QtWidgets.QLabel(self.tab_scramble)
        self.label_1.setGeometry(QtCore.QRect(130, 50, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_1.setFont(font)
        self.label_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.label_scramble = QtWidgets.QLabel(self.tab_scramble)
        self.label_scramble.setGeometry(QtCore.QRect(70, 120, 300, 71))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label_scramble.setFont(font)
        self.label_scramble.setFrameShape(QtWidgets.QFrame.Box)
        self.label_scramble.setText("")
        self.label_scramble.setAlignment(QtCore.Qt.AlignCenter)
        self.label_scramble.setObjectName("label_scramble")
        self.lineEdit_scramble = QtWidgets.QLineEdit(self.tab_scramble)
        self.lineEdit_scramble.setGeometry(QtCore.QRect(260, 320, 631, 151))
        font = QtGui.QFont()
        font.setPointSize(65)
        self.lineEdit_scramble.setFont(font)
        self.lineEdit_scramble.setText("")
        self.lineEdit_scramble.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_scramble.setObjectName("lineEdit_scramble")
        self.lineEdit_scramble.setStyleSheet("background : lightblue;")
        self.stackedWidget = QtWidgets.QStackedWidget(self.tab_scramble)
        self.stackedWidget.setGeometry(QtCore.QRect(590, 120, 461, 80))
        self.stackedWidget.setObjectName("stackedWidget")
        self.tabWidget.addTab(self.tab_scramble, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 26))
        self.menubar.setObjectName("menubar")
        self.menuNew_Words = QtWidgets.QMenu(self.menubar)
        self.menuNew_Words.setObjectName("menuNew_Words")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_Words = QtWidgets.QAction(MainWindow)
        self.actionAdd_Words.setObjectName("actionAdd_Words")
        self.actionAdd_Words.setText("Add Words")
        self.actionRemove_Words = QtWidgets.QAction(MainWindow)
        self.actionRemove_Words.setObjectName("actionRemove_Words")
        self.actionRemove_Words.setText("Remove Words")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setText("Exit")
        self.menuNew_Words.addSeparator()
        self.menuNew_Words.addAction(self.actionAdd_Words)
        self.menuNew_Words.addAction(self.actionRemove_Words)
        self.menuExit.addAction(self.actionExit)
        self.menubar.addAction(self.menuNew_Words.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ########### FUTURE USE ################
        #self.tab_practice = QtWidgets.QWidget()    
        #self.tab_practice.setObjectName("tab_practice")
        #self.tabWidget.addTab(self.tab_practice, "")
        #self.tab_test = QtWidgets.QWidget()
        #self.tab_test.setObjectName("tab_test")
        #self.tabWidget.addTab(self.tab_test, "")
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_speak.setText(_translate("MainWindow", "SPEAK"))
        self.btn_validate.setText(_translate("MainWindow", "Validate"))
        self.label_1.setText(_translate("MainWindow", "Scrambled Word"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_scramble), _translate("MainWindow", "Word Scramble"))
        self.menuNew_Words.setTitle(_translate("MainWindow", "New Words"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))
        
        ########### FUTURE USE  #############
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_practice), _translate("MainWindow", "Practice"))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_test), _translate("MainWindow", "Test"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())