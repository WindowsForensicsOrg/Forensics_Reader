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
db = sqlite3.connect("db11")
def main():

   # print "Typed URL's"
   cursor = db.cursor()
   cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, URL TEXT)''')
   ReadAllReg(path + r"\NTUSER.DAT", r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths", db, cursor)

   cursor.execute('''SELECT * FROM users''')
   user1 = cursor.fetchone()  # retrieve the first row
   #  print(user1[0]) #Print the first column retrieved(user's name)
   all_rows = cursor.fetchall()
   for row in all_rows:
       # row[0] returns the first column in the query (name), row[1] returns email column.
       print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
       # print "Mounted Devices:"
       # result2 = ReadAllReg(path + r"\SYSTEM", "MountedDevices", db)
       # result3 = ReadAllReg(path + r"\SOFTWARE", "Microsoft\\Windows NT\\CurrentVersion", db)
       # print "Current controlset: %s" % forensicating.control_set_check(path + r'\SYSTEM')
       # print os_settings(path + r'\SYSTEM', path + r'\SOFTWARE')
       # printList(result1)
       # printList(result3)
   db.close()
if __name__ == '__main__':
    main()
