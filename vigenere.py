#! /usr/local/bin/python
#-*- coding: utf-8 -*-

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2009/01/27 $"
__copyright__ = "Copyright (c) 2009 Cedric Bonhomme"
__license__ = "Python"

import utils

def encrypt(mot, cle):
    """Cryptage de Vigenère.
    """
    l, k = [], 0
    for i in mot:
        l.append(chr((ord(i) + ord(cle[k])) % 26 + 65))
        k = (k+1) % len(cle)
    return "".join(l)

def decrypt(mot, cle):
    """Décryptage de Vigenère.
    """
    l, k = [], 0
    for i in mot:
        l.append(chr((ord(i) - ord(cle[k])) % 26 + 65))
        k = (k+1) % len(cle)
    return "".join(l)

def matrice_vig(cle):
    """Matrice de vigenere
    """
    l=[]
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l.append(alp)
    for i in cle:
        tmp=[]
        for j in alp:
            tmp.append(chr((ord(i)+ord(j))%26+65))
        l.append("".join(tmp))
    return "\n".join(l)

def analyse_vig(message, taille=None):
    if taille==None:
        pass

    sch = []
    for i in range(taille):
        s = ""
        j=i
        while j<len(message):
            s+=message[j]
            j+=taille
        sch.append(s)

    print sch

    cle=""
    for s in sch:
        """ pour chaque sous-chaine, on calcule la cle necessaire pour que la
        lettre la plus frequente corresponde a un E
        """
        freq = utils.frequence(s)
        print s, freq
        cle+=chr(ord(freq[0][0])-4)
    return cle

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
    cle =  analyse_vig(encrypt("BONJOURCOMMENTALLEZVOUS", "SALUT"), 6)

    print cle
    #print decrypt(cry, cle)