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
# !/usr/bin/python
import binascii

from Registry import Registry


def ReadSingleReg(db, hive, path, regPath, Key, cursor, TableName, Category):
    reg = Registry.Registry(path + "\\" + hive)

    try:
        key = reg.open(regPath)
    except Registry.RegistryKeyNotFoundException:
        print "Couldn't find %s..." % regPath
        pass
    try:
        k = reg.open(regPath)
        v = k.value(Key)
        cursor.execute('''INSERT INTO %s  (Name, Value, Category) VALUES(?,?,?)''' % TableName, (v.name(), v.value(), Category))
        # populate_grid(TableName, cursor)
        return db
    except:
        print "Error in ReadSingleReg"

        return db


def Fetch_Info(db, path, cursor, HiveName, TableName, regPath, Category):
    ReadAllReg(cursor, path + "\\" + HiveName, TableName, regPath, db, Category)
    # populate_grid(TableName, cursor)
    return db


def ReadAllReg(cursor, Hive, TableName, regPath, db, Category):
    reg = Registry.Registry(Hive)
    try:
        key = reg.open(regPath)
    except Registry.RegistryKeyNotFoundException:
        print "Couldn't find %s..." % regPath
        pass
    try:
        for value in [v for v in key.values()]:
            try:
                #  if v.value_type() == Registry.RegSZ or v.value_type() == Registry.RegExpandSZ or v.value_type() == Registry.RegBin:
                cursor.execute('''INSERT INTO %s  (Name, Value, Category) VALUES(?,?,?)''' % TableName,
                               [value.name(), value.value(), Category])
            except:
                cursor.execute('''INSERT INTO %s (Name, Value, Category) VALUES(?,?,?)''' % TableName,
                               (value.name(),
                                str(binascii.b2a_hex(value.raw_data())), Category))
    except:
        print"Error in ReadAllReg"

    return db
