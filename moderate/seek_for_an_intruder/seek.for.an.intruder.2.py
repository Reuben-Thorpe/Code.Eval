# Reuben Thorpe (2016), CodeEval [Seek For An Intruder v1.0]
from sys import argv
from operator import itemgetter

import socket
import struct
import re


def findHacker(dump):
    # Find the most freqently occuring IP in a text dump

    dotDec = r"(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}" \
             "(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"

    dotHex = r"(0x[0-9a-fA-F]{1,2})\.(0x[0-9a-fA-F]{1,2})\." \
             "(0x[0-9a-fA-F]{1,2})\.(0x[0-9a-fA-F]{1,2})"

    dotOct = r"(0[0-3][0-9]{2})\.(0[0-3][0-9]{2})\.(0[0-3][0-9]{2})\." \
             "(0[0-3][0-9]{2})"

    dotBin = r"([0-1]{8})\.([0-1]{8})\.([0-1]{8})\.([0-1]{8})"
    binary = r"([0-1]{32})"
    octal = r"\D(0[0-7]{9,11})\D"
    hexa = r"0x[A-Fa-f0-9]{7,8}"
    deci = r"\D([1-9]{8,10})\D"

    searchSpace = {"dotDec": dotDec, "dotHex": dotHex, "dotOct": dotOct,
                   "dotBin": dotBin, "binary": binary, "octal": octal,
                   "hexa": hexa, "deci": deci}

    masterLedger = {}

    for parse in searchSpace:
        IPS = re.compile(searchSpace[parse]).findall(dump)
        tmpLedger = makeTmpLedger(IPS)          # Convert to count dict
        convertLedger(tmpLedger, parse)         # Convert to dot decimal
        merge(masterLedger, tmpLedger)          # Combine with master dict
        del tmpLedger

    return(max(masterLedger, key=masterLedger.get))


def convertLedger(tmpLedger, mode):
    # Converts the IP keys of a dictionary to dot decimal form
    if mode is "dotDec":
        pass

    elif mode is "dotHex":
        IPs = [IP for IP in tmpLedger]
        for IP in IPs:
            tmpLedger[".".join(str(int(HEX, 16)) for
                      HEX in IP)] = tmpLedger.pop(IP)
        del IPs

    elif mode is "dotOct":
        IPs = [IP for IP in tmpLedger]
        for IP in IPs:
            tmpLedger[".".join(str(int(OCT, 8)) for
                      OCT in IP)] = tmpLedger.pop(IP)
        del IPs

    elif mode is "dotBin":
        IPs = [IP for IP in tmpLedger]
        for IP in IPs:
            tmpLedger[".".join(str(int(BIN, 2)) for
                      BIN in IP)] = tmpLedger.pop(IP)

    elif mode is "binary":
        IPs = [IP for IP in tmpLedger]
        for IP in IPs:
            tmpLedger[".".join(str(int(IP[i:i+8], 2)) for
                      i in range(0, 32, 8))] = tmpLedger.pop(IP)

    elif mode is "octal":
        IPs = [IP for IP in tmpLedger]
        for IP in IPs:
            newIP = ipFrom32(int(IP, 8))
            if newIP is not False:
                tmpLedger[newIP] = tmpLedger.pop(IP)
            else:
                tmpLedger.pop(IP)

    elif mode is "hexa":
        IPs = [IP for IP in tmpLedger]
        for IP in IPs:
            tmpLedger[".".join(str(int(IP[i:i+2], 16)) for
                      i in range(2, 10, 2))] = tmpLedger.pop(IP)

    elif mode is "deci":
        IPs = [IP for IP in tmpLedger]
        for IP in IPs:
            newIP = ipFrom32(int(IP))
            if newIP is not False:
                tmpLedger[newIP] = tmpLedger.pop(IP)
            else:
                tmpLedger.pop(IP)


def makeTmpLedger(IPS):
    # Creates a temporary frequency dictionary
    tmpLedger = {}
    for IP in IPS:
        if IP not in tmpLedger:
            tmpLedger[IP] = 1
        else:
            tmpLedger[IP] += 1

    return(tmpLedger)


def merge(masterLedger, tmpLedger):
    # Merge two frequency dictionaries
    for IP in tmpLedger:
        if IP not in masterLedger:
            masterLedger[IP] = tmpLedger[IP]
        else:
            masterLedger[IP] += tmpLedger[IP]


def ipFrom32(IP):
    # Converts from 32 bit IP to standard format
    try:
        IP = struct.pack('!I', IP)
        IP = socket.inet_ntoa(IP)
        return(IP)
    except socket.error:
        return(False)
    except struct.error:
        return(False)


if __name__ == "__main__":
    dump = open(argv[1], "r").read()
    print(findHacker(dump))
