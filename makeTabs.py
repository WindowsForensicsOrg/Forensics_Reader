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
        ui.tableWidget_OS.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)    
        #End tab Operating System Information
    
    #Tab 3 OpenSavePidlMRU
    rowcount = cursor.execute('''SELECT COUNT(*) FROM Info WHERE KeyStr like "%OPenSavePidlMRU%"''').fetchone()[0]
    if rowcount > 0:
        ui.tabWidget.addTab(ui.tab_Registry, "Registry")
        ui.tabWidget_RegistrySubTabs.addTab(ui.tab_OpenSavePidMRU,"OPenSavePidlMRU")
        
        ui.tableWidget_OpenSavePidlMRU.setRowCount(rowcount)
        ui.tableWidget_OpenSavePidlMRU.setHorizontalHeaderLabels(QString("File extension;Key name;Value;KeyTimeStamp;MFT Number;Source").split(";"))
        cursor.execute('''SELECT KeyParent, Name, Value,KeyTimeStamp, MFT, Source FROM %s WHERE Keystr IS "OpenSavePidlMRU" ORDER BY KeyParent,MRUOrder''' % "Info")
        for row1, form in enumerate(cursor):
            for column, item in enumerate(form):
                #if form[5] == "OpenSavePidlMRU":
                if isinstance(item, str):
                    ui.tableWidget_OpenSavePidlMRU.setItem(row1, column, QTableWidgetItem(str(item).decode('utf8')))
                else:
                    ui.tableWidget_OpenSavePidlMRU.setItem(row1, column, QTableWidgetItem(str(item)))  
        ui.tableWidget_OpenSavePidlMRU.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
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
        ui.tableWidget_MountedDevices.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)  
        #End tab mounted devices
    #Tab TypedPaths
    rowcount = cursor.execute('''SELECT COUNT(Keystr) FROM Info WHERE Keystr IS "Typed Paths"''').fetchone()[0]
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
        ui.tableWidget_TypedPaths.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
    #End tab TypedPaths
    #tab_UserAssist
     
    rowcount = cursor.execute('''SELECT COUNT(*) FROM UserAssistTable''').fetchone()[0]
    if rowcount > 0:
        ui.tabWidget.addTab(ui.tab_Registry, "Registry")
        ui.tabWidget_RegistrySubTabs.addTab(ui.tableWidget_UserAssist, "UserAssist")
        ui.tableWidget_UserAssist.setRowCount(rowcount)
        ui.tableWidget_UserAssist.setHorizontalHeaderLabels(QString("Value;Run Count;Last Run;source").split(";"))
        cursor.execute('''SELECT  FolderData, RunCount, LastRun, source FROM UserAssistTable''')
        for row1, form in enumerate(cursor):
            for column, item in enumerate(form):
                ui.tableWidget_UserAssist.setItem(row1, column, QTableWidgetItem(str(item))) 


        ui.tableWidget_UserAssist.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
 
    #End tab_UserAssist   tableResult->horizontalHeader()->setResizeMode(QHeaderView::ResizeToContents);