# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
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
        Dialog.resize(1181, 852)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(1181, 0))
        Dialog.setAutoFillBackground(True)
        Dialog.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #616161, stop: 0.5 #505050,\n"
"                                      stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    \n"
"}"))
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 100000))
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setAutoFillBackground(True)
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_14 = QtGui.QGridLayout(self.tab)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.textEdit = QtGui.QTextEdit(self.tab)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout_14.addWidget(self.textEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_OS = QtGui.QWidget()
        self.tab_OS.setAutoFillBackground(True)
        self.tab_OS.setObjectName(_fromUtf8("tab_OS"))
        self.gridLayout = QtGui.QGridLayout(self.tab_OS)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidget_OS = QtGui.QTableWidget(self.tab_OS)
        self.tableWidget_OS.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_OS.sizePolicy().hasHeightForWidth())
        self.tableWidget_OS.setSizePolicy(sizePolicy)
        self.tableWidget_OS.setMinimumSize(QtCore.QSize(600, 650))
        self.tableWidget_OS.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget_OS.setAutoFillBackground(True)
        self.tableWidget_OS.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #616161, stop: 0.5 #505050,\n"
"                                      stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    \n"
"}"))
        self.tableWidget_OS.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_OS.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tableWidget_OS.setColumnCount(4)
        self.tableWidget_OS.setObjectName(_fromUtf8("tableWidget_OS"))
        self.tableWidget_OS.setRowCount(0)
        self.tableWidget_OS.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget_OS, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_OS, _fromUtf8(""))
        self.tab_Registry = QtGui.QWidget()
        self.tab_Registry.setAutoFillBackground(True)
        self.tab_Registry.setObjectName(_fromUtf8("tab_Registry"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_Registry)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.tabWidget_RegistrySubTabs = QtGui.QTabWidget(self.tab_Registry)
        self.tabWidget_RegistrySubTabs.setAutoFillBackground(True)
        self.tabWidget_RegistrySubTabs.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #616161, stop: 0.5 #505050,\n"
"                                      stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    \n"
"}"))
        self.tabWidget_RegistrySubTabs.setObjectName(_fromUtf8("tabWidget_RegistrySubTabs"))
        self.tab_MountedDevices = QtGui.QWidget()
        self.tab_MountedDevices.setAutoFillBackground(True)
        self.tab_MountedDevices.setObjectName(_fromUtf8("tab_MountedDevices"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_MountedDevices)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tableWidget_MountedDevices = QtGui.QTableWidget(self.tab_MountedDevices)
        self.tableWidget_MountedDevices.setEnabled(False)
        self.tableWidget_MountedDevices.setAutoFillBackground(True)
        self.tableWidget_MountedDevices.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #616161, stop: 0.5 #505050,\n"
"                                      stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    \n"
"}"))
        self.tableWidget_MountedDevices.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_MountedDevices.setColumnCount(4)
        self.tableWidget_MountedDevices.setObjectName(_fromUtf8("tableWidget_MountedDevices"))
        self.tableWidget_MountedDevices.setRowCount(0)
        self.tableWidget_MountedDevices.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_3.addWidget(self.tableWidget_MountedDevices, 0, 0, 1, 1)
        self.tabWidget_RegistrySubTabs.addTab(self.tab_MountedDevices, _fromUtf8(""))
        self.tab_OpenSavePidMRU = QtGui.QWidget()
        self.tab_OpenSavePidMRU.setAutoFillBackground(True)
        self.tab_OpenSavePidMRU.setObjectName(_fromUtf8("tab_OpenSavePidMRU"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_OpenSavePidMRU)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.tableWidget_OpenSavePidlMRU = QtGui.QTableWidget(self.tab_OpenSavePidMRU)
        self.tableWidget_OpenSavePidlMRU.setEnabled(False)
        self.tableWidget_OpenSavePidlMRU.setAutoFillBackground(True)
        self.tableWidget_OpenSavePidlMRU.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #616161, stop: 0.5 #505050,\n"
"                                      stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    \n"
"}"))
        self.tableWidget_OpenSavePidlMRU.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_OpenSavePidlMRU.setColumnCount(5)
        self.tableWidget_OpenSavePidlMRU.setObjectName(_fromUtf8("tableWidget_OpenSavePidlMRU"))
        self.tableWidget_OpenSavePidlMRU.setRowCount(0)
        self.tableWidget_OpenSavePidlMRU.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_OpenSavePidlMRU.verticalHeader().setStretchLastSection(True)
        self.gridLayout_5.addWidget(self.tableWidget_OpenSavePidlMRU, 0, 0, 1, 1)
        self.tabWidget_RegistrySubTabs.addTab(self.tab_OpenSavePidMRU, _fromUtf8(""))
        self.tab_TypedPaths = QtGui.QWidget()
        self.tab_TypedPaths.setAutoFillBackground(True)
        self.tab_TypedPaths.setObjectName(_fromUtf8("tab_TypedPaths"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_TypedPaths)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.tableWidget_TypedPaths = QtGui.QTableWidget(self.tab_TypedPaths)
        self.tableWidget_TypedPaths.setEnabled(False)
        self.tableWidget_TypedPaths.setAutoFillBackground(True)
        self.tableWidget_TypedPaths.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #616161, stop: 0.5 #505050,\n"
"                                      stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    \n"
"}"))
        self.tableWidget_TypedPaths.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_TypedPaths.setColumnCount(4)
        self.tableWidget_TypedPaths.setObjectName(_fromUtf8("tableWidget_TypedPaths"))
        self.tableWidget_TypedPaths.setRowCount(0)
        self.tableWidget_TypedPaths.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_6.addWidget(self.tableWidget_TypedPaths, 0, 0, 1, 1)
        self.tabWidget_RegistrySubTabs.addTab(self.tab_TypedPaths, _fromUtf8(""))
        self.tab_UserAssist = QtGui.QWidget()
        self.tab_UserAssist.setAutoFillBackground(True)
        self.tab_UserAssist.setObjectName(_fromUtf8("tab_UserAssist"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_UserAssist)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tableWidget_UserAssist = QtGui.QTableWidget(self.tab_UserAssist)
        self.tableWidget_UserAssist.setEnabled(False)
        self.tableWidget_UserAssist.setAutoFillBackground(True)
        self.tableWidget_UserAssist.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #616161, stop: 0.5 #505050,\n"
"                                      stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    \n"
"}"))
        self.tableWidget_UserAssist.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_UserAssist.setColumnCount(4)
        self.tableWidget_UserAssist.setObjectName(_fromUtf8("tableWidget_UserAssist"))
        self.tableWidget_UserAssist.setRowCount(0)
        self.tableWidget_UserAssist.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.tableWidget_UserAssist, 0, 0, 1, 1)
        self.tabWidget_RegistrySubTabs.addTab(self.tab_UserAssist, _fromUtf8(""))
        self.tab_RecentDocs = QtGui.QWidget()
        self.tab_RecentDocs.setAutoFillBackground(True)
        self.tab_RecentDocs.setObjectName(_fromUtf8("tab_RecentDocs"))
        self.gridLayout_13 = QtGui.QGridLayout(self.tab_RecentDocs)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.tableWidget_RecentDocs = QtGui.QTableWidget(self.tab_RecentDocs)
        self.tableWidget_RecentDocs.setEnabled(False)
        self.tableWidget_RecentDocs.setAutoFillBackground(True)
        self.tableWidget_RecentDocs.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #616161, stop: 0.5 #505050,\n"
