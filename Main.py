import sys
import struct
from GUI import Ui_Dialog  # here you need to correct the names
from PyQt4.QtCore import * 
import PyQt4.QtCore as QtCore
from PyQt4.QtGui import *
import os
import sqlite3
from Methods import *

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
    
    
    ReadAllReg(db, cursor, filename + "\\NTUSER.DAT", "Info",
                   r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths", "User", "SubDir","Typed Paths")  # Typed Paths
   # ui.msgLabel.setText("Processing  "+ filename+ "\\SOFTWARE " + r"Microsoft\Windows NT\CurrentVersion")
    ReadAllReg(db, cursor, filename + "\\SOFTWARE", "Info", r"Microsoft\Windows NT\CurrentVersion", "OS", "SubDir", "Operating System Information")
    ReadAllReg(db, cursor, filename + "\\SYSTEM", "Info", "MountedDevices", "OS", "SubDir", "Mounted Devices")  # Mounted devices
    ReadSingleReg(db, cursor, filename + "\\SYSTEM", "Info", "Select", "Current", "OS", "Single", "Operating System Information")  # CurrentControlSet
    ReadAllRegSubdir(db, cursor, filename + "\\NTUSER.DAT", "Info", r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU", "User",
                         "SubDirRec", "OpenSavePidlMRU") #OpenSavePidlMRU
    ui.msgLabel.setText("Done")
    app.processEvents()
    #Order: ID;Name;Value;Category;State;Keystr;RecString;KeyParent;KeyTimeStamp;MRUOrder;MRU
    #Tab 2 Operating System Information
    rowcount = cursor.execute('''SELECT COUNT(Keystr) FROM Info WHERE Keystr IS "Operating System Information"''').fetchone()[0]
    if rowcount != 0:
        #interactor = ui.tabWidget.widget(1)
        ui.tabWidget.addTab(ui.tab_OS, "Operating System Information")
        #app.processEvents()
        #ui.tab_OS.
        #interactor..close()
        #interactor.deleteLater()
        ui.tableWidget_OS.setRowCount(rowcount)
        ui.tableWidget_OS.setHorizontalHeaderLabels(QString("Name;Value;KeyTimeStamp;Source").split(";"))
        cursor.execute('''SELECT Name,Value,KeyTimeStamp,Source FROM %s WHERE Keystr IS "Operating System Information" ORDER BY KeyParent,MRUOrder''' % "Info")
        for row1, form in enumerate(cursor):
            for column, item in enumerate(form):
                #if form[5] == "Operating System Information":
                 ui.tableWidget_OS.setItem(row1, column, QTableWidgetItem(str(item))) 
        ui.tableWidget_OS.resizeColumnsToContents()
        
        #End tab Operating System Information
 
    #Tab 3 OpenSavePidlMRU
    rowcount = cursor.execute('''SELECT COUNT(Keystr) FROM Info WHERE Keystr IS "OpenSavePidlMRU"''').fetchone()[0]
    if rowcount > 0:
        ui.tabWidget.addTab(ui.tab_Registry, "Registry")
        ui.tabWidget_RegistrySubTabs.addTab(ui.tab_OpenSavePidMRU,"OPenSavePidlMRU")
        
        ui.tableWidget_OpenSavePidlMRU.setRowCount(rowcount)
        ui.tableWidget_OpenSavePidlMRU.setHorizontalHeaderLabels(QString("Name;Value;KeyTimeStamp;MFT Number;Source").split(";"))
        cursor.execute('''SELECT  Name,Value,KeyTimeStamp, MFT, Source FROM %s WHERE Keystr IS "OpenSavePidlMRU" ORDER BY KeyParent,MRUOrder''' % "Info")
        for row1, form in enumerate(cursor):
            for column, item in enumerate(form):
                #if form[5] == "OpenSavePidlMRU":
                if isinstance(item, str):
                    ui.tableWidget_OpenSavePidlMRU.setItem(row1, column, QTableWidgetItem(str(item).decode('utf8')))
                else:
                    ui.tableWidget_OpenSavePidlMRU.setItem(row1, column, QTableWidgetItem(str(item)))  
        ui.tableWidget_OpenSavePidlMRU.resizeColumnsToContents() # fit columns to content
                #End tab opensavepidlmru
    #Tab  mounted devices
    rowcount = cursor.execute('''SELECT COUNT(Keystr) FROM Info WHERE Keystr IS "Mounted Devices"''').fetchone()[0]
    if rowcount > 0:
        ui.tabWidget_RegistrySubTabs.addTab(ui.tableWidget_MountedDevices, "MountedDevices")
        ui.tableWidget_MountedDevices.setRowCount(rowcount)
        ui.tableWidget_MountedDevices.setHorizontalHeaderLabels(QString("Name;Value;KeyTimeStamp;Source").split(";"))
        cursor.execute('''SELECT  Name,Value,KeyTimeStamp,Source FROM %s WHERE Keystr IS "Mounted Devices" ORDER BY Name''' % "Info")
        for row1, form in enumerate(cursor):
            for column, item in enumerate(form):
                #if form[5] == "Mounted Devices":
                ui.tableWidget_MountedDevices.setItem(row1, column, QTableWidgetItem(str(item))) 
        ui.tableWidget_MountedDevices.resizeColumnsToContents()        
        #End tab mounted devices
    #Tab TypedPaths
    rowcount = cursor.execute('''SELECT COUNT(Keystr) FROM Info WHERE Keystr IS "Typed Paths"''').fetchone()[0]
    if rowcount > 0:
        ui.tabWidget_RegistrySubTabs.addTab(ui.tableWidget_TypedPaths, "TypedPaths")
        ui.tableWidget_TypedPaths.setRowCount(rowcount)
        ui.tableWidget_TypedPaths.setHorizontalHeaderLabels(QString("Name;Value;KeyTimeStamp;Source").split(";"))
        cursor.execute('''SELECT  Name,Value,KeyTimeStamp,Source FROM %s WHERE Keystr IS "Typed Paths" ORDER BY Name''' % "Info")
        for row1, form in enumerate(cursor):
            for column, item in enumerate(form):
                #if form[5] == "Typed Paths":
                ui.tableWidget_TypedPaths.setItem(row1, column, QTableWidgetItem(str(item)))
        ui.tableWidget_TypedPaths.resizeColumnsToContents()    #End tab TypedPaths



def main():
    db.commit()
    db.close()
if __name__ == "__main__":
   
    
    ui.button_Start_Exam.clicked.connect(StartExam)
    ui.button_Exit.clicked.connect(exit)

    items = ui.tabWidget.count()
    itemsRegistry = ui.tabWidget_RegistrySubTabs.count()
    for w1 in range(0,itemsRegistry):
        for i in range(0,itemsRegistry):  
            ui.tabWidget_RegistrySubTabs.removeTab(w1)
    for w1 in range(1,items):
        for i in range(1,items):  
            ui.tabWidget.removeTab(w1)
    
    
        
               
            
  
    #interactor.close()
    #interactor.deleteLater()
    window.show()#showMaximized()

    
    
    sys.exit(app.exec_())