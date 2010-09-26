#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2010/10/26 $"
__copyright__ = "Copyright (c) 2009 Cedric Bonhomme"
__license__ = "GPL v3"

import time
import tkFileDialog

from Tkinter import *

import rsa
import utils

lorem = """\
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

class KryptoKraphic(object):
    """KryptoKraphic Class.

    A beautiful GUI for RSA.
    """
    def __init__(self):
        """ Constructeur de la fenêtre principale """
        self.root = Tk()
        self.root.title('Krypto RSA')
        self.root.resizable(height = False, width = True)


        # ---- Création d'un objet RSA ----
        self.nb_bits = 128
        self.rsa = rsa.RSA(nb_bits = self.nb_bits)


        # ---- Définitions des formats de fichiers ----
        self.formats = [ \
                        ('Format', '*.key'), \
                        ('Tous', '*.*') \
                       ]


	# ---- Champ de saisie ----
        self.text = Text(self.root, wrap = WORD)
        self.text.grid(row = 1, column = 1, columnspan = 2)
        self.text.insert("1.0", lorem, lorem.encode('UTF-8'))


        # ---- Bouttons ----
        Button(self.root, text = 'Crypter', fg = 'black',   \
			command = self.code).grid(row = 2, column = 1)
        Button(self.root, text = 'Décrypter', fg = 'black', \
			command = self.decode).grid(row = 2, column = 2)


        Scale(self.root, length=150, orient=HORIZONTAL, sliderlength = 25,   \
			label = 'Taille de la clé :', from_=128, to=1024,    \
			tickinterval = 256, resolution = 128, showvalue = 0, \
			command = self.key_length).grid(row = 3, column = 1, \
							columnspan = 2)


        # ---- Menu de la fenêtre principale ----
        barre = Menu(self.root)
        # menu Fichier
        menu_fichier  = Menu(barre,tearoff=0)
        menu_fichier.add_command(label="Crypter un texte", command = self.texte)
        menu_fichier.add_separator()
        menu_fichier.add_command(label="Quitter", command = self.root.quit)
        # menu Clés
        menu_cles = Menu(barre,tearoff=0)
        menu_cles.add_command(label="Exporter", command = self.save_key)
        menu_cles.add_command(label="Importer", command = self.loadKey)
        menu_cles.add_separator()
        menu_cles.add_command(label="Regénérer", command = self.new_keys)
        menu_cles.add_command(label="Afficher", command = self.print_keys)
        # menu Aide
        menu_aide = Menu(barre,tearoff=0)
        menu_aide.add_command(label="À propos de Krypto RSA", command = self.about)

        barre.add_cascade(label="Fichier", menu=menu_fichier)
        barre.add_cascade(label="Clés", menu=menu_cles)
        barre.add_cascade(label="Aide", menu=menu_aide)
        self.root.config(menu=barre)

        self.root.mainloop()

    def new_keys(self):
        """ Generate new RSA keys. """
        debut = time.clock()
        bits = self.nb_bits / 2
        self.rsa = rsa.RSA(nb_bits = self.nb_bits)
        fin = time.clock()
        print "Nouvelles clés de " + str(self.nb_bits) + \
			" bits générées en " + str(fin - debut) + " secondes."

    def code(self):
        """ Encrypt the text. """
        try:
            mot = self.text.get(1.0, END)
        except ValueError:
            print "Erreur de conversion !\nEntrée non valide !\n"
            pass
        try:
            enc = self.rsa.encrypt_text(str(mot))
	except:
	    print "Oups"
	    enc = ""
        self.text.delete("1.0", END)
        self.text.insert("1.0", enc, enc.encode('UTF-8'))
        print enc

    def decode(self):
        """ Decrypt the text. """
        try:
            mot = self.text.get(1.0, END)
        except ValueError:
            print "Erreur de conversion !\nEntrée non valide !\n"
            pass
        try:
            dec = self.rsa.decrypt_text(str(mot))
	except:
            print "Oups"
	    dec = ""
        self.text.delete("1.0", END)
        self.text.insert("1.0", dec[:-1], dec.encode('UTF-8'))
        print dec

    def key_length(self,nb):
        """ Change the length of the keys. """
        self.nb_bits = int(nb)
        print "Taille de clé : " + str(nb)

    def print_keys(self):
        """ Print current keys. """
        print self.rsa

    def loadKey(self):
        """ Load saved keys. """
        file = tkFileDialog.askopenfile(parent = self.root, filetypes = self.formats, mode='rb', title='Importer...')
        if file != None:
            try:
                data = file.read()
                file.close()
            except:
                print "Erreur de lecture !"
            print data
            print "Octets du fichier lu : %d octets." % len(data)

    def save_key(self):
        """ Save current Keys coded by XML format. """
        file = tkFileDialog.asksaveasfile(parent = self.root, filetypes = self.formats, title ="Exporter...", mode='a')
        if file != None:
            dico = {}
            proprietaire = "Bob"
            dico['publique'] = "<publique>" + str(self.rsa.b) + "</publique>"
            dico['prive'] = "<prive>" + str(self.rsa.a) + "</prive>"
            dico['modulus'] = "<modulus>" + str(self.rsa.n) + "</modulus>"
            dico['nbBits'] = "<nbBits>" + str(self.nb_bits) + "</nbBits>"
            try:
                file.write("<%s>" % proprietaire)
                for clef, valeur in dico.items():
                    file.write("\n\t%s" % (valeur))
                file.write("\n</%s>\n" % proprietaire)
                file.close()
            except :
                print "Erreur d'écriture !"
            print "Sauvegardé dans %s" % file.name

    def texte(self):
        """ Open ..."""
        pass

    # ---- About ----
    def about(self):
        """ Help. """
        print "GUI by Cédric Bonhomme."
        print "For RSA Crypto System."


if __name__ == '__main__':
    # Point d'entrée en mode exécution
    KryptoKraphic() # objet application