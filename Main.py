import sys
from PyQt4.QtGui import QApplication, QDialog
from GUI import Ui_Dialog  # here you need to correct the names
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os
import sqlite3
from Methods import *

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Dialog()
ui.setupUi(window)

def StartExam():  # Order:(db, cursor, hive, TableName, regPath,  Key, Category, single or subdir, text):
    filename = QFileDialog.getExistingDirectory()

    db = sqlite3.connect(":memory:")
    cursor = db.cursor()
    cursor.execute(    '''CREATE TABLE Info(Id INTEGER PRIMARY KEY, Name TEXT, Value TEXT,Category TEXT, State TEXT, Keystr TEXT, RecString TEXT, KeyParent TEXT, KeyTimeStamp TEXT, MRUOrder INTEGER)''')
    ReadAllReg(db, cursor, filename + "\\NTUSER.DAT", "Info",
                   r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths", "User", "SubDir","Typed Paths")  # Typed Paths
    ReadAllReg(db, cursor, filename + "\\SOFTWARE", "Info", r"Microsoft\Windows NT\CurrentVersion", "OS", "SubDir", "Operating System Information")
    ReadAllReg(db, cursor, filename + "\\SYSTEM", "Info", "MountedDevices", "OS", "SubDir", "Mounted Devices")  # Mounted devices
    ReadSingleReg(db, cursor, filename + "\\SYSTEM", "Info", "Select", "Current", "OS", "Single", "Operating System Information")  # CurrentControlSet
    ReadAllRegSubdir(db, cursor, filename + "\\NTUSER.DAT", "Info", r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU", "User",
                         "SubDirRec", "OpenSavePidlMRU") #OpenSavePidlMRU

    
    #Tab 2 Operating System Information
    rowcount = cursor.execute('''SELECT COUNT(Keystr) FROM Info WHERE Keystr IS "Operating System Information"''').fetchone()[0]
    
    ui.tableWidget_OS.setRowCount(rowcount)
    ui.tableWidget_OS.setHorizontalHeaderLabels(QString("ID;Name;Value;Category;State;Keystr;RecString;KeyParent;KeyTimeStamp;MRUOrder").split(";"))
    cursor.execute('''SELECT * FROM %s WHERE Keystr IS "Operating System Information" ORDER BY KeyParent,MRUOrder''' % "Info")
    for row1, form in enumerate(cursor):
        for column, item in enumerate(form):
            #if form[5] == "Operating System Information":
            ui.tableWidget_OS.setItem(row1, column, QTableWidgetItem(str(item)))   
    #End tab Operating System Information
    #Tab 3 OpenSavePidlMRU
    rowcount = cursor.execute('''SELECT COUNT(Keystr) FROM Info WHERE Keystr IS "OpenSavePidlMRU"''').fetchone()[0]
    
    ui.tableWidget_OpenSavePidlMRU.setRowCount(rowcount)
    ui.tableWidget_OpenSavePidlMRU.setHorizontalHeaderLabels(QString("ID;Name;Value;Category;State;Keystr;RecString;KeyParent;KeyTimeStamp;MRUOrder").split(";"))
    cursor.execute('''SELECT * FROM %s WHERE Keystr IS "OpenSavePidlMRU" ORDER BY KeyParent,MRUOrder''' % "Info")
    for row1, form in enumerate(cursor):
        for column, item in enumerate(form):
            #if form[5] == "OpenSavePidlMRU":
            ui.tableWidget_OpenSavePidlMRU.setItem(row1, column, QTableWidgetItem(str(item)))   
    #End tab opensavepidlmru
    #Tab  mounted devices
    rowcount = cursor.execute('''SELECT COUNT(Keystr) FROM Info WHERE Keystr IS "Mounted Devices"''').fetchone()[0]
    
    ui.tableWidget_MountedDevices.setRowCount(rowcount)
    ui.tableWidget_MountedDevices.setHorizontalHeaderLabels(QString("ID;Name;Value;Category;State;Keystr;RecString;KeyParent;KeyTimeStamp;MRUOrder").split(";"))
    cursor.execute('''SELECT * FROM %s WHERE Keystr IS "Mounted Devices" ORDER BY Name''' % "Info")
    for row1, form in enumerate(cursor):
        for column, item in enumerate(form):
            #if form[5] == "Mounted Devices":
            ui.tableWidget_MountedDevices.setItem(row1, column, QTableWidgetItem(str(item)))   
    #End tab mounted devices
    #Tab TypedPaths
    rowcount = cursor.execute('''SELECT COUNT(Keystr) FROM Info WHERE Keystr IS "Typed Paths"''').fetchone()[0]
    
    ui.tableWidget_TypedPaths.setRowCount(rowcount)
    ui.tableWidget_TypedPaths.setHorizontalHeaderLabels(QString("ID;Name;Value;Category;State;Keystr;RecString;KeyParent;KeyTimeStamp;MRUOrder").split(";"))
    cursor.execute('''SELECT * FROM %s WHERE Keystr IS "Typed Paths" ORDER BY Name''' % "Info")
    for row1, form in enumerate(cursor):
        for column, item in enumerate(form):
            #if form[5] == "Typed Paths":
            ui.tableWidget_TypedPaths.setItem(row1, column, QTableWidgetItem(str(item)))   
    #TODO Make it sort according to MRUListEx
    #End tab TypedPaths

ui.button_Start_Exam.pressed.connect(StartExam)
ui.button_Exit.pressed.connect(exit)
window.showMaximized()
sys.exit(app.exec_())