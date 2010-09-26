#! /usr/local/bin/python
#-*- coding: utf-8 -*-

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2010/10/26 $"
__copyright__ = "Copyright (c) 2009 Cedric Bonhomme"
__license__ = "GPL v3"

import utils

def encrypt(word, permutation):
    """
    Permutation encryption.
    """
    n = len(permutation)
    table = [list(word[i*n:(i*n)+n]) for i in range(0, len(word)/n)]
    if len(word) % n != 0:
        table.append(list(word[(len(word) - len(word) % n):]))
        table[-1].extend('X' * (n - len(word) % n))
    tmp = [i[:] for i in table]
    for i, sous_chaine in enumerate(table):
        for j, p in enumerate(permutation):
            sous_chaine[j] = tmp[i][p]
    return "".join(["".join(i) for i in table])

def decrypt(word, permutation):
    """
    Permutation decryption.
    """
    n = len(permutation)
    table = [list(word[i*n:(i*n)+n]) for i in range(0, len(word)/n)]
    tmp = [i[:] for i in table]
    for i, sous_chaine in enumerate(table):
        for j, p in enumerate(permutation):
            sous_chaine[p] = tmp[i][j]
    return "".join(["".join(i) for i in table])

def bruteforce(word):
    """
    Permutation brute force.
    """
    result = []
    for i in range(1, 6):
        if (len(mot) % i) == 0:
            for p in utils.all_perms(range(i)):
                result.append(decrypt(mot, p))
    return "\n".join(result)


if __name__ == '__main__':
    # Point of entry in execution mode
    #print decrypt(encrypt("BIENTOTLESVACANCES", [2,4,0,1,3]), [2,4,0,1,3])
    print bruteforce(encrypt("BIENTOTLESVACANCES", [2,4,0,1,3]))