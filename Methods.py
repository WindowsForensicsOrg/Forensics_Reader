#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Methods.py
# 0
#  Copyright 2016 ras <sansforensics@siftworkstation>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
# !/usr/bin/python

import binascii
import struct
import uuid
from os import path
from Registry import Registry
from MRUListExSort import MRULIstExSort
from comDlg32 import openSavePidlMRU

def ReadSingleReg(db, cursor, hive, TableName, regPath, Key, Category, stateStr, KeyStr):
    reg = Registry.Registry(hive)

    try:
        key = reg.open(regPath)
    except Registry.RegistryKeyNotFoundException:
        print "Couldn't find %s..." % regPath
        pass
    try:
        k = reg.open(regPath)
        v = k.value(Key)
        cursor.execute(
            '''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent, KeyTimeStamp) VALUES(?,?,?,?,?,?,?,?)''' % TableName,
            (v.name(), v.value(), Category, stateStr, KeyStr, None, None, key.timestamp()))

    except:
        print "Error in ReadSingleReg"
def clean(item):
    """Clean up the memory by closing and deleting the item if possible."""
    if isinstance(item, list) or isinstance(item, dict):
        for _ in range(len(item)):
            clean(item.pop())
    else:
        try:
            item.close()
        except (RuntimeError, AttributeError): # deleted or no close method
            pass
        try:
            item.deleteLater()
        except (RuntimeError, AttributeError): # deleted or no deleteLater method
            pass
# end cleanUp

def ReadAllReg(db, cursor, Hive, TableName, regPath, Category, stateStr, KeyStr):
    reg = Registry.Registry(Hive)
    try:
        key = reg.open(regPath)
    except Registry.RegistryKeyNotFoundException:
        print "Couldn't find %s..." % regPath
    try:
        for value in [v for v in key.values()]:
            try:
                if value.name() == "InstallDate":
                    cursor.execute(
                        '''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent, KeyTimeStamp) VALUES(?,?,?,?,?,?,?,?)''' % TableName,
                        [value.name(), ToUnix(value), Category, stateStr, KeyStr, None, None, key.timestamp()])
                elif value.name() == "InstallTime":
                    cursor.execute(
                        '''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent, KeyTimeStamp) VALUES(?,?,?,?,?,?,?,?)''' % TableName,
                        [value.name(), FiletimeToDateTime(value), Category, stateStr, KeyStr, None, None,
                         key.timestamp()])
                else:
                    mountedDevices_unicode = ['5f', '5c']
                    if value.value()[0].encode('hex') in mountedDevices_unicode:
                        value1 = value.value().decode('utf16')
                    else:
                        value1 = value.value()
                    cursor.execute(
                        '''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent, KeyTimeStamp) VALUES(?,?,?,?,?,?,?,?)''' % TableName,
                        [value.name(), value1, Category, stateStr, KeyStr, None, None, key.timestamp()])
            except:
                cursor.execute(
                    '''INSERT INTO %s (Name, Value, Category, State, KeyStr, RecString, KeyParent, KeyTimeStamp) VALUES(?,?,?,?,?,?,?,?)''' % TableName,
                    [value.name(), str(binascii.b2a_hex(value.raw_data())), Category, stateStr, KeyStr, None, None,
                     key.timestamp()])

    except:
        print"Error in ReadAllReg"


def read(s):
    Len = 500
    Filetext = ""
    k = 0
    while k < (Len + 1):
        a = s.Read(1)
        if a != "0x00":
            Filetext += a
    return s

def rec(key, cursor, TableName, Category, stateStr, KeyStr):
   
    for subkey in key.subkeys():
        subkeyName = subkey.name()
        list1 = []
        MFT = ''
        cursor.execute(
            '''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent,KeyTimeStamp,MFT) VALUES(?,?,?,?,?,?,?,?,?)''' % TableName,
            [subkey.name(), "", Category, stateStr, KeyStr, "Folder", subkey.name(), subkey.timestamp(), MFT])
        blockstart = 0
        successfull = False

        while not successfull:
            for value1 in [v for v in subkey.values()]:
                if value1.name() == "MRUListEx":
                     list1= MRULIstExSort(list1, value1, successfull)
                     successfull = True

        
        for value in [v for v in subkey.values()]:
            if value.name() != "MRUListEx":
                list1 = openSavePidlMRU(value, subkeyName)
                
                MFT = list1[1]
                
                filePath = list1[0]
                indexnum = 0


                for p in list1: #print "www %d %s %d %d" % (int(p), value.name(),list1.index(int(value.name())))
                     i = str_to_int(value.name())
                     if p == i:
                         indexnum = list1.index(p)
                         print "%d %d" % (p, indexnum)

                blockstart = 0

                cursor.execute(
                    '''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent, KeyTimeStamp, MRUOrder, MFT) VALUES(?,?,?,?,?,?,?,?,?,?)''' % TableName,
                    [value.name(), filePath, Category, stateStr, KeyStr, "Key",subkey.name(), key.timestamp(),indexnum, MFT])
    

def str_to_int(s):
    ctr = i = 0
    for c in reversed(s):
        i += (ord(c) - 48) * (10 ** ctr)
        ctr += 1
    return i


def ReadAllRegSubdir(db, cursor, Hive, TableName, regPath, Category, stateStr, KeyStr):
    reg = Registry.Registry(Hive)
    try:
        key = reg.open(regPath)
    except Registry.RegistryKeyNotFoundException:
        print "Couldn't find %s..." % regPath
    try:

        rec(key, cursor, TableName, Category, stateStr, KeyStr)


    except Exception,e: print str(e), "Couldn't send to rec (ReadAllRegSubdir)"


def FiletimeToDateTime(h):
    from filetimes import filetime_to_dt
    val = h.value()

    time = filetime_to_dt(val)

    return str(time) + " UTC"


def ToUnix(value):
    import datetime
    return (datetime.datetime.fromtimestamp(int(value.value())).strftime('%d-%m-%Y %H:%M:%S'))