"                                      stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    \n"
"}"))
        self.tableWidget_RecentDocs.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_RecentDocs.setColumnCount(4)
        self.tableWidget_RecentDocs.setObjectName(_fromUtf8("tableWidget_RecentDocs"))
        self.tableWidget_RecentDocs.setRowCount(0)
        self.tableWidget_RecentDocs.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_13.addWidget(self.tableWidget_RecentDocs, 0, 0, 1, 1)
        self.tabWidget_RegistrySubTabs.addTab(self.tab_RecentDocs, _fromUtf8(""))
        self.gridLayout_4.addWidget(self.tabWidget_RegistrySubTabs, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_Registry, _fromUtf8(""))
        self.tab_Jumplists = QtGui.QWidget()
        self.tab_Jumplists.setAutoFillBackground(True)
        self.tab_Jumplists.setObjectName(_fromUtf8("tab_Jumplists"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_Jumplists)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.tableWidget_JumpLists = QtGui.QTableWidget(self.tab_Jumplists)
        self.tableWidget_JumpLists.setEnabled(False)
        self.tableWidget_JumpLists.setAutoFillBackground(True)
        self.tableWidget_JumpLists.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #616161, stop: 0.5 #505050,\n"
"                                      stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    \n"
"}"))
        self.tableWidget_JumpLists.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_JumpLists.setColumnCount(4)
        self.tableWidget_JumpLists.setObjectName(_fromUtf8("tableWidget_JumpLists"))
        self.tableWidget_JumpLists.setRowCount(0)
        self.tableWidget_JumpLists.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_7.addWidget(self.tableWidget_JumpLists, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_Jumplists, _fromUtf8(""))
        self.tab_Prefetch = QtGui.QWidget()
        self.tab_Prefetch.setAutoFillBackground(True)
        self.tab_Prefetch.setObjectName(_fromUtf8("tab_Prefetch"))
        self.gridLayout_8 = QtGui.QGridLayout(self.tab_Prefetch)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.tableWidget_Prefetch = QtGui.QTableWidget(self.tab_Prefetch)
        self.tableWidget_Prefetch.setEnabled(False)
        self.tableWidget_Prefetch.setAutoFillBackground(True)
        self.tableWidget_Prefetch.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #616161, stop: 0.5 #505050,\n"
