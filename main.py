#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    
    result = []
    deja_vus = set()

    for car in s:
        if car not in deja_vus:
            count = s.count(car)
            result.append((car, count))
            deja_vus.add(car)
    return result


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    
    # votre code ici

    # cas de base
    # recherche nombre de caractères identiques au premier
    # appel récursif

    if s == "":
        return []

    # Traitement du premier caractère
    premier = s[0]
    count = s.count(premier)

    reste = s.replace(premier, "")
    return [(premier, count)] + artcode_r(reste)
    

#### Fonction principale


def main():
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
