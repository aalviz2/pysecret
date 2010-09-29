#! /usr/bin/python
#-*- coding: utf-8 -*-

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2010/10/26 $"
__copyright__ = "Copyright (c) 2009-2010 Cedric Bonhomme"
__license__ = "GPL v3"

import math
import random

import utils

class Rabin(object):
    """
    Rabin encryption.
    """
    def __init__(self, p = None, q = None, b = None, nb_bits = 256):
        """
        Initialization of keys.
        """
        if p == None and q == None:
            p = random.getrandbits(nb_bits)
            q = random.getrandbits(nb_bits)
            while not utils.miller_rabin_version1(p):
                p = random.getrandbits(nb_bits)
            while not utils.miller_rabin_version1(q):
                q = random.getrandbits(nb_bits)
        n   = p * q
        if b == None:
            b = random.randint(2, n - 1)
        self.p = p
        self.q = q
        self.b = b

    def encrypt(self, x):
        """
        Encryption of the message.
        """
        return pow(x, 2) + self.b * x

    def decrypt(self, y):
        """
        Decryption of the message.
        """
        r1 = pow(y, (self.p+1)/4, self.p)
        r2 = pow(y, (self.q+1)/4, self.q)

        return (utils.reste_chinois([r1, r2], [self.p, self.q]), \
                utils.reste_chinois([-r1, r2], [self.p, self.q]), \
                utils.reste_chinois([r1, -r2], [self.p, self.q]), \
                utils.reste_chinois([r1, -r2], [self.p, self.q]))

    def __str__(self):
        """
        Pretty display of the keys.
        """
        return """Private key: %s\nPublic key: %s""" % ((self.p, self.q), self.b)

if __name__ == '__main__':
    # Point of entry in execution mode
    rabin = Rabin(nb_bits = 256)
    print rabin