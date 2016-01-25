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
import Methods
import binascii
import forensicating
import sys
from Registry import Registry
from Registry import RegistryParse
from Methods import ReadSingleReg
from Methods import ReadAllReg
from forensicating import *
import sqlite3 as lite

path = r"C:\Users\DKRRK\PycharmProjects\Samples"
def main():
   # print "Typed URL's"
   # print str(ReadAllReg(path + r"\NTUSER.DAT", r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths"))
    print "Mounted Devices:"
    ReadAllReg(path + r"\SYSTEM", "MountedDevices")
    print "Current controlset: %s" % forensicating.control_set_check(path + r'\SYSTEM')
    print os_settings(path + r'\SYSTEM', path + r'\SOFTWARE')

main()
