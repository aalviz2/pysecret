#! /usr/local/bin/python
#-*- coding: utf-8 -*-

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2010/10/26 $"
__copyright__ = "Copyright (c) 2009-2010 Cedric Bonhomme"
__license__ = "GPL v3"


def encrypt(mot, cle):
    """
    Autokey cipher encryption.
    """
    l = []
    for i in mot:
        l.extend(chr((ord(i) - 65 + cle) % 26 + 65))
        cle = ord(i) - 65
    return "".join(l)

def decrypt(mot, cle):
    """
    Autokey cipher decryption.
    """
    l = []
    for i in mot:
        cle = (ord(i) - 65 - cle) % 26
        l.extend(chr(cle + 65))
    return "".join(l)

def bruteforce(mot):
    """Brute force.
    """
    return "\n".join([str((cle, decrypt(mot, cle))) for cle in range(26)])

if __name__ == '__main__':
    # Point of entry in execution mode
    #print decrypt(encrypt("VIVELESVACANCES", 8), 8)
    print bruteforce(encrypt("QXQF VFLR TXLG VLWD PRUA", 8))