"""
projet fait par: Vincent Brouillet
groupe: 405
un jeu de devinette
"""
import random as r


def start():
    print("J'ai choisi un nombre de 1 à 100.\nÀ vous de le deviner...")
    devinette(r.randint(1, 100), 0)


def devinette(nombre_rechercher, nombre_essaie):
    nombre_essaie += 1
    essaie = int(input("Entrez votre essaie"))
    if essaie > nombre_rechercher:
        print("le nombre est plus petit")
        devinette(nombre_rechercher, nombre_essaie)
    elif essaie < nombre_rechercher:
        print("le nombre est plus grand")
        devinette(nombre_rechercher, nombre_essaie)
    elif essaie == nombre_rechercher:
        print("Bonne réponse \nnombre d'essaie:", nombre_essaie)
        nombre_rechercher = input("Quit? y/n")
        if nombre_rechercher == "n":
            start()
        else:
            print("au revoir")
            quit()
    else:
        print("error")
        devinette(nombre_rechercher, nombre_essaie)


start()
