#! /usr/local/bin/python
#-*- coding: utf-8 -*-

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2010/10/26 $"
__copyright__ = "Copyright (c) 2009-2010 Cedric Bonhomme"
__license__ = "GPL v3"

def encrypt(message, key):
    """
    Caesar encryption.
    """
    cipher = []
    for character in message.upper():
        if character.isalpha():
            cipher.append(chr((ord(character) + ord(key.upper())) % 26 + 65))
        else:
            cipher.append(character)
    return "".join(cipher)

def decrypt(cipher, key):
    """
    Caesar decryption.
    """
    message = []
    for character in cipher.upper():
        if character.isalpha():
            message.append(chr((ord (character) - ord(key.upper())) % 26 + 65))
        else:
            message.append(character)
    return "".join(message)
    

def bruteforce(cypher):
    """
    Caesar brute force.
    """
    return "\n".join([str((chr(key + 65), decrypt(cypher, chr(key + 65)))) for key in range(26)])

if __name__ == '__main__':
    # Point of entry in execution mode
    print decrypt(encrypt("B ONJOuR", "B"), "b")
    #print bruteforce(encrypt("BONJOUR", "B"))