from Registry import Registry
import struct
from datetime import datetime, timedelta
import codecs
import sys
import sqlite3
def UserAssist(db, cursor, ntuser,software):
    softreg = Registry.Registry(software)

    folderDescription_dict = {}

    folderDescription = softreg.open('Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions')

    for subkey in folderDescription.subkeys():
        guid = subkey.name().upper()
        for value in subkey.values():
            if value.name() == 'Name':
                folderDescription_dict[guid] = value.value()


    reg = Registry.Registry(ntuser)
    userassist = 'Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist'

        # Get all guids in UserAssist key
    userassist_subKeyGuids = []

    top = reg.open(userassist)
    for subkeyGuid in top.subkeys():
        userassist_subKeyGuids.append(subkeyGuid.name())


    entries = []
        
    for guid in userassist_subKeyGuids:
        for value in reg.open(userassist).subkey(guid).subkey("Count").values():
                #Windows 7
                if len(value.value()) == 72:
                    runcount = struct.unpack("<I", value.value()[4:8])[0]
                    wintimestamp = struct.unpack("<Q", value.value()[60:68])[0]
                    key = reg.open(userassist).subkey(guid).name()
                    skey = reg.open(userassist).subkey(guid).subkey("Count").name()
                    focus_raw = struct.unpack("<2H", value.value()[12:16])[0]
                    focus = float(focus_raw) / 60000
                    lastrun = convert_wintime(wintimestamp)
                    guiddata = codecs.decode(value.name(), 'rot_13')
                    folderdata = guid_to_folder(guiddata)
                    source = "From: {} and registry path: {}".format(ntuser, userassist)
                    cursor.execute(
                            '''INSERT INTO %s  (Name, Runcount, Lastrun, Folderdata, Focus, Source) VALUES(?,?,?,?,?,?)''' % "UserAssistTable",
                            [guiddata, runcount, lastrun, folderdata, focus,  source])
                           

    


def convert_wintime(windate):
        us = int(windate) / 10
        first_run = datetime(1601,1,1) + timedelta(microseconds=us)
        return first_run

def guid_to_folder(data):
    try:
        if data[:38] in folderDescription_dict:
            guid = data[:38]
            data = folderDescription_dict[guid] + ':\t' + data[39:]
            return data
        else:
            return data
    except:
        return data

 
           
                         

            


           
