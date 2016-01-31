# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sun Jan 31 19:07:27 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.chordInputLbl = QtWidgets.QLabel(self.centralwidget)
        self.chordInputLbl.setObjectName("chordInputLbl")
        self.gridLayout.addWidget(self.chordInputLbl, 1, 0, 1, 1)
        self.gammaOutputLbl = QtWidgets.QLabel(self.centralwidget)
        self.gammaOutputLbl.setObjectName("gammaOutputLbl")
        self.gridLayout.addWidget(self.gammaOutputLbl, 3, 0, 1, 1)
        self.chordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.chordInput.setObjectName("chordInput")
        self.gridLayout.addWidget(self.chordInput, 1, 1, 1, 1)
        self.chordOutput = QtWidgets.QLineEdit(self.centralwidget)
        self.chordOutput.setObjectName("chordOutput")
        self.gridLayout.addWidget(self.chordOutput, 4, 1, 1, 1)
        self.goBtn = QtWidgets.QPushButton(self.centralwidget)
        self.goBtn.setObjectName("goBtn")
        self.gridLayout.addWidget(self.goBtn, 6, 0, 1, 1)
        self.exitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitBtn.setObjectName("exitBtn")
        self.gridLayout.addWidget(self.exitBtn, 6, 2, 1, 1)
        self.gammaOutput = QtWidgets.QLineEdit(self.centralwidget)
        self.gammaOutput.setObjectName("gammaOutput")
        self.gridLayout.addWidget(self.gammaOutput, 3, 1, 1, 1)
        self.chordOutputLbl = QtWidgets.QLabel(self.centralwidget)
        self.chordOutputLbl.setObjectName("chordOutputLbl")
        self.gridLayout.addWidget(self.chordOutputLbl, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 2, 6, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 5, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.exitBtn.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chordInputLbl.setText(_translate("MainWindow", "Введите аккорды"))
        self.gammaOutputLbl.setText(_translate("MainWindow", "Гамма"))
        self.goBtn.setText(_translate("MainWindow", "Найти гамму"))
        self.exitBtn.setText(_translate("MainWindow", "Выход"))
        self.chordOutputLbl.setText(_translate("MainWindow", "Аккорды"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

