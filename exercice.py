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
    return (vec1[0] * vec2[0] + vec1[1] * vec2[1]) == 0

def average(list):
    somme = 0
    count = 0
    for nb in list:
        if nb >= 0:
            somme += nb
            count += 1
        
    return somme / count

def orthogonal(vec1, vec2):
    return (vec1[0] * vec2[0] + vec1[1] * vec2[1]) == 0


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
