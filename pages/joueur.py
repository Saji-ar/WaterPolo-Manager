from terrain import Terrain

import math

class Joueur:
    def __init__(self, nom, equipe, poste, position, endurance, precision_tir, agressivite):
        self.nom = nom
        self.equipe = equipe
        self.poste = poste  # "gardien", "pointe", "ailier gauche", "ailier droit", "demi gauche", "demi droit", "défenseur pointe"
        self.position = position  # (x, y) sur le terrain
        self.endurance = endurance
        self.precision_tir = precision_tir
        self.agressivite = agressivite
        self.a_le_ballon = False
        self.exclu_pour = 0  # Durée de l’exclusion en ticks


    def se_deplacer_vers(self, cible_x, cible_y, vitesse):
        """Déplacement vers une position cible"""
        if self.position != (cible_x, cible_y):
            dx = cible_x - self.position[0]
            dy = cible_y - self.position[1]

            distance = (dx**2 + dy**2) ** 0.5
            if distance < 3 :
                new_x = cible_x
                new_y = cible_y
            elif distance > 0:
                dx = (dx / distance) * vitesse
                dy = (dy / distance) * vitesse

            new_x = self.position[0] + dx
            new_y = self.position[1] + dy


            if 0<new_x<30 and 0<new_y<20:
                self.position = (new_x, new_y)
                self.endurance -= 1





    def distance_au_joueur(self, autre_joueur):
        """Calcule la distance entre ce joueur et un autre joueur."""
        x1, y1 = self.position
        x2, y2 = autre_joueur.position
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def distance_au_point(self, x, y):
        """Calcule la distance entre ce joueur et un point (x, y)."""
        x1, y1 = self.position
        return math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
    
    def passe(self, emeter, recepteur) : 
        if emeter.a_le_ballon : 
            emeter.a_le_balon = False

        dx, dy = -self.ballon[0] + recepteur.position[0], -self.ballon[1] + recepteur.position[1]
        distance = (dx**2 + dy**2) ** 0.5

        if distance < 4 :
            self.ballon = recepteur.position 
            recepteur.a_le_ballon = True
            return True
        else : 
            dx, dy = dx / distance, dy / distance  # Normalisation
            self.ballon = (self.ballon[0] + dx * 4, self.ballon[1] + dy * 4)  # Mise à jour de la position
            return False
        

    """def tir(self,tireur: Joueur) : 
        dx, dy = self.ballon[0] - tireur.position[0], self.ballon[1] - tireur.position[1]
        distance = (dx**2 + dy**2) ** 0.5
        proba = tireur.precision_tir * (6/distance)
        if (r.randint(0,100) > proba *100)"""
