#! /usr/local/bin/python
#-*- coding: utf-8 -*-

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2010/10/26 $"
__copyright__ = "Copyright (c) 2009-2010 Cedric Bonhomme"
__license__ = "GPL v3"

def encrypt(message, key):
    """
    Cesar encryption.
    """
    return "".join([chr((ord(character) + ord(key) % 26) - 65) for character in message])

def decrypt(cypher, key):
    """
    Cesar decryption.
    """
    return "".join([chr((ord(character) - ord(key)) % 26 + 65)  for character in cypher])

def bruteforce(cypher):
    """
    Cesar brute force.
    """
    return "\n".join([str((chr(key + 65), decrypt(cypher, chr(key + 65)))) for key in range(26)])

if __name__ == '__main__':
    # Point of entry in execution mode
    #print decrypt(encrypt("BONJOUR", "B"))
    print bruteforce(encrypt("BONJOUR", "B"))