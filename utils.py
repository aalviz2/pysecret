#! /usr/local/bin/python
#-*- coding: utf-8 -*-

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2010/10/26 $"
__copyright__ = "Copyright (c) 2009 Cedric Bonhomme"
__license__ = "GPL v3"

"""Tool box.

Basic mathematical functions for cryptography.
"""

import math
import types
import random
import operator
import itertools

#
# Arithmetic functions
#
def pgcd(x,y):
    """Retourne le PGCD de x et y."""
    assert x or y, "les deux arguments sont nuls " + `x, y`
    while y:
        (x, y) = (y, x%y)
    return abs(x)

def pgcd_bezout(x,y):
    """Retourne (d,u,v) tel que d == pgcd(a,b) == au + bv.
    """
    assert x or y, "mauvais arguments " + `x, y`
    assert x >= 0 and y >= 0, "mauvais arguments " + `x, y`
    if y == 0:
        return (x, 1, 0)
    (d, xp, yp) = pgcd_bezout(y , x%y)
    return (d, yp, xp - x/y * yp)

def log(x, base = 10):
    """Retourne le logarithme népérien de 'x'."""
    return math.log(x) / math.log(base)

def euler(nb):
    """Calcul de Euler."""
    return [a for a in range(0,nb) if pgcd(a,nb) == 1]


#
# Modular arithmetic functions
#
def expo_modulaire_rapide(a, p ,n):
    """Calcul l'exposant modulaire (pow()).

    Selon Wikipédia (http://fr.wikipedia.org/wiki/Exponentiation_modulaire)
    """
    result = a % n
    remainders = []
    while p != 1:
        remainders.append(p & 1)
        p = p >> 1
    while remainders:
        rem = remainders.pop()
        result = ((a ** rem) * result ** 2) % n
    return result

def inv_modulo(a,m):
    """Retourne l'inverse modulaire de a modulo m.
    """
    assert m > 1, "mauvais arguments " + `a, m`
    (d, x, _) = pgcd_bezout(a, m)
    if d == 1:
        return x % m
    return None

def eqn_modulaire(a,b,m):
    """ Resolution de a*x=b%m
    """
    return (b * inv_modulo(a, m)) % m

#
# Tests de primalité classiques
#

def premier(a, b):
    """Renvoie True si a et b sont premiers entre eux.
    """
    assert a or b, "les deux arguments sont nuls " + `a, b`
    return pgcd(a, b) == 1

def est_premier(n):
    """Renvoie True si un nombre est premier, False sinon.
    """
    if n == 2:
        return True
    elif (n == 1 or n % 2 == 0):
        return False
    else:
        r = int(math.sqrt(n))
        i = 3
        while i <= r:
            if n % i == 0:
                return 0
            i = i + 2
        return True



#
# Tests de primalité probabilistes
#


def petit_theoreme_fermat(p):
    """Retourne True si p semble être premier, False si il ne l'est pas."""
    a = random.randint(1, p-1)
    return expo_modulaire_rapide(a, p - 1, p) == 1


