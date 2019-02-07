from numpy import zeros, array
import matplotlib.pyplot as plt
from typing import Iterable
from personne import Personne

TabPersonnes = Iterable[Personne]
Couleur = (float, float, float)


def ajouter_personne(x: float, y: float, tab: TabPersonnes, n: int) -> int:
    tab[n] = Personne(x, y)
    return n + 1


def flasher_personnes(tab: TabPersonnes, n: int):
    for i in range(n):
        p = tab[i]

        # Si on considère la dernière personne du tableau
        if i == (n - 1):
            p.flash_with(tab[0])
        else:
            p.flash_with(tab[i + 1])


def dessiner_regards(tab: TabPersonnes, n: int):
    for p in tab:
        flash = p.get_flash()
        # Traçage de la ligne
        plt.plot([p.get_x(), flash.get_x()], [p.get_y(), flash.get_y()])


def dessiner_regards_colores(tab: TabPersonnes, n: int):
    for p in tab:
        flash = p.get_flash()

        # Traçage de la ligne
        plt.plot([p.get_x(), flash.get_x()], [
                 p.get_y(), flash.get_y()], color=p.get_couleur())


def avancer_personnes(tab: TabPersonnes):
    for p in tab:
        flash = p.get_flash()
        p.set_x(p.get_x() + (0.05 * (flash.get_x() - p.get_x())))
        p.set_y(p.get_y() + (0.05 * (flash.get_y() - p.get_y())))


def rosace():
    tab: TabPersonnes = zeros(4, Personne)

    # Ajout des personnes au tableau
    n = 0
    n = ajouter_personne(0, 0, tab, n)  # 0
    n = ajouter_personne(10, 0, tab, n)  # 1
    n = ajouter_personne(10, 10, tab, n)  # 2
    n = ajouter_personne(0, 10, tab, n)  # 3

    flasher_personnes(tab, n)

    for i in range(100):
        dessiner_regards(tab, n)
        avancer_personnes(tab)

    plt.show()


rosace()
