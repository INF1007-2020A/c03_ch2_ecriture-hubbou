#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    resultat = ''
    for lettre in mot:
        # TODO completer la fonction ici
        
        resultat += lettre
    return mot

def dissipated_power(voltage, resistance):
    return pow(voltage, 2) / resistance

def orthogonal(vec1, vec2):
    if (vec1[0] * vec2[0] + vec1[0])


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
