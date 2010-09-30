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
__copyright__ = "Copyright (c) 2009-2010 Cedric Bonhomme"
__license__ = "GPL v3"

import utils

def encrypt(message, matrix, encryption=True):
    """
    Hill encryption (decryption).
    """
    message = message.upper()
    if not utils.invertible(matrix):
        # The matrix should be invertible.
        return "Non invertible matrix"
    if len(message) % 2 != 0:
        message = message + 'X'
    couple = [list(message[i*2:(i*2)+2]) for i in range(0, len(message)/2)]
    result = [i[:] for i in couple]
    if not encryption:
        # To decrypt, just need to inverse the matrix.
        matrix = utils.inverse_matrix(matrix)
    for i, c in enumerate(couple):
        if c[0].isalpha() and c[1].isalpha():
            result[i][0] = chr(((ord(c[0])-65) * matrix[0][0] + \
                                    (ord(c[1])-65) * matrix[0][1]) % 26 + 65)
            result[i][1] = chr(((ord(c[0])-65) * matrix[1][0] + \
                                    (ord(c[1])-65) * matrix[1][1]) % 26 + 65)
    return "".join(["".join(i) for i in result])

def decrypt (cypher, matrix):
    """
    Hill decryption.
    """
    return encrypt(cypher, matrix, False)

if __name__ == '__main__':
    # Point of entry in execution mode
    print encrypt("Vivement les vacances !", [[11, 3], [8, 7]])
    print decrypt(encrypt("Vivement les vacances !", [[11, 3], [8, 7]]), [[11, 3], [8, 7]])