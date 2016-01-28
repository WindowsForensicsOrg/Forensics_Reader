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
import Tkinter as tk
import sqlite3
import sys
import tkFont

import tkTable
from Methods import *

# from tkMessageBox import *
from tkFileDialog import askdirectory


class GUI(object):
    """  def __init__(self, master):
          self.master=master
          b = Button(text="Browse...",command=lambda : master.callback())
          b.pack()

          pad=3
          self._geom='300x300+0+0'
          master.geometry("{0}x{1}+0+0".format(
              master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
          master.bind('<Escape>',self.toggle_geom)

      def toggle_geom(self,event):
          geom=self.master.winfo_geometry()
          print(geom,self._geom)
          self.master.geometry(self._geom)
          self._geom=geom
      def callback(self, master):
          dirname = askdirectory(parent=root,initialdir="/",title='Path to exported files')

      """

    def __init__(self, master):
        self.master = master
        fontHead = tkFont.Font(family="Arial", size=10, weight=tkFont.BOLD)
        fontBold = tkFont.Font(family="Arial", size=8, weight=tkFont.BOLD)
        fontReg = tkFont.Font(family="Arial", size=8)
        frameN = tk.Frame(master)
        frameN.grid(row=0, padx=5, pady=5)
        frameXBH = tk.Frame(frameN)
        frameXBH.grid(row=0, columnspan=5, padx=5)
        tk.Canvas(frameXBH, borderwidth=0, relief="flat", height=1, width=20, background="#cccccc").grid(row=0)
        tk.Label(frameXBH, text="Forensics Reader", font=fontBold, width=15).grid(row=0, column=1)
        tk.Canvas(frameXBH, borderwidth=0, relief="flat", height=1, width=800, background="#cccccc").grid(row=0,
                                                                                                          column=2,
                                                                                                       sticky="WE")
        tk.Label(frameN, text="Directory containing exported files:", font=fontReg).grid(row=1, sticky="W")
        xbPath = tk.Entry(frameN, width=30, font=fontReg)
        xbPath.grid(row=1, column=1, sticky="W")
        xbBrowse = tk.Button(frameN, text="Browse for folder", font=fontReg,
                             command=lambda: self.get_dir(master, xbPath))
        xbBrowse.grid(row=1, column=2, sticky="W")
        xbRel = tk.Checkbutton(frameN, text="Save case for later", font=fontReg)
        xbRel.grid(row=1, column=4, sticky="W")
        tk.Canvas(frameN, borderwidth=1, relief="groove", width=800, height=0).grid(row=2, columnspan=5, pady=10)
        # SAVE AND CANCEL
        btnSave = tk.Button(frameN, text="Start", width=10, command=lambda: self._grid())
        btnSave.grid(row=3, column=3, sticky="E")
        btnCancel = tk.Button(frameN, text="Cancel", width=10, command=lambda: self.cancel_btn())
        btnCancel.grid(row=3, column=4, sticky="W")

    #    def create_window(self):
    #        self.counter += 1
    #        t = tk.Toplevel(self)
    #        t.wm_title("Window #%s" % self.counter)
    #        l = tk.Label(t, text="This is window #%s" % self.counter)
    #        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)

    def cancel_btn(self):
        sys.exit(-1)

    def get_dir(self, master, masterPath):
        global globvar
        dirname = askdirectory(mustexist=1, title="Please select folder containing exported files")
        dirname = dirname.replace("/", "\\")
        globvar = dirname
        masterPath.insert(0, dirname)

    def StartExam(self):
        Fetch_Info(Userdb, globvar, UserCursor, "NTUSER.DAT", "UsersInfo",
                   r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths", "Typed Urls")  # Typed Paths

        ReadSingleReg(OSdb, "SYSTEM", globvar, "Select", "Current", cursorOS, "OsInfo",
                      "CurrentControlSet")  # CurrentControlSet

    def _grid(self):
        self.StartExam()
        table = tkTable.Table(root, rows=2, cols=10)
        table.pack()



OSdb = sqlite3.connect(":memory:")
Userdb = sqlite3.connect(":memory:")
UserCursor = Userdb.cursor()
cursorOS = OSdb.cursor()
cursorOS.execute('''CREATE TABLE OsInfo(Id INTEGER PRIMARY KEY, Name TEXT, Value TEXT,Category TEXT)''')
UserCursor.execute('''CREATE TABLE UsersInfo(Id INTEGER PRIMARY KEY, Name TEXT, Value TEXT, Category TEXT)''')

"""
# print "Mounted Devices:"
    # result2 = ReadAllReg(dirname + r"\SYSTEM", "MountedDevices", db)
    # result3 = ReadAllReg(dirname + r"\SOFTWARE", "Microsoft\\Windows NT\\CurrentVersion", db)
    # print "Current controlset: %s" % forensicating.control_set_check(path + r'\SYSTEM')
    # print os_settings(path + r'\SYSTEM', dirname + r'\SOFTWARE')
    # printList(result1)
    # printList(result3)
"""





def main():

    OSdb.commit()
    OSdb.close()
    Userdb.close()


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(0, 0)
    app = GUI(root)
    root.mainloop()
