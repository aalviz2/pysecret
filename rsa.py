#! /usr/bin/python
#-*- coding: utf-8 -*-

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2010/10/26 $"
__copyright__ = "Copyright (c) 2009 Cedric Bonhomme"
__license__ = "GPL v3"

import math
import zlib
import random
import base64
import hashlib

from cPickle import dumps, loads

import utils

class RSA(object):
    """
    RSA cipher.
    """
    def __init__(self, p = None, q = None, b = None, nb_bits = 256):
        """Initialise les clés.

        Génère 'p' et 'q' premiers de taille 'nb_bits' bits aléatoirment,
        calcul a,b et n à l'aide de phi et de b.
        """
        if p == None and q == None:
            p = random.getrandbits(nb_bits)
            q = random.getrandbits(nb_bits)
            while not utils.miller_rabin_version1(p):
                p = random.getrandbits(nb_bits)
            while not utils.miller_rabin_version1(q):
                q = random.getrandbits(nb_bits)
        n   = p * q
        phi = (p - 1) * (q - 1)
        if b == None:
            while True:
                b = random.randint(2, phi - 1)
                if utils.premier(b, phi):
                    break
        a  = utils.inv_modulo(b, phi)
        self.a = a
        self.b = b
        self.n = n

    def encrypt_int(self, x):
        """Chiffre le message."""
        #return pow(x, self.b, self.n)
        return utils.expo_modulaire_rapide(x, self.b, self.n)

    def decrypt_int(self, y):
        """Déchiffre le message."""
        #return pow(y, self.a, self.n)
        return utils.expo_modulaire_rapide(y, self.a, self.n)

    def encrypt_text(self, message):
        """Encrypts a string 'message' with the public key 'key'"""
        return self.chopstring(message, self.encrypt_int)

    def decrypt_text(self, cypher):
        """Decrypts a cypher with the private key 'key'"""
        return self.gluechops(cypher, self.decrypt_int)

    def chopstring(self, message, funcref):
        """Découpe 'message' en bloc d'au plus n,
        converti en entier, et appel funcref(integer) pour chaque bloc.

        Utilisée par encrypt_text
        """
        msglen = len(message)
        mbits = msglen * 8
        nbits = int(math.floor(utils.log(self.n, 2)))
        nbytes = nbits / 8
        blocks = msglen / nbytes

        if msglen % nbytes > 0:
            blocks += 1

        cypher = []

        for bindex in range(blocks):
            offset = bindex * nbytes
            block = message[offset:offset+nbytes]
            value = utils.bytes2int(block)
            cypher.append(funcref(value))

        return self.picklechops(cypher)

    def gluechops(self, chops, funcref):
        """Recompose les blocs en string,
        et appel funcref(integer) pour chaque bloc.

        Utilisée par decryt_text
        """
        message = ""

        chops = self.unpicklechops(chops)

        for cpart in chops:
            mpart = funcref(cpart)
            message += utils.int2bytes(mpart)

        return message

    def picklechops(self, chops):
        """Sérialise et transforme 'chops' en base 64."""
        value = zlib.compress(dumps(chops))
        encoded = base64.encodestring(value)
        return encoded.strip()

    def unpicklechops(self, string):
        """Désérialise 'string'."""
        return loads(zlib.decompress(base64.decodestring(string)))


    def __str__(self):
        """
        Pretty display of the keys.
        """
        return """Private key: %s\nPublic key: %s\nModulo: %s""" % (self.a, self.b, self.n)


if __name__ == '__main__':
    # Point d'entrée en mode exécution.
    rsa = RSA(nb_bits = 128)
    print rsa
    cr = rsa.encrypt_text("Bonjour, comment allez-vous ?")
    dcr = rsa.decrypt_text(cr)
    print
    print "Cipher text :"
    print cr
    print
    print "Text :"
    print dcr