from db_add import *            #
from db_list import *           #
from db_ressources import *     #

def importer(src,sep,dest):
    """se contente de charger les données excel dans un tableau et enregistrer le tableau dans un fichier"""
    data = loard_data_from_excel(src,sep)   # importation des données depuis un fichier execel
    rewrite_the_file(data,dest)             # enregistrement des données importées dans un fichier cible
    return data                             # retourne les donnée importée et enregistrées pour d'autre manips

# =============== IMPORTATION DES DONNEES ======================
# ----------------------------------------------------------
def import_presence(valeurs):
    """ Impporte les présences des étudiants enregistrée en excel.csv """
    if len(valeurs) == 5:                                               # vérification du nombre de paramètres
        acro, date, path, separateur, am_pm = valeurs                   # affectation multiple
        importer(path,separateur, f_presence (acro,date,am_pm) )        # importation et enregistre les données
    else:
        help_import('import_pres',valeurs)
# ----------------------------------------------------------
def import_etudiant(valeurs):
    """ Impporte les étudiants enregistrés en excel.csv"""
    if len(valeurs) == 2:                                               # vérification du nombre de paramètres
        path, separateur = valeurs                                      # affectation multiple
        importer(path,separateur, f_etudiant () )                       # importation et enregistre les données
    else:
        help_import('import_',valeurs)
# ----------------------------------------------------------
def import_cours(valeurs):
    """ Impporte les cours enregistrés en excel.csv"""
    if len(valeurs) == 2:                                               # vérification du nombre de paramètres
        path, separateur = valeurs                                      # affectation multiple
        cours = importer(path,separateur, f_etudiant () )               # importation et enregistre les données

        for c in cours:                                                 # parcourt tous les cours
            creer_dossier_pres(c[0])                                    # et crée un dossier de présence pour chaque cours importé
    else:
        help_import('import_',valeurs)


# ================ GENERATION DONNEE ALEATOIRES ====================
def generer_presence_al(valeurs):
    """ Génère de manière aléatoire les présences des étudiants à des séances d'un cours"""
    import random                                   # importation locale d'un module
    if len(valeurs)==3:
        acro, date, am_pm = valeurs                 # affectation multiple        
        etudians = loard_data(f_etudiant())         # chargement de la liste de tous les étudiants
        seances  = loard_data(f_seances())          # chargement de la liste de toutes les séances

        tab_dt   = date.split(',')                  # découpage des dates
        for dt in tab_dt:                           # parcourt de toutes les dates et pour chacune d'elle
            sean = [acro,dt,am_pm,'Pas de résumé!'] # on crée une séance
            seances.append(sean)                    # que l'on ajoute à la liste de toutes les séances
            pres = []                               # on se prepare la liste de présence à la séance
            p_a = ['A','P']                         # deux possiblités pour chaque présence à faire
            for e in etudians:                      # on parcourt la liste des étudiants
                mat = e[0]                          # matricule de l'étudiant
                pa = p_a[random.randrange(2)]       # on décide aléatoirement s'il est présent ou absent 
                p = [mat ,pa ,'R.A.S']              # on crée la présence associé à l'étudiant
                pres.append(p)                      # on ajoute la présence de l'étudiant à la liste de présence
                                                    # à la fin, on pense aussi à sauvegarder la liste de
            rewrite_the_file(pres,f_presence(acro,dt,am_pm)) # présence dans un fichier approprié
                                                    # à la fin de tout, il faud penser à mettre à jour le
        rewrite_the_file(seances,"tdp/seances.txt") # le fichier contenant toutes les séances                   
    else:
        help_import('pres_al',valeurs)


# ================= HELP FUNCTION ==================
def help_import(cmd,tab=[]):
    msg = ""
    if cmd == "import_pres":
        msg = """
        acro_cour : l'acronyme du cours
        date_sean : la date de la séance
        path      : le chemin vers le fichier excel.csv
        separateur: le séparateur [','|';'] utilisé dans le fichier excel.csv   (Optionnel: ',' par défaut)
        am_pm     : la séance était avant(AM) ou après-midi(PM)                 (Optionnel: 'AM': par défaut)
        """
    elif cmd == "import_":
        msg = """
        path      : le chemin vers le fichier excel.csv
        separateur: le séparateur [','|';'] utilisé dans le fichier excel.csv   (Optionnel: ',' par défaut)
        """
    elif cmd == "pres_al":
        msg = """
        acro_cour : l'acronyme du cours
        date_sean : la date de la séance
        am_pm     : la séance était avant(AM) ou après-midi(PM)                 (Optionnel: 'AM': par défaut)
        """

    
    msg = """
    --------------- (Import help) --------------------
    Le tableau des valeurs %s est supposé contenir %s""" % (str(tab),msg)
    print(msg)

