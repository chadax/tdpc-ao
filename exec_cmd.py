from affichage import *                # importer le fichier contenant les fonctions d'affichage
from import_data import *              # importer le fichier contenant les fonctions d'importation des données


def exe_cmd(arg_valeurs):
    if(arg_valeurs):
        arg     = arg_valeurs[0]        # extraction de l'argument
        valeurs = arg_valeurs[1:]       # extraction des valeurs

        if arg == '-ip':                # ou encore importer les présences depuis un fichier excel.csv
            import_presence(valeurs)     
        elif arg == '-ie':              # ou encore importer les étudiants depuis un fichier excel.csv
            import_etudiant(valeurs)     
        elif arg == '-ic':              # ou encore importer les cours depuis un fichier excel.csv
            import_cours(valeurs)     
        elif arg == '-gp':              # ou encore générer les présences aléatoirement
            generer_presence_al(valeurs)
        # -------------------------------------------------------------------------------------
        elif arg == '-pe':              # ou encore les présences d'un étudiant
            afficher_pres_etud_au_cours(valeurs)
        elif arg == '-te':              # ou encore le taux de participation d'un étudiant
            afficher_tdp_etud_au_cours(valeurs)
        elif arg == '-te*':             # ou encore le taux de participation de tous les étudiant dans un cours
            afficher_tdp_etud_all_cours(valeurs)       
        elif arg == '-t**':             # ou encore le taux de participation de tous les étudiant dans un cours
            afficher_tdp_all_stud_au_cours(valeurs)       
        elif arg == '-h':               # ou encore afficher de l'aide
            arg_help()     
        else:                           # si aucun argument ne correspond
            print("Erreur: Option inconnue!")
    else:
        arg_help()

# ==================================================
def arg_help():   
    msg = """
    -ie : importe des étudiants et le tableau de valeur est supposé contenir
            path      : le chemin vers le fichier excel.csv
            separateur: le séparateur [','|';'] utilisé dans le fichier excel.csv

    -ic : importe des cours et le tableau de valeur est supposé contenir
            path      : le chemin vers le fichier excel.csv
            separateur: le séparateur [','|';'] utilisé dans le fichier excel.csv
            
    -ip : imorte des présences et  le tableau de valeur est supposé contenir
            acro_cour : l'acronyme du cours
            date_sean : la date de la séance
            path      : le chemin vers le fichier excel.csv
            separateur: le séparateur [','|';'] utilisé dans le fichier excel.csv
            am_pm     : la séance était avant(AM) ou après-midi(PM)     

    -gp : génère des présence de manière aléatoire le tableau de valeur est supposé contenir
            acro_cour : l'acronyme du cours
            date_sean : la date de la séance (ou les dates)
            am_pm     : la séance était avant(AM) ou après-midi(PM)
    -----------------------------------------------------------------------------------

    -pe : afficher les présences d'un étudiant à toutes les séances d'un cours
            et le tableau de valeur est supposé contenir
            acro     : l'acronyme du cours concerné
            mat      : le matricule de l'étudiant

    -te : afficher le taux de participation d'un étudiant à un cours
            et le tableau de valeur est supposé contenir
            acro     : l'acronyme du cours concerné
            mat      : le matricule de l'étudiant

    -te* : afficher le taux de participation d'un étudiant à tous ses cours
            et le tableau de valeur est supposé contenir
            mat      : le matricule de l'étudiant concerné

    -t** : afficher le taux de participation de tous les étudiant à un cours
            et le tableau de valeur est supposé contenir
            acro     : l'acronyme du cours concerné
    """
    print(msg)
