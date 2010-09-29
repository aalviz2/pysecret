#! /usr/local/bin/python
#-*- coding: utf-8 -*-

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2010/10/26 $"
__copyright__ = "Copyright (c) 2009-2010 Cedric Bonhomme"
__license__ = "GPL v3"

def encrypt(word, dic):
    """
    Substitution encryption.
    """
    return "".join([dic[i] for i in word])

def decrypt(word, dic):
    """
    Substitution decryption.
    """
    dic_decryption = {}
    # Create the dictionnary for the decryption.
    for i in dic:
        for j in dic:
            if dic[j] == i:
                dic_decryption[i] = j
                break
    return encrypt(word, dic_decryption)

if __name__ == '__main__':
    # Point of entry in execution mode
    dic = {'A':'X', 'B':'N', 'C':'Y', 'D':'A', 'E':'H', 'F':'P', 'G':'O', 'H':'G', \
        'I':'Z', 'J':'Q', 'K':'W', 'L':'B', 'M':'T', 'N':'S', 'O':'F', 'P':'L', \
        'Q':'R', 'R':'C', 'S':'V', 'T':'M', 'U':'U', 'V':'E', 'W':'K', 'X':'J', 'Y':'D', 'Z':'I'}

    print decrypt("MGZVYZLGHCMHJMYXSSFMNHAHYCDLMHA", dic)