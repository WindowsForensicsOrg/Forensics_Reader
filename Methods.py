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
import struct
import uuid
from os import path

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
            '''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent, KeyTimeStamp) VALUES(?,?,?,?,?,?,?,?)''' % TableName,
            (v.name(), v.value(), Category, stateStr, KeyStr, None, None, key.timestamp()))

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
                        '''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent, KeyTimeStamp) VALUES(?,?,?,?,?,?,?,?)''' % TableName,
                        [value.name(), ToUnix(value), Category, stateStr, KeyStr, None, None, key.timestamp()])
                elif value.name() == "InstallTime":
                    cursor.execute(
                        '''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent, KeyTimeStamp) VALUES(?,?,?,?,?,?,?,?)''' % TableName,
                        [value.name(), FiletimeToDateTime(value), Category, stateStr, KeyStr, None, None,
                         key.timestamp()])
                else:
                    cursor.execute(
                        '''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent, KeyTimeStamp) VALUES(?,?,?,?,?,?,?,?)''' % TableName,
                        [value.name(), value.value(), Category, stateStr, KeyStr, None, None, key.timestamp()])
            except:
                cursor.execute(
                    '''INSERT INTO %s (Name, Value, Category, State, KeyStr, RecString, KeyParent, KeyTimeStamp) VALUES(?,?,?,?,?,?,?,?)''' % TableName,
                    [value.name(), str(binascii.b2a_hex(value.raw_data())), Category, stateStr, KeyStr, None, None,
                     key.timestamp()])

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

def rec(key, cursor, TableName, Category, stateStr, KeyStr):
   
    for subkey in key.subkeys():
        list1 = []
        cursor.execute(
            '''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent,KeyTimeStamp) VALUES(?,?,?,?,?,?,?,?)''' % TableName,
            [subkey.name(), "", Category, stateStr, KeyStr, "Folder", subkey.name(), subkey.timestamp()])
        blockstart = 0
        successfull = False

        while not successfull:
            for value1 in [v for v in subkey.values()]:
                if value1.name() == "MRUListEx":
                     list1= recReg(list1, value1, successfull)
                     successfull = True


        for value in [v for v in subkey.values()]:
            fileName = ""
            filePath = ""
            if value.name() != "MRUListEx":
                while ord(value.value()[blockstart]) != 0:
                    # Blocklength as unsigned 16 bit int in little endian
                    blocklength = struct.unpack('<H', value.value()[blockstart:blockstart + 2])[0]
                    blocktype = value.value()[blockstart + 2].encode('hex')

                    # Type 1f = system folder. E.g. My Computer, Downloads, My Music etc.
                    if blocktype == '1f':

                        temp = rootfolder(value.value()[0:blocklength])
                        print temp
                        filePath = temp

                    # Type 2f = Driveletter
                    elif blocktype == '2f':

                        driveletter = value.value()[blockstart + 3:blockstart + 6]
                        filePath = path.join(filePath, driveletter)

                    # Type 31 = Folder
                    # Type 31 blocks and type 32 blocks contain the same structure
                    elif blocktype == '31':

                        attr = dirnameascii(value.value()[blockstart:blockstart + blocklength])
                        for k, v in attr.iteritems():
                            print k, v
                        filePath = path.join(filePath, v)

                    # Type 32 = File
                    # Type 31 blocks and type 32 blocks contain the same structure
                    elif blocktype == '32':

                        attr = fnameascii(value.value()[blockstart:blockstart + blocklength])
                        for k, v in attr.iteritems():
                            print k, v
                            fileName = attr['FileUnicodeName']
                            print filePath + "XXX"
                        filePath = path.join(filePath, fileName)
                        filePath = str(filePath) + attr['MFTEntry']
                    blockstart = blockstart + blocklength
                indexnum = 0


                for p in list1: #print "www %d %s %d %d" % (int(p), value.name(),list1.index(int(value.name())))
                     i = str_to_int(value.name())
                     if p == i:
                         indexnum = list1.index(p)
                         print "xyz %d %d" % (p, indexnum)

                blockstart = 0

                cursor.execute(
                    '''INSERT INTO %s  (Name, Value, Category, State, KeyStr, RecString, KeyParent, KeyTimeStamp, MRUOrder) VALUES(?,?,?,?,?,?,?,?,?)''' % TableName,
                    [value.name(), filePath, Category, stateStr, KeyStr, "Key",subkey.name(), key.timestamp(),indexnum])
    

