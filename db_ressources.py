import os

def creer_dossier_pres(acro):       # crée le dossier de présence d'un cours à partir de son acronyme
    """crée le dossier de présence d'un cours à partir de son acronyme"""
    d = "tdpc/presences/%s" % acro  # on crée le chemin vers le dossier
    if not os.path.isdir(d):        # vérifie si le dossier n'existe pas avant de le créer
        os.makedirs(d)              #   et s'il n'existe pas alors on le crée

def f_presence(acro,date,am_pm):    # retourne le chemin complet d'un fichier de présene à un cours
    """se base sur l'acronyme, la date et la période du jour pour construire le chemin vers
    le fichier dans lequel devra être stockées les présences de la séance du cours"""

    s="tdpc/presences/%s/%s_%s.txt" # la chaine paramétré représentant le path vers
    return  s % (acro,date,am_pm)   # le fichier de présences du cours

def f_etudiant():                   # retourne le path du fichier etudiants.txt
    """retourne le chemin vers le fichier contenant les noms des étudiants"""
    return "tdpc/etudiants.txt"     # qui contient les noms de tous les étudiant

def f_cours():                      # retourne le path du fichier cousrs.txt
    """retourne le chemin vers le fichier contenant les noms des cours"""
    return "tdpc/cours.txt"         # qui contient tous les cours

def f_seances():                    # retourne le path du fichier seances.txt
    """retourne le chemin vers le fichier contenant toutes les séances organisées dans tous les cours"""
    return "tdpc/seances.txt"       # qui contient toutes les séances organisées dans tous les cours
