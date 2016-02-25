# Reuben Thorpe (2016), CodeEval [Seek For An Intruder v1.0]
# Bottle neck, most likly regex parse, memory leak
from sys import argv
from operator import itemgetter
import socket
import struct
import re


def findHacker(dump):
    """
    This function returns the most commonly found IP address in a string,
    the IP address can be in the following forms.

        Dotted decimal : 192.0.2.235 with no leading zero.
        Dotted hexadecimal : 0xc0.0x0.0x02.0xeb
        Dotted octal : 0300.0000.0002.0353
        Dotted binary : 11000000.00000000.00000010.11101011
        Binary : 11000000000000000000001011101011
        Octal : 030000001353
        Hexadecimal : 0xC00002EB
        Decimal : 3221226219

    """
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

    searchSpace = (dotDec, dotHex, dotOct, dotBin, binary, octal, hexa, deci)
    ledger = {}

    for parse in searchSpace:
        matches = re.compile(parse).findall(dump)
        if parse is dotDec:
            for IP in matches:
                addToLedger(IP, ledger)

        elif parse is dotHex:
            IPS = ((".".join(str(int(HEX, 16)) for HEX in IP) for
                   IP in matches))
            for IP in IPS:
                addToLedger(IP, ledger)

        elif parse is dotOct:
            IPS = (".".join(str(int(OCT, 8)) for OCT in IP) for
                   IP in matches)
            for IP in IPS:
                addToLedger(IP, ledger)

        elif parse is dotBin:
            IPS = (".".join(str(int(BIN, 2)) for BIN in IP) for
                   IP in matches)
            for IP in IPS:
                addToLedger(IP, ledger)

        elif parse is binary:
            IPS = (".".join(str(int(IP[i:i+8], 2)) for
                            i in range(0, 32, 8)) for
                   IP in matches)
            for IP in IPS:
                addToLedger(IP, ledger)

        elif parse is octal:
            IPS = (int(IP, 8) for IP in matches)
            for IP in IPS:
                convAddToLedger(IP, ledger) # DISS

        elif parse is hexa:
            IPS = (".".join(str(int(IP[i:i+2], 16)) for
                            i in range(2, 10, 2)) for
                   IP in matches)
            for IP in IPS:
                addToLedger(IP, ledger)

        else:
            for IP in matches:
                convAddToLedger(int(IP), ledger) # DISS

    result = max(ledger, key=ledger.get)
    return(result)


def convAddToLedger(IP, ledger):
    # Converts from 32 bit IP and then adds to leger
    try:
        IP = struct.pack('!I', IP)
        IP = socket.inet_ntoa(IP)
    except socket.error:
        return(False)
    except struct.error:
        return(False)

    addToLedger(IP, ledger)


def addToLedger(IP, ledger):
    # Adds 32 bit IP to ledger
    if IP not in ledger:
        ledger[IP] = 1
    else:
        ledger[IP] += 1


if __name__ == "__main__":
    dump = open(argv[1], "r").read()
    print(findHacker(dump))