def str_to_int(s):
    ctr = i = 0
    for c in reversed(s):
        i += (ord(c) - 48) * (10 ** ctr)
        ctr += 1
    return i
 
def recReg(list1, value, successfull):
    print "In rec %s" % (value.name())
    successfull = True
    if value.name() == 'MRUListEx':
        print "MRUlistEX in regrec"
        hex_chars = map(int, map(ord, (value.value())))  # Read mrulistex
        i = 0
        for i, val in enumerate(hex_chars):  # remove '0'
            if val == 255:
                break
            if i == 0 or i % 4 == 0:  # The numbers are index 0 and every fourth thereafter
                list1.append(int(val))
                i = i + 1
            else:
                i = i+1
        return list1

def str_to_guid(str):
    guidstr = str[3] + str[2] + \
              str[1] + str[0] + \
              str[5] + str[4] + \
              str[7] + str[6] + \
              str[8:16]
    return uuid.UUID(guidstr.encode('hex'))
 

def rootfolder(rootblock):
    # Folder names are defined in the Software Hive - Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\
    rootfolderguid = str_to_guid(rootblock[4:20])
    rootfolderguid = knownFolders(rootfolderguid)
    return rootfolderguid


def parsebeefblock(beefblock):
    beefcontent = []
    beefunicodenameblock = beefblock[46:].decode('utf16')
    beefunicodename = beefunicodenameblock[:beefunicodenameblock.find(chr(0))]
    # Parse file identifier (MFT) as 48 bit int in little endian
    beefmftentry = int(''.join(reversed(beefblock[20:26])).encode('hex'), 16)
    beefcontent.append(beefunicodename)
    beefcontent.append(beefmftentry)
    return beefcontent

def fnameascii(asciiblock):
    fileattr = {}
    fnameblock = asciiblock[14:]
    fname = fnameblock[:fnameblock.find(chr(0))]
    # Check if beef block is inside asciiblock
    # If found send beef block to function 'parsebeefblock'
    if len(asciiblock[:14 + len(fname) + 3]) < len(asciiblock):
        beefsigoffset = asciiblock.find('EFBE'.decode('hex'))
        beefstart = beefsigoffset - 6
        beefblock = asciiblock[beefstart:]
        beefparsed = parsebeefblock(beefblock)
        fileattr['FileUnicodeName'] = beefparsed[0]
        if beefparsed[1] == 0:
            fileattr['MFTEntry'] = ''
        else:
            fileattr['MFTEntry'] = "\t\tMFT Entry of " + '"' + beefparsed[0] + '"' + ": " + str(beefparsed[1])
        return fileattr

    fileattr['Filename'] = fname
    return fileattr

def dirnameascii(dirblock):
    dirattr = {}
    dirnameblock = dirblock[14:]
    dirname = dirnameblock[:dirnameblock.find(chr(0))]
    # Check if beef block is inside dirblock
    # If found send beef block to function 'parsebeefblock'
    if len(dirblock[:14 + len(dirname) + 3]) < len(dirblock):
        beefsigoffset = dirblock.find('EFBE'.decode('hex'))
        beefstart = beefsigoffset - 6
        beefblock = dirblock[beefstart:]
        beefparsed = parsebeefblock(beefblock)
        dirattr['\tDirectoryUnicodeName:\t'] = beefparsed[0]
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
        print "couldn't send to rec() (ReadAllRegSubdir)"
        pass


