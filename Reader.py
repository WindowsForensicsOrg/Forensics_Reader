#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#
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
#  along with this Aprogram; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
# !/usr/bin/python
# !/usr/bin/python
import sqlite3

from Methods import *

path = r"D:\Google Drive\Python\Samples"
OSdb = sqlite3.connect(":memory:")
Userdb = sqlite3.connect(":memory:")
UserCursor = Userdb.cursor()
cursorOS = OSdb.cursor()
cursorOS.execute('''CREATE TABLE OsInfo(id INTEGER PRIMARY KEY, Name TEXT, Value TEXT,Category TEXT)''')
UserCursor.execute('''CREATE TABLE UsersInfo(id INTEGER PRIMARY KEY, name TEXT, Value TEXT, Category TEXT)''')


def main():
    Fetch_Info(Userdb, path, UserCursor, "NTUSER.DAT", "UsersInfo",
               r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths", "Typed Urls")  # Typed Paths
    Userdb.commit()
    ReadSingleReg(OSdb, "SYSTEM", path, "Select", "Current", cursorOS, "OsInfo",
                  "CurrentControlSet")  # CurrentControlSet
    OSdb.commit()

    OSdb.close()
    Userdb.close()

if __name__ == '__main__':
    main()


    # print "Mounted Devices:"
    # result2 = ReadAllReg(path + r"\SYSTEM", "MountedDevices", db)
    # result3 = ReadAllReg(path + r"\SOFTWARE", "Microsoft\\Windows NT\\CurrentVersion", db)
    # print "Current controlset: %s" % forensicating.control_set_check(path + r'\SYSTEM')
    # print os_settings(path + r'\SYSTEM', path + r'\SOFTWARE')
    # printList(result1)
    # printList(result3)
