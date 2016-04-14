from Main import *
def makeTabs(cursor, tabWidget,tabWidget_RegistrySubTabs, ui ):
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
        ui.tabWidget.addTab(ui.tab_Registry, "Registry")
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
    if rowcount > 0:
        ui.tabWidget.addTab(ui.tab_Registry, "Registry")
        ui.tabWidget_RegistrySubTabs.addTab(ui.tableWidget_TypedPaths, "TypedPaths")
        ui.tableWidget_TypedPaths.setRowCount(rowcount)
        ui.tableWidget_TypedPaths.setHorizontalHeaderLabels(QString("Name;Value;KeyTimeStamp;Source").split(";"))
        cursor.execute('''SELECT  Name,Value,KeyTimeStamp,Source FROM %s WHERE Keystr IS "Typed Paths" ORDER BY Name''' % "Info")
        for row1, form in enumerate(cursor):
            for column, item in enumerate(form):
                #if form[5] == "Mounted Devices":
                ui.tableWidget_TypedPaths.setItem(row1, column, QTableWidgetItem(str(item))) 
        ui.tableWidget_TypedPaths.resizeColumnsToContents()