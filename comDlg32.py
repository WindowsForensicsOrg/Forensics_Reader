import struct
from os import path
from shellitemBlocks import *
from guids import *


def openSavePidlMRU(value, subkeyName):
    fileName = ''
    filePath = ''
    mft = ''
    blockstart = 0
    while ord(value.value()[blockstart]) != 0:
        # Blocklength as unsigned 16 bit int in little endian
        blocklength = struct.unpack('<H', value.value()[blockstart:blockstart + 2])[0]
        blocktype = value.value()[blockstart + 2].encode('hex')

        # Type 1f = system folder. E.g. My Computer, Downloads, My Music etc.
        if blocktype == '1f':

            temp = rootfolder(value.value()[0:blocklength])
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
                filePath = path.join(filePath, v)

        # Type 32 = File
        # Type 31 blocks and type 32 blocks contain the same structure
        elif blocktype == '32' or blocktype == '36':

            attr = fnameascii(value.value()[blockstart:blockstart + blocklength])
            for k, v in attr.iteritems():
                fileName = attr['FileUnicodeName']
            filePath = path.join(filePath, fileName)
            mft = attr['MFTEntry']

            
        blockstart = blockstart + blocklength

    blockstart = 0
    return ','.join([filePath, mft, subkeyName, value.name()]).split(',')