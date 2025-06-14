from Personnage import Personnage

def main():
    # Création de deux personnages
    personnage1 = Personnage(nom="Guerrier", classe="Guerrier", niveau=1, points_de_vie=100, force=20, intelligence=5)
    personnage2 = Personnage(nom="Mage", classe="Mage", niveau=1, points_de_vie=80, force=5, intelligence=20)

    # Affichage des informations des personnages
    print(personnage1.afficher_info())
    print(personnage2.afficher_info())

    # Attaque du personnage 1 sur le personnage 2
    print(personnage1.attaquer(personnage2))

    # Attaque du personnage 2 sur le personnage 1
    print(personnage2.attaquer(personnage1))
    
if __name__ == "__main__":
    main()