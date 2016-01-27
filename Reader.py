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

path = r"C:\Users\DKRRK\PycharmProjects\Samples"
db = sqlite3.connect(":memory:")
def main():


   cursor = db.cursor()
   cursor.execute('''CREATE TABLE OsInfo(id INTEGER PRIMARY KEY, name TEXT, URL TEXT)''')
   Fetch_Info(db, path, cursor, "NTUSER.DAT", "OsInfo",
              r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths")
   db.close()




if __name__ == '__main__':
    main()


    # print "Mounted Devices:"
    # result2 = ReadAllReg(path + r"\SYSTEM", "MountedDevices", db)
    # result3 = ReadAllReg(path + r"\SOFTWARE", "Microsoft\\Windows NT\\CurrentVersion", db)
    # print "Current controlset: %s" % forensicating.control_set_check(path + r'\SYSTEM')
    # print os_settings(path + r'\SYSTEM', path + r'\SOFTWARE')
    # printList(result1)
    # printList(result3)
