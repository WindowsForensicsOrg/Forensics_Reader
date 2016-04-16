import sys
import struct
from GUI import Ui_Dialog  # here you need to correct the names
from PyQt4.QtCore import * 
import PyQt4.QtCore as QtCore
from PyQt4.QtGui import *
import os
import sqlite3
from Methods import *
from makeTabs import *
from userassist import *


app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Dialog()
ui.setupUi(window)



def StartExam():  # Order:(db, cursor, hive, TableName, Source,  Key, Category, single or subdir, text):
    filename = QFileDialog.getExistingDirectory()

    db = sqlite3.connect(":memory:")
    db.text_factory = str
    cursor = db.cursor()
    ui.msgLabel.setText("Processing.....  ")
    app.processEvents()
    cursor.execute(    '''CREATE TABLE Info(Id INTEGER PRIMARY KEY, Name TEXT, Value TEXT,Category TEXT, State TEXT, Keystr TEXT, RecString TEXT, KeyParent TEXT, KeyTimeStamp TEXT, MRUOrder INTEGER, MFT INTEGER, Source TEXT)''')
    
    if os.access(filename + "\\NTUSER.DAT", os.R_OK): 
        ReadAllReg(db, cursor, filename + "\\NTUSER.DAT", "Info",
                       r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths", "User", "SubDir","Typed Paths")  # Typed Paths
        ReadAllRegSubdir(db, cursor, filename + "\\NTUSER.DAT", "Info", r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU", "User",
                         "SubDirRec", "OpenSavePidlMRU") #OpenSavePidlMRU
    if os.access(filename + "\\NTUSER.DAT", os.R_OK) and os.access(filename + "\\SOFTWARE", os.R_OK):
       cursor.execute(    '''CREATE TABLE UserAssistTable(Id INTEGER PRIMARY KEY, Name TEXT, focus TEXT, RunCount INTEGER, LastRun TEXT, Folderdata TEXT, Source TEXT)''')
       UserAssist(db, cursor, filename + "\\NTUSER.DAT", filename + "\\SOFTWARE")
    if os.access(filename + "\\SOFTWARE", os.R_OK): 
        ReadAllReg(db, cursor, filename + "\\SOFTWARE", "Info", r"Microsoft\Windows NT\CurrentVersion", "OS", "SubDir", "Operating System Information")
    if os.access(filename + "\\SYSTEME", os.R_OK): 
        ReadAllReg(db, cursor, filename + "\\SYSTEM", "Info", "MountedDevices", "OS", "SubDir", "Mounted Devices")  # Mounted devices
        ReadSingleReg(db, cursor, filename + "\\SYSTEM", "Info", "Select", "Current", "OS", "Single", "Operating System Information")  # CurrentControlSet
    

    ui.msgLabel.setText("Done")
    app.processEvents()
    #Order: ID;Name;Value;Category;State;Keystr;RecString;KeyParent;KeyTimeStamp;MRUOrder;MRU
  
    makeTabs(cursor, ui.tabWidget,ui.tabWidget_RegistrySubTabs, ui) #makeTabs.py 



def main():
    db.commit()
    db.close()
if __name__ == "__main__":
   
    
    ui.button_Start_Exam.clicked.connect(StartExam)
    ui.button_Exit.clicked.connect(sys.exit)

    items = ui.tabWidget.count()
    itemsRegistry = ui.tabWidget_RegistrySubTabs.count()
    for w1 in range(0,itemsRegistry):
        for i in range(0,itemsRegistry):  
            ui.tabWidget_RegistrySubTabs.removeTab(w1)
    for w1 in range(1,items):
        for i in range(1,items):  
            ui.tabWidget.removeTab(w1)

    window.show()#showMaximized()  
    sys.exit(app.exec_())