import sys
from PyQt4.QtGui import QApplication, QDialog
from test2 import Ui_Dialog  # here you need to correct the names
from PyQt4.QtCore import pyqtSlot
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
                   r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths", "User", "SubDir","Typed Urls")  # Typed Paths
    ReadAllReg(db, cursor, filename + "\\SOFTWARE", "Info", r"Microsoft\Windows NT\CurrentVersion", "OS", "SubDir", "Operating System Information")
    ReadAllReg(db, cursor, filename + "\\SYSTEM", "Info", "MountedDevices", "OS", "SubDir", "Mounted Devices")  # Mounted devices
    ReadSingleReg(db, cursor, filename + "\\SYSTEM", "Info", "Select", "Current", "OS", "Single", "Operating System Information")  # CurrentControlSet
    ReadAllRegSubdir(db, cursor, filename + "\\NTUSER.DAT", "Info",
                         r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU", "User",
                         "SubDirRec", "Recent files (ComDlg32)")

    #cursor.execute('''SELECT * FROM %s ORDER BY KeyParent,MRUOrder''' % "Info")
   
    rowcount = cursor.execute('''SELECT COUNT(*) FROM Info ORDER BY KeyParent,MRUOrder''').fetchone()[0]
    ui.tableWidget_OS.setRowCount(rowcount)

    cursor.execute('''SELECT * FROM %s ORDER BY KeyParent,MRUOrder''' % "Info")
    for row1, form in enumerate(cursor):
        for column, item in enumerate(form):
            #if form[5] == "Operating System Information":
            ui.tableWidget_OS.setItem(row1, column, QTableWidgetItem(str(item)))   

ui.button_Start_Exam.pressed.connect(StartExam)
ui.button_Exit.pressed.connect(exit)
window.show()
sys.exit(app.exec_())