#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Methods.py
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
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
#!/usr/bin/python
#!/usr/bin/python
from Registry import Registry
from Registry import RegistryParse
import binascii
import sys


def ReadSingleReg(hive, Path, Key):
    with open(hive, 'rb') as h:
        r = Registry.Registry(h)
    try:
            k = r.open(Path)
            v = k.value(Key)
            return v.value()
    except:
        return "Empty"

def ReadAllReg(Hive, Path):
    reg = Registry.Registry(Hive)
    try:
        key = reg.open(Path)
    except Registry.RegistryKeyNotFoundException:
        print "Couldn't find %s..." % Path
        sys.exit(-1)

    for value in [v for v in key.values() if v.value_type() == Registry.RegSZ or v.value_type() == Registry.RegExpandSZ or v.value_type() == Registry.RegBin]:
            print "%s: %s: %s" % (value.name(), value.value(), value.value_type_str())

