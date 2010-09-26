#! /usr/local/bin/python
#-*- coding: utf-8 -*-

# Hill encryption with a 2*2 matrix.
#                        |11  8|
# A = [[11,3], [8,7]] =  |3   7| with A inversible in Z26.
#
# Y = xA
# x = YA

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2010/10/26 $"
__copyright__ = "Copyright (c) 2009 Cedric Bonhomme"
__license__ = "GPL v3"

import utils

def encrypt(word, matrix, encryption=True):
    """
    Hill encryption (decryption).
    """
    word = word.upper()
    if not utils.inversible(matrix):
        return "Non inversible matrix"
    if len(word) % 2 != 0:
        word = word + 'X'
    couple = [list(word[i*2:(i*2)+2]) for i in range(0, len(word)/2)]
    result = [i[:] for i in couple]
    if not encryption:
        matrix = utils.inv_matrix(matrix)
    for i, c in enumerate(couple):
        result[i][0] = chr(((ord(c[0])-65) * matrix[0][0] + \
                                (ord(c[1])-65) * matrix[0][1]) % 26 + 65)
        result[i][1] = chr(((ord(c[0])-65) * matrix[1][0] + \
                                (ord(c[1])-65) * matrix[1][1]) % 26 + 65)
    return "".join(["".join(i) for i in result])

def decrypt (word, matrix):
    """
    Hill decryption.
    """
    return encrypt(word, matrix, False)

if __name__ == '__main__':
    # Point of entry in execution mode
    print decrypt(encrypt("VIVELEPYTHON", [[11, 3], [8, 7]]), [[11, 3], [8, 7]])