# Miller-Rabin. Première version.
def miller_rabin_pass(a, n):
    d = n - 1
    s = 0
    while d & 1:
        d = d >> 1
        s = s + 1

    a_to_power = expo_modulaire_rapide(a, d, n)
    if a_to_power == 1:
        return True
    for i in xrange(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1

def miller_rabin_version1(n):
    for repeat in xrange(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, n):
            return False
    return True


# Miller-Rabin. Deuxième version.
def millerTest(a, i, n):
    if i == 0:
        return 1
    x = millerTest(a, i / 2, n)
    if x == 0:
        return 0
    y = (x * x) % n
    if ((y == 1) and (x != 1) and (x != (n - 1))):
        return 0
    if (i % 2) != 0:
        y = (a * y) % n
    return y

def miller_rabin_version2(n):
    if millerTest(random.randint(2, n - 2), n - 1, n) == 1:
        return True
    return False


# Jacobi
def jacobi(a, b):
    """Renvoie la valeur du symbol de Jacobi."""
    if a % b == 0:
        return 0
    result = 1
    while a > 1:
        if a & 1:
            if ((a-1)*(b-1) >> 2) & 1:
                result = -result
            b, a = a, b % a
        else:
            if ((b ** 2 - 1) >> 3) & 1:
                result = -result
            a = a >> 1
    return result

def jacobi_witness(x, n):
    """Returns False if n is an Euler pseudo-prime with base x, and
    True otherwise.
    """
    j = jacobi(x, n) % n
    f = fast_exponentiation(x, (n-1)/2, n)
    if j == f:
        return False
    return True







def reste_chinois(la,lm):
    """Retourne la solution du théorème chinois.
    """
    M = reduce(operator.mul, lm)
    lM = [M/mi for mi in lm]
    ly = map(inv_modulo, lM, lm)
    laMy = map((lambda ai, Mi, yi : ai*Mi*yi), la, lM, ly)
    return sum(laMy) % M

def eratosthenes_prime_gen():
    """Génère des nombres premiers avec le crible d'Eratosthenes.
    """
    d = {}
    for i in itertools.count(2):
        if i in d:
            for j in d[i]:
                d[i + j] = d.get(i + j, []) + [j]
            del d[i]
        else:
            d[i * i] = [i]
            yield i

def factorise(n):
    """Factorise un nombre.
    """
    factors = []
    for p in eratosthenes_prime_gen():
        if p * p > n:
            break
        while n % p == 0:
            n /= p
            factors.append(p)
    if n != 1:
        factors.append(n)
    return factors

def nombrePremierListe(n):
    """Renvoi la liste des nombre premier inférieurs à n.
    """
    generateur = eratosthenes()
    return [generateur.next() for _ in range(n)]

def all_perms(liste):
    """Renvoie toutes les permutations d'une liste.
    """
    if len(liste) <=1:
        yield liste
    else:
        for perm in all_perms(liste[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + liste[0:1] + perm[i:]

def frequence(mot):
    """Fréquence d'apparition des lettres d'un mot.
    """
    dic = {}
    for i in mot:
        if i in dic:
            dic[i] = dic[i] + 1
        else:
            dic[i] = 1
    liste = dic.items()
    liste.sort(key = operator.itemgetter(1), reverse = True)
    return liste



def resolve_system(a,b,m):
    """Résolution du système d'équations a et b
    """
    a1 = [(i*b[0])%m for i in a]
    b1 = [(i*a[0])%m for i in b]
    c1 = [(i-j)%m for (i, j) in itertools.izip(a1, b1)]
    y = eqn_modulaire(c1[1], c1[2], m);
    x = eqn_modulaire(a[0], (a[2]-a[1]*y)%m, m)
    return (x,y)

def equation(mat1, mat2):
    """Résolution d'équations.

    Résolution d'un système d'équation affines modulaires.
    """
    c1 = mat1[0] - mat1[1]
    c2 = mat2[0][0] - mat2[0][1]
    c3 = mat2[1][0] - mat2[1][1]
    a, b = 0, 0

    if c1 <= 0:
       c1 = c1 % 31
    if c2 <= 0:
       c2 = c2 % 31

    inv = inv_modulo(c2, 31)
    if inv != None:
        a = (c1 * inv) % 31
    else:
        l = []
        for i in range(1, 31):
            if (c2 * i) % 31 == c1:
                l.append(i)
        for i in l:
            if pgcd(31, 6) != 1:
                l.remove(i)
	a = l[0]

    b = (mat1[1] - mat2[0][1] * a) % 31

    return (a, b)


def determinant(matrice):
    return (matrice[0][0] * matrice[1][1]) - \
                    (matrice[1][0] * matrice[0][1])

def systeme_ordre_deux(matrice1, matrice2):
    determinant_denominateur = determinant(matrice1)
    determinant_numerateur1 = determinant([matrice2, [matrice1[1][0], matrice1[1][1]]])
    determinant_numerateur2 = determinant([[matrice1[0][0], matrice1[0][1]], matrice2])

    return ((determinant_numerateur1/determinant_denominateur) ,
            (determinant_numerateur2/determinant_denominateur))

def system2inconnusResolve(x1, y1, x2, y2):
    xtmp = (x1 - x2) % 26
    ytmp = (y1 - y2) % 26
    a = (ytmp * inv_modulo(xtmp, 26)) % 26
    b = (y2 - (x2 * a)) % 26
    return a, b


def racine_cubique(a):
    """Renvoie la racine cubique de a."""
    for i in range(10000):
        if pow(i,3) == a:
            return i
    return None

def inversible(matrice):
    """Renvoie True si une matrice 2*2 est inversible dans Z26."""
    determinant = matrice[0][0] * matrice[1][1] - \
                    matrice[1][0] * matrice[0][1]
    return pgcd(determinant, 26) == 1

def inv_matrix(matrice):
    """Inverse une matrice 2*2."""
    if not inversible(matrice):
        return "Non inversible matrix"
    resultat = [i[:] for i in matrice]
    resultat[0][0] = matrice[1][1]
    resultat[1][1] = matrice[0][0]
    resultat[1][0] = (-matrice[1][0]) % 26
    resultat[0][1] = (-matrice[0][1]) % 26
    return resultat


#
# FONCTIONS DE CONVERSIONS
#

def int_to_bin(x, count = 8):
    """Transforme un entier en binaire."""
    return "".join(map(lambda y : str((x >> y) & 1), range(count-1, -1, -1)))

def bin_to_decimal(x):
    """Transforme un binaire en entier."""
    return sum(map(lambda z: int(x[z]) and 2**(len(x) - z - 1),
                   range(len(x)-1, -1, -1)))

def mot_to_bin(mot, count = 8):
    """Transforme un mot en liste de binaires."""
    return [int_to_bin(ord(i), count) for i in mot]

def binList_to_mot(liste):
    """Transforme une liste de binaires en mot."""
    return "".join([chr(bin_to_decimal(i)) for i in liste])

def bytes2int(bytes):
    """
    >>> (128*256 + 64)*256 + + 15
    8405007
    >>> l = [128, 64, 15]
    >>> bytes2int(l)
    8405007
    """
    if not (type(bytes) is types.ListType or type(bytes) is types.StringType):
        raise TypeError("Liste ou String.")

    # Convert byte stream to integer
    integer = 0
    for byte in bytes:
        integer <<= 8 #integer *= 256
        if type(byte) is types.StringType:
            byte = ord(byte)
        integer += byte

    return integer

def int2bytes(number):
    """
    >>> bytes2int(int2bytes(123456789))
    123456789
    """
    if not (type(number) is types.LongType or type(number) is types.IntType):
        raise TypeError("Long ou String.")

    string = ""

    while number > 0:
        string = "%s%s" % (chr(number & 0xFF), string)
        number >>= 8 #integer /= 256

    return string


if __name__ == '__main__':
    # Point d'entrée en exécution
    #print equation([3,24], [[4, 19], [1, 1]])
    #print reste_chinois([5, 3, 7], [10, 17, 9])
    #print reste_chinois([4*inv_modulo(13,99),\
                                #56*inv_modulo(15,101)],[99,101])
    #print inv_modulo(8,31)
    #print factorise(121549788)
    #print est_premier(157)
    #print mot_to_bin("SALUT")
    #print binList_to_mot(mot_to_bin("SALUT"))
    #print miller_rabin_version2(100711433)
    print systeme_ordre_deux([[4, 2], [2, 3]], [24, 16])