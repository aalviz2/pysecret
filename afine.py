#! /usr/local/bin/python
#-*- coding: utf-8 -*-

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2010/10/26 $"
__copyright__ = "Copyright (c) 2009 Cedric Bonhomme"
__license__ = "GPL v3"

import string

import utils

def encrypt(mot, cle):
    """
    Afine encryption.
    """
    return [(chr(((ord(i) - 65) * cle[0] + cle[1]) % 26 + 65)) for i in mot]

def decrypt(mot, cle):
    """
    Afine decryption
    """
    inv = utils.inv_modulo(cle[0], 26)
    return [(chr(((ord(i) - 65 - cle[1]) * inv) % 26 + 65)) for i in mot]

def brute_force(mot):
    """"Brute force
    """
    valeurs_a = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    valeurs_b = range(1, 26)
    for i in valeurs_a:
        for j in valeurs_b:
            print (i, j)
            print "".join(decrypt(mot, (i, j)))
            print

if __name__ == '__main__':
    message ="LaventureaMelbournesesttermineebrutalementpourMarionBartoliLaFrancaiseopposeeaVeraZvonarevaen quartsdefinaledelOpendAustralienapasvulejourhormisendebutdepremiersetResultatunedefaiteendeuxmanches"

    print "Cipher text:"
    print "".join(encrypt(string.upper(message), (7, 3)))
    print
    print "Text:"
    print "".join(decrypt("".join(encrypt(string.upper(message), (7, 3))), (7, 3)))
    print
    #brute_force("".join(encrypt(string.upper(message), (7, 3))))