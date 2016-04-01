# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\Tabbed grid.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(950, 705)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 931, 621))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tableWidget = QtGui.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 931, 601))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tableWidget_OS = QtGui.QTableWidget(self.tab_2)
        self.tableWidget_OS.setGeometry(QtCore.QRect(0, 0, 931, 601))
        self.tableWidget_OS.setObjectName(_fromUtf8("tableWidget_OS"))
        self.tableWidget_OS.setColumnCount(10)
        self.tableWidget_OS.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_OS.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_OS.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_OS.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_OS.setHorizontalHeaderItem(1, item)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        #Tab 3 OpenSavePidlMRU
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.TableWidget_OpenSavePidlMRU = QtGui.QTableWidget(self.tab_3)
        self.TableWidget_OpenSavePidlMRU.setGeometry(QtCore.QRect(0, 0, 931, 601))
        self.TableWidget_OpenSavePidlMRU.setObjectName(_fromUtf8("tableWidget_OS"))
        self.TableWidget_OpenSavePidlMRU.setColumnCount(10)
        self.TableWidget_OpenSavePidlMRU.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.TableWidget_OpenSavePidlMRU.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.TableWidget_OpenSavePidlMRU.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.TableWidget_OpenSavePidlMRU.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.TableWidget_OpenSavePidlMRU.setHorizontalHeaderItem(1, item)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        #End tab 3
        self.splitter = QtGui.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(20, 650, 225, 23))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.button_Start_Exam = QtGui.QPushButton(self.splitter)
        self.button_Start_Exam.setObjectName(_fromUtf8("pushButton_2"))
        self.button_Exit = QtGui.QPushButton(self.splitter)
        self.button_Exit.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.tabWidget.setCurrentIndex(0)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Start", None))
        item = self.tableWidget_OS.verticalHeaderItem(0)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Operating System Information", None))
        #Tab 3 OpenSavePidlMRU
        item = self.TableWidget_OpenSavePidlMRU.verticalHeaderItem(0)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "OpenSavePidlMRU", None))
        self.button_Start_Exam.setText(_translate("Dialog", "Start", None))
        self.button_Exit.setText(_translate("Dialog", "Exit", None))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    f = Ui_Dialog(object)
    f.Show()
    app.setMainWidget(f)
    app.exec_loop()
