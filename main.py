#### Imports et définition des variables globales
"""
Artcode
"""

import sys
sys.setrecursionlimit(1200)
#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de 
    caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    l = []
    n = 1
    i = 0
    while i < len(s) - 1:

        if s[i] == s[i + 1]:
            n = n + 1
        else:
            l.append((s[i], n))
            n = 1
        i = i + 1

        # La chaîne est terminée, ajout du dernier Tuple
        if i == len(s) - 1:
            l.append((s[i], n))

    return l


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de 
    caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # Pylint n'aime pas range(len(s)) mais dans ce cas c'est
    # plus pratique
    for i in range(len(s)):
        if i == len(s) - 1:
            return  [(s[i], i + 1)]
        if s[i] != s[i + 1]:
            return [(s[i], i + 1)] + artcode_r(s[i+1:])

    return []

def main():
    """
        Fonction principale
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
