from numpy import zeros, array
import matplotlib.pyplot as plt
from typing import Iterable

class Personne:
    x = 0
    y = 0
    flash = None
    couleur = (0, 0, 0)

TabPersonnes = Iterable[Personne]
Couleur = (float, float, float)

def creer_personne(x: float, y: float) -> Personne:
    p : Personne = Personne()
    p.x = x
    p.y = y

    return p

def ajouter_personne(x: float, y: float, tab: TabPersonnes, n: int) -> int:
    tab[n] = creer_personne(x, y)
    return n + 1

def flasher_personnes(tab: TabPersonnes, n: int):
    for i in range(n):
        #Si on considère la dernière personne du tableau
        if i == (n - 1):
            tab[i].flash = tab[0]
        else:
            tab[i].flash = tab[i + 1]

def dessiner_regards(tab: TabPersonnes, n: int):
    for i in range(n):
        p = tab[i]
        flash = p.flash
        #Traçage de la ligne
        plt.plot([p.x, flash.x], [p.y, flash.y])

def dessiner_regards_colores(tab: TabPersonnes, n: int):
    for i in range(n):
        p = tab[i]
        flash = p.flash
        #Traçage de la ligne
        plt.plot([p.x, flash.x], [p.y, flash.y], color=p.couleur)

def avancer_personne(tab: TabPersonnes, n: int):
    for i in range(n):
        p = tab[i]
        flash = p.flash

        p.x += 0.05 * (flash.x - p.x)
        p.y += 0.05 * (flash.y - p.y)

def rosace():
    tab: TabPersonnes = zeros(10, Personne)

    #Ajout des personnes au tableau
    n = 0
    n = ajouter_personne(0, 0, tab, n) #0
    n = ajouter_personne(10, 0, tab, n) #1
    n = ajouter_personne(10, 10, tab, n) #2
    n = ajouter_personne(0, 10, tab, n) #3

    flasher_personnes(tab, n)

    for i in range(100):
        dessiner_regards(tab, n)
        avancer_personne(tab, n)
    
    plt.show()

def rosace_coloree():
    tab: TabPersonnes = zeros(10, Personne)

    #Ajout des personnes au tableau
    n = 0
    n = ajouter_personne(0, 0, tab, n) #0

    n = ajouter_personne(10, 0, tab, n) #1
    n = ajouter_personne(10, 10, tab, n) #2
    n = ajouter_personne(0, 10, tab, n) #3

    flasher_personnes(tab, n)

    for i in range(100):
        dessiner_regards(tab, n)
        avancer_personne(tab, n)
    
    plt.show()


rosace()