"                                      stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    \n"
"}"))
        self.tableWidget_Prefetch.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_Prefetch.setColumnCount(4)
        self.tableWidget_Prefetch.setObjectName(_fromUtf8("tableWidget_Prefetch"))
        self.tableWidget_Prefetch.setRowCount(0)
        self.tableWidget_Prefetch.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_8.addWidget(self.tableWidget_Prefetch, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_Prefetch, _fromUtf8(""))
        self.tab_RecentFolder = QtGui.QWidget()
        self.tab_RecentFolder.setAutoFillBackground(True)
        self.tab_RecentFolder.setObjectName(_fromUtf8("tab_RecentFolder"))
        self.gridLayout_9 = QtGui.QGridLayout(self.tab_RecentFolder)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.tableWidget_RecentFolder = QtGui.QTableWidget(self.tab_RecentFolder)
        self.tableWidget_RecentFolder.setEnabled(False)
        self.tableWidget_RecentFolder.setAutoFillBackground(True)
        self.tableWidget_RecentFolder.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #616161, stop: 0.5 #505050,\n"
"                                      stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    \n"
"}"))
        self.tableWidget_RecentFolder.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_RecentFolder.setColumnCount(4)
        self.tableWidget_RecentFolder.setObjectName(_fromUtf8("tableWidget_RecentFolder"))
        self.tableWidget_RecentFolder.setRowCount(0)
        self.tableWidget_RecentFolder.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_9.addWidget(self.tableWidget_RecentFolder, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_RecentFolder, _fromUtf8(""))
        self.tab_EventLog = QtGui.QWidget()
        self.tab_EventLog.setAutoFillBackground(True)
        self.tab_EventLog.setObjectName(_fromUtf8("tab_EventLog"))
        self.gridLayout_10 = QtGui.QGridLayout(self.tab_EventLog)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.tableWidget_EventLogs = QtGui.QTableWidget(self.tab_EventLog)
        self.tableWidget_EventLogs.setEnabled(False)
        self.tableWidget_EventLogs.setAutoFillBackground(True)
        self.tableWidget_EventLogs.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #616161, stop: 0.5 #505050,\n"
"                                      stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    \n"
"}"))
        self.tableWidget_EventLogs.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_EventLogs.setColumnCount(4)
        self.tableWidget_EventLogs.setObjectName(_fromUtf8("tableWidget_EventLogs"))
        self.tableWidget_EventLogs.setRowCount(0)
        self.tableWidget_EventLogs.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_EventLogs.verticalHeader().setStretchLastSection(False)
        self.gridLayout_10.addWidget(self.tableWidget_EventLogs, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_EventLog, _fromUtf8(""))
        self.tab_WebCacheV01 = QtGui.QWidget()
        self.tab_WebCacheV01.setAutoFillBackground(True)
        self.tab_WebCacheV01.setObjectName(_fromUtf8("tab_WebCacheV01"))
        self.gridLayout_11 = QtGui.QGridLayout(self.tab_WebCacheV01)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.tableWidget_WebCacheV01 = QtGui.QTableWidget(self.tab_WebCacheV01)
        self.tableWidget_WebCacheV01.setEnabled(False)
        self.tableWidget_WebCacheV01.setAutoFillBackground(True)
        self.tableWidget_WebCacheV01.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #616161, stop: 0.5 #505050,\n"
