# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Google Drev\Div\GUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
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
        Dialog.resize(1967, 1724)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(True)
        sizePolicy.setVerticalStretch(True)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        layout = QHBoxLayout(dialog)
        layout.addWidget(textbox)
        Dialog.setLayout(layout)

        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 0, 981, 741))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout = QtGui.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.horizontalLayout.addLayout(self.formLayout)
        self.tableWidget_OS = QtGui.QTableWidget(self.tab_2)
        self.tableWidget_OS.setColumnCount(10)
        self.tableWidget_OS.setObjectName(_fromUtf8("tableWidget_OS"))
        self.tableWidget_OS.setRowCount(0)
        self.tableWidget_OS.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_OS.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout.addWidget(self.tableWidget_OS)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_Registry = QtGui.QWidget()
        self.tab_Registry.setObjectName(_fromUtf8("tab_Registry"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_Registry)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget_juser = QtGui.QTabWidget(self.tab_Registry)
        self.tabWidget_juser.setObjectName(_fromUtf8("tabWidget_juser"))
        self.tab_MountedDevices = QtGui.QWidget()
        self.tab_MountedDevices.setObjectName(_fromUtf8("tab_MountedDevices"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.tab_MountedDevices)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.tableWidget_MountedDevices = QtGui.QTableWidget(self.tab_MountedDevices)
        self.tableWidget_MountedDevices.setColumnCount(10)
        self.tableWidget_MountedDevices.setObjectName(_fromUtf8("tableWidget_MountedDevices"))
        self.tableWidget_MountedDevices.setRowCount(0)
        self.tableWidget_MountedDevices.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_MountedDevices.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_7.addWidget(self.tableWidget_MountedDevices)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_7)
        self.tabWidget_juser.addTab(self.tab_MountedDevices, _fromUtf8(""))
        self.tab_OpenSavePidMRU = QtGui.QWidget()
        self.tab_OpenSavePidMRU.setObjectName(_fromUtf8("tab_OpenSavePidMRU"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_OpenSavePidMRU)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.tableWidget_OpenSavePidlMRU = QtGui.QTableWidget(self.tab_OpenSavePidMRU)
        self.tableWidget_OpenSavePidlMRU.setColumnCount(10)
        self.tableWidget_OpenSavePidlMRU.setObjectName(_fromUtf8("tableWidget_OpenSavePidlMRU"))
        self.tableWidget_OpenSavePidlMRU.setRowCount(0)
        self.tableWidget_OpenSavePidlMRU.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_OpenSavePidlMRU.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_6.addWidget(self.tableWidget_OpenSavePidlMRU)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.tabWidget_juser.addTab(self.tab_OpenSavePidMRU, _fromUtf8(""))
        self.tab_TypedPaths = QtGui.QWidget()
        self.tab_TypedPaths.setObjectName(_fromUtf8("tab_TypedPaths"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_TypedPaths)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.tableWidget_TypedPaths = QtGui.QTableWidget(self.tab_TypedPaths)
        self.tableWidget_TypedPaths.setColumnCount(10)
        self.tableWidget_TypedPaths.setObjectName(_fromUtf8("tableWidget_TypedPaths"))
        self.tableWidget_TypedPaths.setRowCount(0)
        self.tableWidget_TypedPaths.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_TypedPaths.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_8.addWidget(self.tableWidget_TypedPaths)
        self.gridLayout_4.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.tabWidget_juser.addTab(self.tab_TypedPaths, _fromUtf8(""))
        self.tab_UserAssist = QtGui.QWidget()
        self.tab_UserAssist.setObjectName(_fromUtf8("tab_UserAssist"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_UserAssist)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.horizontalLayout_9.addLayout(self.formLayout_2)
        self.tableWidget_UserAssist = QtGui.QTableWidget(self.tab_UserAssist)
        self.tableWidget_UserAssist.setColumnCount(10)
        self.tableWidget_UserAssist.setObjectName(_fromUtf8("tableWidget_UserAssist"))
        self.tableWidget_UserAssist.setRowCount(0)
        self.tableWidget_UserAssist.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_UserAssist.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_9.addWidget(self.tableWidget_UserAssist)
        self.gridLayout_5.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.tabWidget_juser.addTab(self.tab_UserAssist, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget_juser, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_Registry, _fromUtf8(""))
        self.tab_Jumplists = QtGui.QWidget()
        self.tab_Jumplists.setObjectName(_fromUtf8("tab_Jumplists"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_Jumplists)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tableWidget_JumpLists = QtGui.QTableWidget(self.tab_Jumplists)
        self.tableWidget_JumpLists.setColumnCount(10)
        self.tableWidget_JumpLists.setObjectName(_fromUtf8("tableWidget_JumpLists"))
        self.tableWidget_JumpLists.setRowCount(0)
        self.tableWidget_JumpLists.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_JumpLists.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_3.addWidget(self.tableWidget_JumpLists)
        self.gridLayout_6.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_Jumplists, _fromUtf8(""))
        self.tab_Prefetch = QtGui.QWidget()
        self.tab_Prefetch.setObjectName(_fromUtf8("tab_Prefetch"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_Prefetch)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.tableWidget_Prefetch = QtGui.QTableWidget(self.tab_Prefetch)
        self.tableWidget_Prefetch.setColumnCount(10)
        self.tableWidget_Prefetch.setObjectName(_fromUtf8("tableWidget_Prefetch"))
        self.tableWidget_Prefetch.setRowCount(0)
        self.tableWidget_Prefetch.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_Prefetch.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_4.addWidget(self.tableWidget_Prefetch)
        self.gridLayout_7.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_Prefetch, _fromUtf8(""))
        self.tab_RecentFolder = QtGui.QWidget()
        self.tab_RecentFolder.setObjectName(_fromUtf8("tab_RecentFolder"))
        self.gridLayout_8 = QtGui.QGridLayout(self.tab_RecentFolder)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.tableWidget_Recent_Folder = QtGui.QTableWidget(self.tab_RecentFolder)
        self.tableWidget_Recent_Folder.setColumnCount(10)
        self.tableWidget_Recent_Folder.setObjectName(_fromUtf8("tableWidget_Recent_Folder"))
        self.tableWidget_Recent_Folder.setRowCount(0)
        self.tableWidget_Recent_Folder.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_5.addWidget(self.tableWidget_Recent_Folder)
        self.gridLayout_8.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_RecentFolder, _fromUtf8(""))
        self.button_Start_Exam = QtGui.QPushButton(Dialog)
        self.button_Start_Exam.setGeometry(QtCore.QRect(890, 810, 93, 28))
        self.button_Start_Exam.setObjectName(_fromUtf8("button_Start_Exam"))
        self.button_Cancel = QtGui.QPushButton(Dialog)
        self.button_Cancel.setGeometry(QtCore.QRect(1000, 810, 93, 28))
        self.button_Cancel.setObjectName(_fromUtf8("button_Cancel"))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_juser.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Operating System Information", None))
        self.tabWidget_juser.setTabText(self.tabWidget_juser.indexOf(self.tab_MountedDevices), _translate("Dialog", "Mounted Devices", None))
        self.tabWidget_juser.setTabText(self.tabWidget_juser.indexOf(self.tab_OpenSavePidMRU), _translate("Dialog", "OpenSavePidlMRU", None))
        self.tabWidget_juser.setTabText(self.tabWidget_juser.indexOf(self.tab_TypedPaths), _translate("Dialog", "Typed Paths", None))
        self.tabWidget_juser.setTabText(self.tabWidget_juser.indexOf(self.tab_UserAssist), _translate("Dialog", "UserAssist", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Registry), _translate("Dialog", "Registry", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Jumplists), _translate("Dialog", "Jumplists", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Prefetch), _translate("Dialog", "Prefetch", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_RecentFolder), _translate("Dialog", "Recent Folder", None))
        self.button_Start_Exam.setText(_translate("Dialog", "Start", None))
        self.button_Cancel.setText(_translate("Dialog", "Cancel", None))