def FiletimeToDateTime(h):
    from filetimes import filetime_to_dt
    val = h.value()

    time = filetime_to_dt(val)

    return str(time) + " UTC"


def ToUnix(value):
    import datetime
    return (datetime.datetime.fromtimestamp(int(value.value())).strftime('%d-%m-%Y %H:%M:%S'))


def knownFolders(UUID):

    UUID = "{" + str(UUID) + "}"
    knownfolders = {
        "FOLDERGUID_MyComputer": "{20d04fe0-3aea-1069-a2d8-08002b30309d}",
        "FOLDERGUID_NetworkFolder": "{D20BEEC4-5CA8-4905-AE3B-BF251EA09B53}",
        "FOLDERGUID_ComputerFolder ": "{0AC0837C-BBF8-452A-850D-79D08E667CA7}",
        "FOLDERGUID_InternetFolder ": "{4D9F7874-4E0C-4904-967B-40B0D20C3E4B}",
        "FOLDERGUID_ControlPanelFolder ": "{82A74AEB-AEB4-465C-A014-D097EE346D63}",
        "FOLDERGUID_PrintersFolder ": "{76FC4E2D-D6AD-4519-A663-37BD56068185}",
        "FOLDERGUID_SyncManagerFolder ": "{43668BF8-C14E-49B2-97C9-747784D784B7}",
        "FOLDERGUID_SyncSetupFolder ": "{0F214138-B1D3-4a90-BBA9-27CBC0C5389A}",
        "FOLDERGUID_ConflictFolder ": "{4bfefb45-347d-4006-a5be-ac0cb0567192}",
        "FOLDERGUID_SyncResultsFolder ": "{289a9a43-be44-4057-a41b-587a76d7e7f9}",
        "FOLDERGUID_RecycleBinFolder ": "{B7534046-3ECB-4C18-BE4E-64CD4CB7D6AC}",
        "FOLDERGUID_ConnectionsFolder ": "{6F0CD92B-2E97-45D1-88FF-B0D186B8DEDD}",
        "FOLDERGUID_Fonts ": "{FD228CB7-AE11-4AE3-864C-16F3910AB8FE}",
        "FOLDERGUID_Desktop ": "{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}",
        "FOLDERGUID_Startup ": "{B97D20BB-F46A-4C97-BA10-5E3608430854}",
        "FOLDERGUID_Programs ": "{A77F5D77-2E2B-44C3-A6A2-ABA601054A51}",
        "FOLDERGUID_StartMenu ": "{625B53C3-AB48-4EC1-BA1F-A1EF4146FC19}",
        "FOLDERGUID_Recent ": "{AE50C081-EBD2-438A-8655-8A092E34987A}",
        "FOLDERGUID_SendTo ": "{8983036C-27C0-404B-8F08-102D10DCFD74}",
        "FOLDERGUID_Documents ": "{FDD39AD0-238F-46AF-ADB4-6C85480369C7}",
        "FOLDERGUID_Favorites ": "{1777F761-68AD-4D8A-87BD-30B759FA33DD}",
        "FOLDERGUID_NetHood ": "{C5ABBF53-E17F-4121-8900-86626FC2C973}",
        "FOLDERGUID_PrintHood ": "{9274BD8D-CFD1-41C3-B35E-B13F55A758F4}",
        "FOLDERGUID_Templates ": "{A63293E8-664E-48DB-A079-DF759E0509F7}",
        "FOLDERGUID_CommonStartup ": "{82A5EA35-D9CD-47C5-9629-E15D2F714E6E}",
        "FOLDERGUID_CommonPrograms ": "{0139D44E-6AFE-49F2-8690-3DAFCAE6FFB8}",
        "FOLDERGUID_CommonStartMenu ": "{A4115719-D62E-491D-AA7C-E74B8BE3B067}",
        "FOLDERGUID_PublicDesktop ": "{C4AA340D-F20F-4863-AFEF-F87EF2E6BA25}",
        "FOLDERGUID_ProgramData ": "{62AB5D82-FDC1-4DC3-A9DD-070D1D495D97}",
        "FOLDERGUID_CommonTemplates ": "{B94237E7-57AC-4347-9151-B08C6C32D1F7}",
        "FOLDERGUID_PublicDocuments ": "{ED4824AF-DCE4-45A8-81E2-FC7965083634}",
        "FOLDERGUID_RoamingAppData ": "{3EB685DB-65F9-4CF6-A03A-E3EF65729F3D}",
        "FOLDERGUID_LocalAppData ": "{F1B32785-6FBA-4FCF-9D55-7B8E7F157091}",
        "FOLDERGUID_LocalAppDataLow ": "{A520A1A4-1780-4FF6-BD18-167343C5AF16}",
        "FOLDERGUID_InternetCache ": "{352481E8-33BE-4251-BA85-6007CAEDCF9D}",
        "FOLDERGUID_Cookies ": "{2B0F765D-C0E9-4171-908E-08A611B84FF6}",
        "FOLDERGUID_History ": "{D9DC8A3B-B784-432E-A781-5A1130A75963}",
        "FOLDERGUID_System ": "{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}",
        "FOLDERGUID_SystemX86 ": "{D65231B0-B2F1-4857-A4CE-A8E7C6EA7D27}",
        "FOLDERGUID_Windows ": "{F38BF404-1D43-42F2-9305-67DE0B28FC23}",
        "FOLDERGUID_Profile ": "{5E6C858F-0E22-4760-9AFE-EA3317B67173}",
        "FOLDERGUID_Pictures ": "{33E28130-4E1E-4676-835A-98395C3BC3BB}",
        "FOLDERGUID_ProgramFilesX86 ": "{7C5A40EF-A0FB-4BFC-874A-C0F2E0B9FA8E}",
        "FOLDERGUID_ProgramFilesCommonX86 ": "{DE974D24-D9C6-4D3E-BF91-F4455120B917}",
        "FOLDERGUID_ProgramFilesX64 ": "{6D809377-6AF0-444b-8957-A3773F02200E}",
        "FOLDERGUID_ProgramFilesCommonX64 ": "{6365D5A7-0F0D-45e5-87F6-0DA56B6A4F7D}",
        "FOLDERGUID_ProgramFiles ": "{905e63b6-c1bf-494e-b29c-65b732d3d21a}",
        "FOLDERGUID_ProgramFilesCommon ": "{F7F1ED05-9F6D-47A2-AAAE-29D317C6F066}",
        "FOLDERGUID_AdminTools ": "{724EF170-A42D-4FEF-9F26-B60E846FBA4F}",
        "FOLDERGUID_CommonAdminTools ": "{D0384E7D-BAC3-4797-8F14-CBA229B392B5}",
        "FOLDERGUID_Music ": "{4BD8D571-6D19-48D3-BE97-422220080E43}",
        "FOLDERGUID_Videos ": "{18989B1D-99B5-455B-841C-AB7C74E4DDFC}",
        "FOLDERGUID_PublicPictures ": "{B6EBFB86-6907-413C-9AF7-4FC2ABF07CC5}",
        "FOLDERGUID_PublicMusic ": "{3214FAB5-9757-4298-BB61-92A9DEAA44FF}",
        "FOLDERGUID_PublicVideos ": "{2400183A-6185-49FB-A2D8-4A392A602BA3}",
        "FOLDERGUID_ResourceDir ": "{8AD10C31-2ADB-4296-A8F7-E4701232C972}",
        "FOLDERGUID_LocalizedResourcesDir ": "{2A00375E-224C-49DE-B8D1-440DF7EF3DDC}",
        "FOLDERGUID_CommonOEMLinks ": "{C1BAE2D0-10DF-4334-BEDD-7AA20B227A9D}",
        "FOLDERGUID_CDBurning ": "{9E52AB10-F80D-49DF-ACB8-4330F5687855}",
        "FOLDERGUID_UserProfiles ": "{0762D272-C50A-4BB0-A382-697DCD729B80}",
        "FOLDERGUID_Playlists ": "{DE92C1C7-837F-4F69-A3BB-86E631204A23}",
        "FOLDERGUID_SamplePlaylists ": "{15CA69B3-30EE-49C1-ACE1-6B5EC372AFB5}",
        "FOLDERGUID_SampleMusic ": "{B250C668-F57D-4EE1-A63C-290EE7D1AA1F}",
        "FOLDERGUID_SamplePictures ": "{C4900540-2379-4C75-844B-64E6FAF8716B}",
        "FOLDERGUID_SampleVideos ": "{859EAD94-2E85-48AD-A71A-0969CB56A6CD}",
        "FOLDERGUID_PhotoAlbums ": "{69D2CF90-FC33-4FB7-9A0C-EBB0F0FCB43C}",
        "FOLDERGUID_Public ": "{DFDF76A2-C82A-4D63-906A-5644AC457385}",
        "FOLDERGUID_ChangeRemovePrograms ": "{df7266ac-9274-4867-8d55-3bd661de872d}",
        "FOLDERGUID_AppUpdates ": "{a305ce99-f527-492b-8b1a-7e76fa98d6e4}",
        "FOLDERGUID_AddNewPrograms ": "{de61d971-5ebc-4f02-a3a9-6c82895e5c04}",
        "FOLDERGUID_Downloads ": "{374DE290-123F-4565-9164-39C4925E467B}",
        "FOLDERGUID_PublicDownloads ": "{3D644C9B-1FB8-4f30-9B45-F670235F79C0}",
        "FOLDERGUID_SavedSearches ": "{7d1d3a04-debb-4115-95cf-2f29da2920da}",
        "FOLDERGUID_QuickLaunch ": "{52a4f021-7b75-48a9-9f6b-4b87a210bc8f}",
        "FOLDERGUID_Contacts ": "{56784854-C6CB-462b-8169-88E350ACB882}",
        "FOLDERGUID_SidebarParts ": "{A75D362E-50FC-4fb7-AC2C-A8BEAA314493}",
        "FOLDERGUID_SidebarDefaultParts ": "{7B396E54-9EC5-4300-BE0A-2482EBAE1A26}",
        "FOLDERGUID_TreeProperties ": "{5b3749ad-b49f-49c1-83eb-15370fbd4882}",
        "FOLDERGUID_PublicGameTasks ": "{DEBF2536-E1A8-4c59-B6A2-414586476AEA}",
        "FOLDERGUID_GameTasks ": "{054FAE61-4DD8-4787-80B6-090220C4B700}",
        "FOLDERGUID_SavedGames ": "{4C5C32FF-BB9D-43b0-B5B4-2D72E54EAAA4}",
        "FOLDERGUID_Games ": "{CAC52C1A-B53D-4edc-92D7-6B2E8AC19434}",
        "FOLDERGUID_RecordedTV ": "{bd85e001-112e-431e-983b-7b15ac09fff1}",
        "FOLDERGUID_SEARCH_MAPI ": "{98ec0e18-2098-4d44-8644-66979315a281}",
        "FOLDERGUID_SEARCH_CSC ": "{ee32e446-31ca-4aba-814f-a5ebd2fd6d5e}",
        "FOLDERGUID_Links ": "{bfb9d5e0-c6a9-404c-b2b2-ae6db6af4968}",
        "FOLDERGUID_UsersFiles ": "{f3ce0f7c-4901-4acc-8648-d5d44b04ef8f}",
        "FOLDERGUID_SearchHome ": "{190337d1-b8ca-4121-a639-6d472d16972a}",
        "FOLDERGUID_OriginalImages": "{2C36C0AA-5812-4b87-BFD0-4CD0DFB19B39}"
    }
    for k, v in knownfolders.items():
        if UUID == str(v):
            UUID = str(k)

            continue

    return UUID