"                                      stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    \n"
"}"))
        self.tableWidget_WebCacheV01.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_WebCacheV01.setColumnCount(4)
        self.tableWidget_WebCacheV01.setObjectName(_fromUtf8("tableWidget_WebCacheV01"))
        self.tableWidget_WebCacheV01.setRowCount(0)
        self.tableWidget_WebCacheV01.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_11.addWidget(self.tableWidget_WebCacheV01, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_WebCacheV01, _fromUtf8(""))
        self.tab_USB = QtGui.QWidget()
        self.tab_USB.setAutoFillBackground(True)
        self.tab_USB.setObjectName(_fromUtf8("tab_USB"))
        self.gridLayout_12 = QtGui.QGridLayout(self.tab_USB)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.tableWidget_USB = QtGui.QTableWidget(self.tab_USB)
        self.tableWidget_USB.setEnabled(False)
        self.tableWidget_USB.setAutoFillBackground(True)
        self.tableWidget_USB.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #616161, stop: 0.5 #505050,\n"
"                                      stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    \n"
"}"))
        self.tableWidget_USB.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_USB.setColumnCount(4)
        self.tableWidget_USB.setObjectName(_fromUtf8("tableWidget_USB"))
        self.tableWidget_USB.setRowCount(0)
        self.tableWidget_USB.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_USB.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_12.addWidget(self.tableWidget_USB, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_USB, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.splitter = QtGui.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.button_Start_Exam = QtGui.QPushButton(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_Start_Exam.sizePolicy().hasHeightForWidth())
        self.button_Start_Exam.setSizePolicy(sizePolicy)
        self.button_Start_Exam.setMinimumSize(QtCore.QSize(50, 30))
        self.button_Start_Exam.setMaximumSize(QtCore.QSize(100, 50))
        self.button_Start_Exam.setObjectName(_fromUtf8("button_Start_Exam"))
        self.button_Exit = QtGui.QPushButton(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_Exit.sizePolicy().hasHeightForWidth())
        self.button_Exit.setSizePolicy(sizePolicy)
        self.button_Exit.setMinimumSize(QtCore.QSize(50, 30))
        self.button_Exit.setMaximumSize(QtCore.QSize(100, 50))
        self.button_Exit.setObjectName(_fromUtf8("button_Exit"))
        self.msgLabel = QtGui.QLabel(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msgLabel.sizePolicy().hasHeightForWidth())
        self.msgLabel.setSizePolicy(sizePolicy)
        self.msgLabel.setText(_fromUtf8(""))
        self.msgLabel.setObjectName(_fromUtf8("msgLabel"))
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(8)
        self.tabWidget_RegistrySubTabs.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Welcome bla bla</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">This is the übertool.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">This age will be replaced by something cool</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_OS), _translate("Dialog", "Operating System Information", None))
        self.tabWidget_RegistrySubTabs.setTabText(self.tabWidget_RegistrySubTabs.indexOf(self.tab_MountedDevices), _translate("Dialog", "Mounted Devices", None))
        self.tabWidget_RegistrySubTabs.setTabText(self.tabWidget_RegistrySubTabs.indexOf(self.tab_OpenSavePidMRU), _translate("Dialog", "OpenSavePidlMRU", None))
        self.tabWidget_RegistrySubTabs.setTabText(self.tabWidget_RegistrySubTabs.indexOf(self.tab_TypedPaths), _translate("Dialog", "Typed Paths", None))
        self.tabWidget_RegistrySubTabs.setTabText(self.tabWidget_RegistrySubTabs.indexOf(self.tab_UserAssist), _translate("Dialog", "UserAssist", None))
        self.tabWidget_RegistrySubTabs.setTabText(self.tabWidget_RegistrySubTabs.indexOf(self.tab_RecentDocs), _translate("Dialog", "RecentDocs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Registry), _translate("Dialog", "Registry", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Jumplists), _translate("Dialog", "Jumplists", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Prefetch), _translate("Dialog", "Prefetch", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_RecentFolder), _translate("Dialog", "Recent Folder", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_EventLog), _translate("Dialog", "EventLogs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_WebCacheV01), _translate("Dialog", "WebCacheV01", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_USB), _translate("Dialog", "USB", None))
        self.button_Start_Exam.setText(_translate("Dialog", "Start", None))
        self.button_Exit.setText(_translate("Dialog", "Exit", None))

