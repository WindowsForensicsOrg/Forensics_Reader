#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Reader.py
#
#  Copyright 2016 ras <riisras@gmail.com>
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
import Tkinter as tk
import sqlite3
import tkFont
import ttk
from tkFileDialog import askdirectory

from Methods import *


class GUI(object):
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
        tk.Canvas(frameXBH, borderwidth=0, relief="flat", height=1, width=800, background="#cccccc").grid(row=0,column=2,sticky="WE")
        tk.Label(frameN, text="Directory containing exported files:", font=fontReg).grid(row=1, sticky="W")
        global xbPath
        xbPath = tk.Entry(frameN, text="hhe", width=30, font=fontReg)
        xbPath.grid(row=1, column=1, sticky="W")
        xbBrowse = tk.Button(frameN, text="Browse for folder", font=fontReg, command=lambda: self.get_dir(xbPath))
        xbBrowse.grid(row=1, column=2, sticky="W")
        xbRel = tk.Checkbutton(frameN, text="Save case for later", font=fontReg)
        xbRel.grid(row=1, column=4, sticky="W")
        tk.Canvas(frameN, borderwidth=1, relief="groove", width=800, height=0).grid(row=2, columnspan=5, pady=10)
        btnStart = tk.Button(frameN, text="Start", width=10, command=lambda: self._grid(frameXBH))
        btnStart.grid(row=3, column=3, sticky="E")
        btnCancel = tk.Button(frameN, text="Cancel", width=10, command=lambda: self.cancel_btn())
        btnCancel.grid(row=3, column=4, sticky="W")

    def cancel_btn(self): #Cancel button
        raise SystemExit

    def get_dir(self, xbPath): #Pich folder containing files
        xbPath.delete(0, "end")
        xbPath.insert(1, askdirectory(mustexist=1, title="Please select folder containing exported files").replace("/", "\\"))

    def OnClick(self, event): #When user expands a tree in treeview the columns are selected
        item = self.tree.selection()[0]
        topChild = self.tree.parent(item)
        for row in self.tree.get_children(): #function to close all nodes. broken. Sæt den til overmappen og luk kun enkelte
            if row != topChild:
                self.tree.item(row, open=False)
        if self.tree.item(item,"text") in ("User activities", "Operating System information", "Mounted Devices"): #The list of 'directories'
            self.tree["displaycolumns"]=("Keyname", "Keyvalue")
        else:
            print "Error. Value not in list"


    def StartExam(self):  # Order:(db, cursor, hive, TableName, regPath,  Key, Category, single or subdir, text):
        ReadAllReg(db, cursor, xbPath.get() + "\\NTUSER.DAT", "Info", r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths", "User", "SubDir", "Typed Urls")  # Typed Paths
        ReadAllReg(db, cursor, xbPath.get() + "\\SOFTWARE", "Info", r"Microsoft\Windows NT\CurrentVersion", "OS", "SubDir", "Operating System Information")
        ReadAllReg(db, cursor, xbPath.get() + "\SYSTEM", "Info", "MountedDevices", "OS", "SubDir", "Mounted Devices") #Mounted devices
        ReadSingleReg(db, cursor, xbPath.get() + "\\SYSTEM", "Info", "Select", "Current", "OS", "Single", "Current Control Set")  # CurrentControlSet

    def _grid(self, master):
        self.StartExam()
        self.create_window(master)

    def create_window(self, master):
        root = tk.Toplevel()
        self.tree = ttk.Treeview(root)
        root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        self.tree["columns"] = ("Keyname", "Keyvalue")
        #tree.column("one", width=100)
        self.tree.column("#0", width=300) #First column
        self.tree.column("Keyname",width=300)
        self.tree.column("Keyvalue", width=2000 )
        #tree.heading("one", text="ID")
        self.tree.heading("Keyname", text="Key Name",anchor=tk.W)
        self.tree.heading("Keyvalue", text="Key value",anchor=tk.W)
        self.tree.insert("", 3, "dirOS", open=False, text="Operating System information")
        self.tree.insert("", 3, "dirUser",open=False, text="User activities")
        cursor.execute('''SELECT * FROM %s''' % "Info")
        all_rows = cursor.fetchall()
        fo = open("Info.txt", "wb")
        for row in all_rows:  #TODO. Hvilke skridt skal udføres når der kommer andre ting ind over fx. linkfiler og eventfiler.
            #TODO Husk at sortere i listerne i treeview så det ikke bliver 1, 10, 2, 20 osv
            #TODO hust at lukke de andre dirs når et nyt bliver åbnet så du kan sætte de rigtige columns
            if isinstance(row[2], unicode): #binf.read().decode('utf-16').encode('utf-8')
                try:
                    txtStr = row[2].decode('utf-16').encode('ascii')
                    print('{0} : {1}, {2}, {3}'.format(row[0], row[1], txtStr, row[3]))
                except:
                    txtStr = row[2]
                    print('{0} : {1}, {2}, {3}'.format(row[0], row[1], txtStr, row[3]))

            fo.writelines('{0} : {1}, {2}, {3}\r\n'.format(row[0], row[1], txtStr, row[3]))
            if row[3] == "OS" and row[4] == "Single":
                self.tree.insert("dirOS", 0, text=row[5], values=(row[1], txtStr))
            elif row[3] == "OS" and row[4] == "SubDir":
                try:
                    self.tree.insert("dirOS", 3, row[5], open=False,text=row[5])

                    self.tree.insert(row[5], 3, text="", values=(row[1], txtStr))
                except:
                    self.tree.insert(row[5], 3, text="", values=(row[1], txtStr))
            if row[3] == "User" and row[4] == "Single":
                self.tree.insert("dirUser", 0, text=row[5], values=(row[1], txtStr))
            elif row[3] == "User" and row[4] == "SubDir":
                #tree.heading('#0', text="name") CHANGE COLUMN HEADER!!!
                try:
                    self.tree.insert("dirUser", 3, row[5], open=False,text=row[5])
                    self.tree.insert(row[5], 3, text="", values=(row[1], txtStr))
                except:
                     self.tree.insert(row[5], 3, text="", values=(row[1], txtStr))
        self.tree.bind("<<TreeviewOpen>>", self.OnClick)
        self.tree.pack(expand=1, fill='both', side='bottom')
        fo.close()
        root.mainloop()

db = sqlite3.connect(":memory:")
cursor = db.cursor()
cursor.execute('''CREATE TABLE Info(Id INTEGER PRIMARY KEY, Name TEXT, Value TEXT,Category TEXT, State TEXT, Keystr TEXT)''')

def main():
    db.commit()
    db.close()

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(0, 0)
    app = GUI(root)
    root.mainloop()