#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    resultat = ''
    for lettre in mot:
        # TODO completer la fonction ici
        
        resultat += lettre
    return mot

    

def dissipated_power(voltage, resistance):
    print("")
    print(voltage)
    print(resistance)
    power = voltage**2 / resistance
    print(power)
    return power

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

def bills(amount):
    if amount < 0:
        return None

    nbVingt = amount // 20
    amount -= nbVingt * 20
    
    nbDix = amount // 10
    amount -= nbDix * 10
    
    nbCinq = amount // 5
    amount -= nbCinq * 5
    
    nbUn = amount

    return (nbVingt, nbDix, nbCinq, nbUn)


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
