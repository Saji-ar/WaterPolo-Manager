from joueur2 import Joueur 
from match2 import Match


# Ajout des joueurs avec leurs postes et côtés respectifs
joueurs_dom = [
    Joueur("Gardien A", "domicile", "gardien", (0, 0), 100, 0, 0),
    Joueur("Ailier Gauche A", "domicile", "ailier gauche", (0, 0), 100, 80, 20),
    Joueur("Ailier Droit A", "domicile", "ailier droit", (0, 0), 100, 80, 20),
    Joueur("Demi Gauche A", "domicile", "demi gauche", (0, 0), 100, 75, 15),
    Joueur("Demi Droit A", "domicile", "demi droit", (0, 0), 100, 75, 15),
    Joueur("Pointe A", "domicile", "pointe", (0, 0), 100, 90, 30),
    Joueur("Défenseur Pointe A", "domicile", "défenseur pointe", (0, 0), 100, 65, 40)
]

joueurs_ext = [
    Joueur("Gardien B", "exterieur", "gardien", (0, 0), 100, 0, 0),
    Joueur("Ailier Gauche B", "exterieur", "ailier gauche", (0, 0), 100, 80, 20),
    Joueur("Ailier Droit B", "exterieur", "ailier droit", (0, 0), 100, 80, 20),
    Joueur("Demi Gauche B", "exterieur", "demi gauche", (0, 0), 100, 75, 15),
    Joueur("Demi Droit B", "exterieur", "demi droit", (0, 0), 100, 75, 15),
    Joueur("Pointe B", "exterieur", "pointe", (0, 0), 100, 90, 30),
    Joueur("Défenseur Pointe B", "exterieur", "défenseur pointe", (0, 0), 100, 65, 40)
]
equipe_A = "Équipe A"
equipe_B = "Équipe B"
match = Match(equipe_A,equipe_B,joueurs_dom,joueurs_ext)
match.lancement_jeu()

