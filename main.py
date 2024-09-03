import random as r

def start(x, n_e):
    x = r.randint(1,100)
    n_e = 0
    print("J'ai choisi un nombre de 1 à 100.\nÀ vous de le deviner...")
    essaie(x, n_e)
def essaie(x, n_e):
    n_e += 1
    e = int(input("Entrez votre essaie"))
    if e > x:
        print("le nombre est plus petit")
        essaie(x, n_e)
    elif e < x:
        print("le nombre est plus grand")
        essaie(x, n_e)
    elif e == x:
        print("Bonne réponse \nnombre d'essaie:", n_e)
        r = input("Quit? y/n")
        if r == "n":
            start(x, n_e)
        else:
            print("au revoir")
            quit()
    else:
        print("error")
        essaie(x, n_e)

start(0, 0)