"""
Pour m'entrainer à la POO, j'ai décidé de mettre la classe Personne dans un fichier séparé
"""


class Personne:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__flash = None
        self.__couleur = (0, 0, 0)

    # Définir les coordonnées en x de la personne
    def set_x(self, x: float):
        self.__x = x

    # Définir les coordonnées en y de la personne
    def set_y(self, y: float):
        self.__y = y

    # Définir la couleur de la personne
    def set_couleur(self, couleur: (float, float, float)):
        self.__couleur = couleur

    # Récupérer les coordonnées en x de la personne
    def get_x(self):
        return self.__x

    # Récupérer les coordonnées en y de la personne
    def get_y(self):
        return self.__y

    # Récupérer le flash associé à la personne
    def get_flash(self):
        return self.__flash

    # Récupérer la couleur associée à la personne
    def get_couleur(self):
        return self.__couleur

    # Flasher la personne avec une autre
    def flash_with(self, p):
        self.__flash = p
