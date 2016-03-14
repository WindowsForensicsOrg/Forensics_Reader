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
import uuid

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
        cursor.execute(
            '''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent) VALUES(?,?,?,?,?,?,?)''' % TableName,
            (v.name(), v.value(), Category, stateStr, KeyStr, None, None))

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
                    cursor.execute(
                        '''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent) VALUES(?,?,?,?,?,?,?)''' % TableName,
                        [value.name(), ToUnix(value), Category, stateStr, KeyStr, None, None])
                elif value.name() == "InstallTime":
                    cursor.execute(
                        '''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent) VALUES(?,?,?,?,?,?,?)''' % TableName,
                        [value.name(), FiletimeToDateTime(value), Category, stateStr, KeyStr, None, None])
                else:
                    cursor.execute(
                        '''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent) VALUES(?,?,?,?,?,?,?)''' % TableName,
                        [value.name(), value.value(), Category, stateStr, KeyStr, None, None])
            except:
                cursor.execute(
                    '''INSERT INTO %s (Name, Value, Category, State, KeyStr, RecString, KeyParent) VALUES(?,?,?,?,?,?,?)''' % TableName,
                    [value.name(), str(binascii.b2a_hex(value.raw_data())), Category, stateStr, KeyStr, None, None])

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


def rec(key, cursor, TableName, Category, stateStr, KeyStr):  # TODO husk at behandle data så det ikke bare er hex

    for subkey in key.subkeys():

        cursor.execute(
            '''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent) VALUES(?,?,?,?,?,?,?)''' % TableName,
            [subkey.name(), "", Category, stateStr, KeyStr, "Folder", subkey.name()])

        blockstart = 0
        for value in [v for v in subkey.values()]:

            if value.name() == 'MRUListEx':

                print 'mrulist'
                continue
            else:

                while ord(value.value()[blockstart]) != 0:
                    blocklength = ord(value.value()[blockstart])
                    blocktype = value.value()[blockstart + 2:blockstart + 4].encode('hex')
                    if blocktype == '1f50':
                        print 'Found Root Folder'
                        print  'Root Directory GUID:\t', rootfolder(value.value()[0:blocklength])

                    elif blocktype == '3100':
                        print 'Found Diretory'
                        attr = dirnameascii(value.value()[blockstart:blockstart + blocklength])
                        for k, v in attr.iteritems():
                            print k, v

                    elif blocktype == '3200':
                        fileName = ""
                        print 'Found Filename'
                        attr = fnameascii(value.value()[blockstart:blockstart + blocklength])
                        for k, v in attr.iteritems():
                            print k, v
                            fileName = v

                    elif blocktype == '3600':
                        print 'Found Filename - Unicode'

                    # print 'Block start:\t', blockstart
                    # print 'Block type:\t', blocktype
                    # print 'Block length:\t', blocklength
                    blockstart = blockstart + blocklength

            blockstart = 0
            cursor.execute(
                '''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent) VALUES(?,?,?,?,?,?,?)''' % TableName,
                [value.name(), fileName, Category, stateStr, KeyStr, "Key",
                 subkey.name()])
    rec(subkey)


def str_to_guid(str):
    guidstr = str[3] + str[2] + \
              str[1] + str[0] + \
              str[5] + str[4] + \
              str[7] + str[6] + \
              str[8:16]
    return uuid.UUID(guidstr.encode('hex'))


def rootfolder(rootblock):
    rootfolderguid = str_to_guid(rootblock[4:20])
    return rootfolderguid


def fnameascii(asciiblock):
    fileattr = {}
    fnameblock = asciiblock[14:]
    fname = fnameblock[:fnameblock.find(chr(0))]
    fsize = asciiblock[4:8]
    fdate = asciiblock[8:12]
    fileattr['\tFilename:\t'] = fname
    fileattr['\tFilesize:\t'] = fsize.encode('hex')
    fileattr['\tFiledate:\t'] = fdate.encode('hex')
    return fileattr


def dirnameascii(dirblock):
    dirattr = {}
    dirnameblock = dirblock[14:]
    dirname = dirnameblock[:dirnameblock.find(chr(0))]
    dirsize = dirblock[4:8]
    dirdate = dirblock[8:12]
    dirattr['\tDirectory name:\t'] = dirname
    dirattr['\tDirectory size:\t'] = dirsize.encode('hex')
    dirattr['\tDirectory date:\t'] = dirdate.encode('hex')
    return dirattr


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
