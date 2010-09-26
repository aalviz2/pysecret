#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2010/10/26 $"
__copyright__ = "Copyright (c) 2009 Cedric Bonhomme"
__license__ = "GPL v3"

import utils

class El_gamal(object):
    def __init__(self, p = None, a = None, alpha = None):
        """
        Initialization.
        """
        if p == None and a == None:
            pass
        self.alpha = alpha
        self.p = p
        self.beta = pow(self.alpha, a, self.p)

        self.pub = (self.p, self.alpha, self.beta)
        self.priv = a

    def encrypt(self, x, lambada):
        """
        Encrypt x with lanbda.
        """
        y1 = pow(self.alpha, lambada, self.p)
        y2 = (x * pow(self.beta, lambada, self.p)) % self.p
        return (y1, y2)

    def decrypt(self, y):
        """
        Decrypt y.
        """
        return (y[1] * utils.inv_modulo(pow(y[0], self.priv, self.p), \
                    self.p)) % self.p

    def sign(self, x, lambada):
        """
        Sign the message x.
        """
        gamma = pow(self.alpha, lambada, self.p)
        delta = ((x - self.priv * gamma) * \
                    utils.inv_modulo(lambada, self.p - 1)) % (self.p - 1)
        return (gamma, delta)

    def verify(self, x, sig):
        """Check the signature."""
        return \
            (pow(self.beta, sig[0], self.p) * \
            pow(sig[0], sig[1], self.p)) % self.p \
            == pow(self.alpha, x, self.p)

    def __str__(self):
        """
        Pretty display of the keys.
        """
        return """Public key: %s\nPrivate key: %s""" % % (self.pub, self.priv)

if __name__ == "__main__":
    # Point of entry in execution mode
    el = El_gamal(23, 6, 7)
    print el
    print "Texte chiffré :", el.encrypt(7, 3)
    print "Texte déchiffré :", el.decrypt(el.encrypt(7, 3))

    print "Signature :", el.sign(7, 5)
    print "Vérification signature :", el.verify(7, el.sign(7, 5))