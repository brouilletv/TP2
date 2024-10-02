"""
projet fait par: Vincent Brouillet
groupe: 405
un jeu de devinette
"""
import random as r


def start():
    borne = input(f"voulez vous choisir les borne? y/n")
    if borne == "n":
        minimum = 1
        maximum = 100
    else:
        minimum = int(input(f"minimum?"))
        maximum = int(input(f"maximum?"))
    print(f"les borne sont {minimum} et {maximum}")
    devinette(r.randint(minimum, maximum), 0)


def devinette(nombre_rechercher, nombre_essaie):
    nombre_essaie += 1
    essaie = int(input(f"Entrez votre essaie"))
    if essaie > nombre_rechercher:
        print(f"le nombre est plus petit")
        devinette(nombre_rechercher, nombre_essaie)
    elif essaie < nombre_rechercher:
        print(f"le nombre est plus grand")
        devinette(nombre_rechercher, nombre_essaie)
    elif essaie == nombre_rechercher:
        print(f"Bonne réponse \nnombre d'essaie: {nombre_essaie}")
        nombre_rechercher = input("Quit? y/n")
        if nombre_rechercher == "n":
            start()
        else:
            print(f"au revoir")
            quit()
    else:
        print(f"error")
        devinette(nombre_rechercher, nombre_essaie)


start()
