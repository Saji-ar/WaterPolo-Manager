ticks = 20                   # frame par seconde
vitesse_du_jeu = 2          # vitesse du jeu
temps_par_phase = 30        #temps de chaque phase par équipe en seconde
longueur_terrain = 30
largeur_terrain = 20
taille_but = 3
fact_alea_pos = 0.5           #le facteur aléatoire autoure d'une position

#Position a l'engagement

base_x_ext = 0.5 # Ligne de but domicile
base_x_dom = longueur_terrain - 0.5 # Ligne de but extérieur


positions_dom = {
    "gardien": (base_x_dom, largeur_terrain // 2),
    "ailier gauche": (base_x_dom, 18),
    "ailier droit": (base_x_dom, 1),
    "pointe": (base_x_dom, 12),
    "demi gauche": (base_x_dom, 16),
    "demi droit": (base_x_dom, 5),
    "défenseur pointe": (base_x_dom, 8)
}

# Positionnement des joueurs extérieur
positions_ext = {
    "gardien": (base_x_ext, largeur_terrain // 2),
    "ailier gauche": (base_x_ext, 1),
    "ailier droit": (base_x_ext, 18),
    "pointe": (base_x_ext,12),
    "demi gauche": (base_x_ext,5),
    "demi droit": (base_x_ext, 16),
    "défenseur pointe": (base_x_ext, 8)
}


#stat des joueurs 

Vitesse_max = 2                     # en m/s
acceleration = 2                    # en m/s^2