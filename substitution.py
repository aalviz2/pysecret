#! /usr/local/bin/python
#-*- coding: utf-8 -*-

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2010/10/26 $"
__copyright__ = "Copyright (c) 2009 Cedric Bonhomme"
__license__ = "GPL v3"

def encrypt(mot, dic):
    """Cryptage par substitution.
    """
    return "".join([dic[i] for i in mot])

def decrypt(mot, dic):
    """Déchiffrement.
    """
    dic_dec = {}
    for i in dic:
        for j in dic:
            if dic[j] == i:
                dic_dec[i] = j
                break
    return encrypt(mot, dic_dec)

if __name__ == '__main__':
    dic = {'A':'X', 'B':'N', 'C':'Y', 'D':'A', 'E':'H', 'F':'P', 'G':'O', 'H':'G', \
        'I':'Z', 'J':'Q', 'K':'W', 'L':'B', 'M':'T', 'N':'S', 'O':'F', 'P':'L', \
        'Q':'R', 'R':'C', 'S':'V', 'T':'M', 'U':'U', 'V':'E', 'W':'K', 'X':'J', 'Y':'D', 'Z':'I'}


    print decrypt("MGZVYZLGHCMHJMYXSSFMNHAHYCDLMHA", dic)