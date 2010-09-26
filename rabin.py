#! /usr/bin/python
#-*- coding: utf-8 -*-

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2010/10/26 $"
__copyright__ = "Copyright (c) 2009 Cedric Bonhomme"
__license__ = "GPL v3"

import math
import random

import utils

class Rabin(object):
    """Chiffrement de Rabin.
    """
    def __init__(self, p = None, q = None, b = None, nb_bits = 256):
        """Initialise les clés."""
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
        """Chiffre le message."""
        return pow(x, 2) + self.b * x

    def decrypt(self, y):
        """Déchiffre le message."""
        r1 = pow(y, (self.p+1)/4, self.p)
        r2 = pow(y, (self.q+1)/4, self.q)

        return (utils.reste_chinois([r1, r2], [self.p, self.q]), \
                utils.reste_chinois([-r1, r2], [self.p, self.q]), \
                utils.reste_chinois([r1, -r2], [self.p, self.q]), \
                utils.reste_chinois([r1, -r2], [self.p, self.q]))

    def __str__(self):
        """Affichage élégant des clés."""
        return """\
            Clé privée: %s
            Clé publique: %s""" % ((self.p, self.q), self.b)

if __name__ == '__main__':
    # Point d'entrée en mode exécution.
    rabin = Rabin(nb_bits = 256)
    print rabin