# Data block related to shell items
# Used in ComDlg32, Shell bags etc.

def parsebeefblock(beefblock):
    beefcontent = []
    # Unicode name starts in offset 46 and end of filename is '00'
    beefunicodenameblock = beefblock[46:].decode('utf16')
    beefunicodename = beefunicodenameblock[:beefunicodenameblock.find(chr(0))]
    # Parse file identifier (MFT) as 48 bit int in little endian
    beefmftentry = int(''.join(reversed(beefblock[20:26])).encode('hex'), 16)
    # Returns a list containing two items
    # which are unicode name and MFT Entry
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
            fileattr['MFTEntry'] = str(beefparsed[1])
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