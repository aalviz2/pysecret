#! /usr/local/bin/python
#-*- coding: utf-8 -*-

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2010/10/26 $"
__copyright__ = "Copyright (c) 2009 Cedric Bonhomme"
__license__ = "GPL v3"

import utils

def encrypt(mot, permutation):
    """
    Permutation encryption.
    """
    n = len(permutation)
    tableau = [list(mot[i*n:(i*n)+n]) for i in range(0, len(mot)/n)]
    if len(mot) % n != 0:
        tableau.append(list(mot[(len(mot) - len(mot) % n):]))
        tableau[-1].extend('X' * (n - len(mot) % n))
    tmp = [i[:] for i in tableau]
    for i, sous_chaine in enumerate(tableau):
        for j, p in enumerate(permutation):
            sous_chaine[j] = tmp[i][p]
    return "".join(["".join(i) for i in tableau])

def decrypt(mot, permutation):
    """
    Permutation decryption.
    """
    n = len(permutation)
    tableau = [list(mot[i*n:(i*n)+n]) for i in range(0, len(mot)/n)]
    tmp = [i[:] for i in tableau]
    for i, sous_chaine in enumerate(tableau):
        for j, p in enumerate(permutation):
            sous_chaine[p] = tmp[i][j]
    return "".join(["".join(i) for i in tableau])

def bruteforce(mot):
    """
    Permutation brute force.
    """
    resultat = []
    for i in range(1, 6):
        if (len(mot) % i) == 0:
            for p in utils.all_perms(range(i)):
                resultat.append(decrypt(mot, p))
    return "\n".join(resultat)


if __name__ == '__main__':
    # Point of entry in execution mode
    #print decrypt(encrypt("BIENTOTLESVACANCES", [2,4,0,1,3]), [2,4,0,1,3])
    print bruteforce(encrypt("BIENTOTLESVACANCES", [2,4,0,1,3]))