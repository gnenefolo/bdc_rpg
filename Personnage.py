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
        info = f"Nom: {self.nom}\n"
        info += f"Classe: {self.classe}\n"
        info += f"Niveau: {self.niveau}\n"
        info += f"Points de vie: {self.points_de_vie}\n"
        info += f"Force: {self.force}\n"
        info += f"Intelligence: {self.intelligence}\n"
        if self.arme:
            info += f"Arme: {self.arme}\n"
        else:
            info += "Pas d'arme équipée.\n"
        return info
    
    def attaquer(self, cible):
        if not self.en_vie:
            return f"{self.nom} est mort et ne peut pas attaquer."
        
        degats = self.force
        cible.points_de_vie -= degats
        
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