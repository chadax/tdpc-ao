######################################################################################################
# CONTENU DU FICHIER 4 fonctions à savoir:
#
# 1. loard_data(path): 
#                     désérialise le contenu d'un fichier pour reproduire le tableau et le retourne
# 2. find_indice_element(tab,val_cham,num_champ):
#                     retourne l'indice de la première ligne trouvée, telle que sa case d'incide num_champ a
#                     val_cham pour valeur
# 3. select_lines(tab,val_cham,num_champ):
#                     retourne une liste de lignes, telles que leurs case d'incide num_champ ont
#                     val_cham pour valeur
# 4. loard_data_from_excel(path, sep):
#                     retourne un tableau contenant des données chargées à partir d'un fichier excel(.csv)
###########################################################################################################

import os                                       # importation du module os (utili pour manipuler les path)

def loard_data(path):
    """lit un fichier dont le contenu est au format d'un tableau sériablisé
    et désérialise le contenu du fichier pour reproduire le tableau et le retourne
    """
    tab = []                                    # le fameux tableau à retourner
    if os.path.isfile(path):                    # on vérifie si le fichier à ouvrir existe (pour essayer d'ouvir un fichier inexistant)
        fichier = open(path,"r")                # ouverture du fichier en mode lecture seule
        chaine = fichier.read()                 # lecture de tout le contenu du fichier
        fichier.close()                         # fermeture du fichier
        if chaine:                              # on s'assure d'avoir quelque chose dans chaine
            tab = eval(chaine)                  # et on désérialise (un manière de parler)
    
    return tab                                  # et pour finir on retourne le tableau résultant de la désérialisation
    
def find_indice_element(tab,val_cham,num_champ):
    """retourne l'indice de la premier lignes du tableau tab, telles que  
    sa cases d'indice num_champ a pour valeur val_cham, et None si aucune ligne trouvée"""
    if len(tab) and len(tab[0][num_champ:]):    # on s'assure que le tableau n'est pas vide, et que sa premi_re ligne contient la case d'indice num_champ
        for i,lg in enumerate(tab):             # on parcourt toutes les lignes du tableau, en prenant l'indice de la ligne et la ligne
            if lg[num_champ] == val_cham:       # si la case de la ligne à l'indce num_champ a val_chem comme valeur
                return i                        # on retourne l'indice de la ligne et tout s'arrête là
                                                # car mission accomplie
    return None                                 # si rien n'a été trouvé on retourne None

def select_lines(tab,val_cham,num_champ):
    """selectionne toutes les lignes du tableau tab, telles que  
    leurs cases d'indice num_champ ont pour valeur val_cham"""
    new_tab = []                                # on prépare le tableau à retourne, (liste des lignes qui respecteront la condition)
    if len(tab) and len(tab[0][num_champ:]):    # on s'assure que le tableau n'est pas vide, et que sa premi_re ligne contient la case d'indice num_champ
        for lg in tab:                          # on parcourt toutes les lignes du tableau
            if lg[num_champ] == val_cham:       # chaque case d'indice num_champ est comparé à val_cham
                new_tab.append(lg)              # en cas d'égalité, la ligne est ajouter au tableau à retourner
            # end if                            # juste
        # end for                               # pour
    # end if                                    # rire
    return new_tab                              # et à la fin de la sortie de la boucle on retourne le tableau

def loard_data_from_excel(path,sep):
    """charge dans un tableau les données d'un fichier execel au format CSV, au final le tableau a autant des
    lignes et des colonne que dispose le fichier"""
    tab = []
    if os.path.isfile(path):                    # on vérifie si le fichier existe
        fichier = open(path,"r")                #   ouverture du fichier en mode lecture seul
        chaine = fichier.read()                 #   lecture du contenu entier du fichier
        fichier.close()                         #   fermeture du fichier
        chaine = chaine.replace(sep,"','")      #   on remplace les séparateur csv par des ','
        chaine = chaine.replace("\n","'],['")   #   on remplace les passage à la ligne par des '],['
        chaine = "[['%s']]" % chaine            #   on entoure toute la chaine avec des [[ ]]
        if chaine:                              #   on vérifie si notre chaine contient quelque chose
            tab = eval(chaine)                  #   et on désérialise (un manière de parler)
            del tab[-1]                         #   et on supprime le dernier élément qui est un élément supplémentaire et vide
    else:                                       # sinon
        print("Erreur: fichier introuvable!")   #   on afficher un message d'erreur à l'utilisateur
    return tab                                  # et on retourne le tableau (soit vide ou contenant des données)
