#! /usr/local/bin/python
#-*- coding: utf-8 -*-

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2009/01/27 $"
__copyright__ = "Copyright (c) 2009-2010 Cedric Bonhomme"
__license__ = "GPL v3"

import utils

def encrypt(word, key):
    """
    Vigenere encryption.
    """
    l, k = [], 0
    for i in word:
        if i.isalpha():
            l.append(chr((ord(i) + ord(key[k])) % 26 + 65))
        else:
            l.append(i)
        k = (k+1) % len(key)
    return "".join(l)

def decrypt(word, key):
    """
    Vigenere decryption.
    """
    l, k = [], 0
    for i in word:
        if i.isalpha():
            l.append(chr((ord(i) - ord(key[k])) % 26 + 65))
        else:
            l.append(i)
        k = (k+1) % len(key)
    return "".join(l)

def matrice_vig(key):
    """
    Matrice of Vigenere
    """
    l = []
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l.append(alp)
    for i in key:
        tmp = []
        for j in alp:
            tmp.append(chr((ord(i) + ord(j)) % 26 + 65))
        l.append("".join(tmp))
    return "\n".join(l)

def analyse_vig(message, length=None):
    if length == None:
        pass

    sch = []
    for i in range(length):
        s = ""
        j=i
        while j<len(message):
            s += message[j]
            j += length
        sch.append(s)

    print sch

    key = ""
    for s in sch:
        """ pour chaque sous-chaine, on calcule la key necessaire pour que la
        lettre la plus frequente corresponde a un E
        """
        freq = utils.word_frequency(s)
        print s, freq
        key += chr(ord(freq[0][0]) - 4)
    return key

if __name__ == '__main__':
    #print decrypt(encrypt("THISCRYPTOSYSTEMISNOTSECURE", "THEKEY"), "THEKEY")

    cry = "KQOWEFVJPUJUUNUKGLMEKJINMWUXFQMKJBGWRLFNFGHUDWUUMBSVLPS\
NCMUEKQCTESWREEKOYSSIWCTUAXYOTAPXPLWPNTCGOJBGFQHTDWXIZA\
YGFFNSXCSEYNCTSSPNTUJNYTGGWZGRWUUNEJUUQEAPYMEKQHUIDUXFP\
GUYTSMTFFSHNUOCZGMRUWEYTRGKMEEDCTVRECFBDJQCUSWVBPNLGOYL\
SKMTEFVJJTWWMFMWPNMEMTMHRSPXFSSKFFSTNUOCZGMDOEOYEEKCPJR\
GPMURSKHFRSEIUEVGOYCWXIZAYGOSAANYDOEOYJLWUNHAMEBFELXYVL\
WNOJNSIOFRWUCCESWKVIDGMUCGOCRUWGNMAAFFVNSIUDEKQHCEUCPFC\
MPVSUDGAVEMNYMAMVLFMAOYFNTQCUAFVFJNXKLNEIWCWODCCULWRIFT\
WGMUSWOVMATNYBUHTCOCWFYTNMGYTQMKBBNLGFBTWOJFTWGNTEJKNEE\
DCLDHWTVBUVGFBIJG"


    #key =  analyse_vig(encrypt("BONJOURCOMMENTALLEZVOUS", "SALUT"), 6)
    #print key
    #print decrypt(cry, key)


    print decrypt(encrypt("BONJOUR COMMENT ALLEZ VOUS ?", "SALUT"), "SALUT")