from Main import *
def recOpenSavePidlMRU(key, cursor, TableName, Category, stateStr, KeyStr,Source):
   
    for subkey in key.subkeys():
        subkeyName = subkey.name()
        list1 = []
        MFT = ''
        cursor.execute(
            '''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent,KeyTimeStamp,MFT,Source) VALUES(?,?,?,?,?,?,?,?,?,?)''' % TableName,
            [subkey.name(), "", Category, stateStr, KeyStr, "Folder", subkey.name(), subkey.timestamp(), MFT,Source])
        blockstart = 0
        successfull = False

        while not successfull:
            for value1 in [v for v in subkey.values()]:
                if value1.name() == "MRUListEx":
                     list1 = MRUListExSort(list1, value1, successfull)
                     successfull = True

        
        for value in [v for v in subkey.values()]:
            if value.name() != "MRUListEx":
                ComDlg = openSavePidlMRU(value, subkeyName)
                
                MFT = ComDlg[1]
                
                filePath = ComDlg[0]
                indexnum = 0


                for p in list1: #print "www %d %s %d %d" % (int(p), value.name(),list1.index(int(value.name())))
                     i = str_to_int(value.name())
                     if p == i:
                         indexnum = list1.index(p)

                blockstart = 0

                cursor.execute(
                    '''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent, MRUOrder, MFT,Source. KeyTimeStamp) VALUES(?,?,?,?,?,?,?,?,?,?)''' % TableName,
                    [value.name(), filePath, Category, stateStr, KeyStr, "Key",subkey.name(),indexnum, MFT,Source, ""])
    



def OpenSavePidlMRU(db, cursor, Hive, TableName, Source, Category, stateStr, KeyStr):
    reg = Registry.Registry(Hive)
    try:
        key = reg.open(Source)
        Source = "From: {} and registry path: {}".format(Hive, Source)
    except Registry.RegistryKeyNotFoundException:
        print "Couldn't find %s..." % Source
    try:

        recOpenSavePidlMRU(key, cursor, TableName, Category, stateStr, KeyStr, Source)


    except Exception,e: print str(e), "Couldn't send to rec (ReadAllRegSubdir)"
