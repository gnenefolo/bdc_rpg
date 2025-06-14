from tabulate import tabulate

class Personnage:
    def __init__(self, nom, classe, niveau, points_de_vie, force, intelligence, arme=None):
        self.nom = nom
        self.classe = classe
        self.niveau = niveau
        self.points_de_vie = points_de_vie
        self.force = force
        self.intelligence = intelligence
        self.arme = arme
        self.en_vie = True
        
    def afficher_info(self):
        etat = "En vie" if self.en_vie else "Mort"

        table = [
            ["Nom", self.nom],
            ["Classe", self.classe],
            ["Niveau", self.niveau],
            ["Points de vie", self.points_de_vie],
            ["Force", self.force],
            ["Intelligence", self.intelligence],
            ["Arme", self.arme.nom if self.arme else "Aucune arme équipée"],
            ["Dégâts de l'arme", self.arme.degats if self.arme else 0],
            ["État", etat]
        ]

        print(tabulate(table, tablefmt="fancy_grid"))
    
    def attaquer(self, cible):
        if not self.en_vie:
            return f"{self.nom} est mort et ne peut pas attaquer."

        if self.arme:
            degats = self.force * 2 + self.arme.degats
        else:
            degats = self.force * 2

        cible.subir_degats(degats)
        
        if cible.points_de_vie <= 0:
            cible.en_vie = False
            cible.points_de_vie = 0
            return f"{self.nom} attaque {cible.nom} et inflige {degats} points de dégâts. {cible.nom} est mort."
        else:
            return f"{self.nom} attaque {cible.nom} et inflige {degats} points de dégâts. {cible.nom} a maintenant {cible.points_de_vie} points de vie."
        
    def subir_degats(self, degats):
        if not self.en_vie:
            return f"{self.nom} est déjà mort."
        
        self.points_de_vie -= degats
        
        if self.points_de_vie <= 0:
            self.en_vie = False
            self.points_de_vie = 0
            return f"{self.nom} subit {degats} points de dégâts et meurt."
        else:
            return f"{self.nom} subit {degats} points de dégâts et a maintenant {self.points_de_vie} points de vie."