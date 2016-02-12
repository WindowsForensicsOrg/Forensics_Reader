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

from Registry import Registry


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
        cursor.execute('''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent) VALUES(?,?,?,?,?,?,?)''' % TableName, (v.name(), v.value(), Category, stateStr, KeyStr,None,None))

    except:
        print "Error in ReadSingleReg"


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
                    cursor.execute('''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent) VALUES(?,?,?,?,?,?,?)''' % TableName, [value.name(),ToUnix(value), Category, stateStr, KeyStr,None,None])
                elif value.name() == "InstallTime":
                    cursor.execute('''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent) VALUES(?,?,?,?,?,?,?)''' % TableName, [value.name(),FiletimeToDateTime(value), Category, stateStr, KeyStr,None,None])
                else:
                    cursor.execute('''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent) VALUES(?,?,?,?,?,?,?)''' % TableName,[value.name(), value.value(), Category, stateStr, KeyStr,None,None])
            except:
                cursor.execute('''INSERT INTO %s (Name, Value, Category, State, KeyStr, RecString, KeyParent) VALUES(?,?,?,?,?,?,?)''' % TableName,[value.name(), str(binascii.b2a_hex(value.raw_data())), Category, stateStr, KeyStr,None,None])

    except:
        print"Error in ReadAllReg"


def rec(key, cursor, TableName, Category, stateStr, KeyStr): #TODO husk at behandle data så det ikke bare er hex

    for subkey in key.subkeys():
        print subkey.name() + "***"
        cursor.execute('''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent) VALUES(?,?,?,?,?,?,?)''' % TableName,[subkey.name(), "", Category, stateStr, KeyStr,"Folder", subkey.name()])
        for value in [v for v in subkey.values()]:
            print value.raw_data()
            cursor.execute('''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent) VALUES(?,?,?,?,?,?,?)''' % TableName,[value.name(), str(binascii.b2a_hex(value.raw_data())), Category, stateStr, KeyStr,"Key", subkey.name()])
    rec(subkey)

def ReadAllRegSubdir(db, cursor, Hive, TableName, regPath, Category, stateStr, KeyStr):
    reg = Registry.Registry(Hive)
    try:
        key = reg.open(regPath)
    except Registry.RegistryKeyNotFoundException:
        print "Couldn't find %s..." % regPath
    try:
        rec(key, cursor, TableName, Category, stateStr, KeyStr)


    except:
        print"Error in ReadAllRegSubdir"

def FiletimeToDateTime(h):
    from filetimes import filetime_to_dt
    val = h.value()

    time = filetime_to_dt(val)

    return str(time) + " UTC"




def ToUnix(value):
    import datetime
    return (datetime.datetime.fromtimestamp(int(value.value())).strftime('%d-%m-%Y %H:%M:%S'))
