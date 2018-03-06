
# 1. rewrite_the_file(tab,path):
#     sérialise le tableau tab et enregistre la chaine en résultant dans le fichier dont le chemin est path

def rewrite_the_file(tab,path):
    """sérialise le tableau tab et l'écrit dans le fichier dont le chemin est indiqué en paramètre"""
    chaine = str(tab).replace('], [',"],\n [")      # sérialisation du tableau et ajout de passage à la ligne à la fin de chaque ligne
    fichier= open(path,"w")                         # ouverture du fichier en écriture (ce qui a pour effet d'écraser tous son contenu)
    fichier.write(chaine)                           # écriture de chaine (tableau sérialisé) dans le fichier
    fichier.close()                                 # fermeture du fichier




# def ajouter_ligne_au_fichier(new_ligne,fichier):
#     lignes = loard_data(fichier)
#     lignes.append(new_ligne)       
#     rewrite_the_file(lignes,fichier)