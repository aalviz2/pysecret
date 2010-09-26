#! /usr/local/bin/python
#-*- coding: utf-8 -*-

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2010/10/26 $"
__copyright__ = "Copyright (c) 2009 Cedric Bonhomme"
__license__ = "GPL v3"

def encrypt(mot, cle):
    """
    Cesar encryption.
    """
    return "".join([chr((ord(caractere)+ord(cle)%26)-65) for caractere in mot])

def decrypt(chaine, cle):
    """
    Cesar decryption.
    """
    return "".join([chr((ord(caractere)-ord(cle))%26+65)  for caractere in chaine])

def bruteforce(mot):
    """
    Cesar brute force.
    """
    return "\n".join([str((chr(cle+65),decrypt(mot, chr(cle+65)))) for cle in range(26)])

if __name__ == '__main__':
    # Point of entry in execution mode
    #print decrypt(encrypt("BONJOUR", "B"))
    print bruteforce(encrypt("BONJOUR", "B"))