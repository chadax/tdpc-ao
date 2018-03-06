from db_list import *
from db_ressources import *

def find_element(path,val,num):
    """ entre dans un fichier, charge les donnée et trouve une ligne particulière """
    line = []
    data  = loard_data(path)                        # charge les données
    indice= find_indice_element(data,val,num)       # trouve l'indice de l'élément
    if indice != None:                              # on vérifie si l'indice a été trouvé
        line  = data[indice]                        # récupère l'élément et    
    return line                                     # pour finir retourne l'élément


def tdpc_etud(tab_pres):
    """ parcourt un tableau de présence et calcule le tdpc """
    if len(tab_pres)!=0:                        # on vérifie si le tableau contient des présence 
        nbr_a = 0                               #   le nombre d'absences au cours, au départ == à 0
        for p in tab_pres:                      #   on parcourt les différentes présences
            p_a = p[1]                          #   on prend l'information qui dit si l'étudiant est
            if (p_a=='A'):                      #   présent ou absent et s'il est absent
                nbr_a += 1                      #   alors le nombre d'absence augmente de 1
        pour = 100-((nbr_a/len(tab_pres))*100)  #   on calcule le tdp de  l'étudiant au cours on convertie le tdpc 
        tdpc = str(pour)[:4] + '%'              #   en chaine de caractère et on récupère le 4 premier caractère
    else:                                       # sinom
        tdpc = "[R.A.S]"                        #   Rien A Signaler
    return tdpc                                 # et pour finir on retourne le tdpc

# ============= PRESENCES D'UN ETUDIANT A TOUTES LES SEANCES ORGANISEES A UN COURS ====================
def pres_etud_au_cours(acro,mat):
    """ la fonction retourne un tableau de présence d'un étudant à toutes les séances d'un cours"""
    tab_pres_etud = []                                          # prepar le tableau de présence de l'étudiant   
    seances = loard_data(f_seances())                           # charge toutes les séances de tous les cours
    seances_cours = select_lines(seances,acro,0)                # sélection uniniquement celles du cours acro
    
    for sean in seances_cours:                                  # parcourt toutes les séances du cours
        presences = loard_data(f_presence(acro,sean[1],sean[2]))# charge toutes les présences de la séance
        indice = find_indice_element(presences,mat,0)           # recherche et trouve celle de l'étudiant
        if indice!= None:                                       # si la présence de l'étudiant est trouvée
            pres = presences[indice]                            # on la recupère et 
            pres.extend(sean[1:])                               # on n'y ajoute la leçon de la séance
            tab_pres_etud.append(pres)                          # et le tout est ajoute à la liste de présence
                                                                # de l'étudiant, et finalement c'est
    return tab_pres_etud                                        # cette liste qui sera retournée à la fin


# ======= FINALISE L'AFFICHAGE D'UN TDPC OU L'AFFICHAGE DES PRESENCES D'UN ETUDIANT A TOUTES LES SEANCES D'UN COURS ===========
def f_affi_pres_ou_tdp_etud(chaine_formatee,mat,acro,info):
    """ finalise l'affichage des présences ou du tdpc d'un étudiant à toutes les séances d'un cours """
    cr   = find_element(f_cours(),acro,0)       # trouve le cours dont l'acronyme est acro
    etud = find_element(f_etudiant(),mat,0)     # trouve l'étudiant dont le matricule est mat
    intitule, enseig, nom_et, promo = cr[1], cr[3], etud[1], etud[2]# affectation multiple
    print(chaine_formatee % (intitule, enseig, nom_et, mat, promo, info))  # affichage suivant la chaine paramétrée 

# ------- chaine paramétrée en fonction de l'affichage d'un taux de participation au cours
def finaliser_affi_tdpc_etud(tdpc,mat,acro):
    """ finalise l'affichage du tdpc d'un étudiant à un cours """
    # creation de la chaine paramétrée
    chaine_formatee ="""
    Présence au Cours de : %s, dispensé par: %s
    Etudiant: %s   Mat: %s  Prom.: %s TDPC.: %s
    ---------------------------------------------------------
    """ #1er %s représente l'intitulé du cours, l'autre l'enseignant, l'autre l'étudiant, le suivant le matricule, puis la promotion
    f_affi_pres_ou_tdp_etud(chaine_formatee,mat,acro,tdpc) # cette fonction va s'occuper de tout arranger en fournissant une valeur à chaque paramètre

# ------- chaine paramétrée en fonction de l'affichage des présences d'un étudiant à toutes les séances d'un cours
def finaliser_affi_pres_etud(pres_str,mat,acro):
    """ finalise l'affichage des présences d'un étudiant à toutes les séances d'un cours """
    # creation de la chaine paramétrée
    chaine_formatee ="""
    Présence au Cours de : %s, dispensé par: %s
    Etudiant: %s   Mat: %s  Prom.: %s
    ----------------------------------------------------------------
    %s
    """ #1er %s représente l'intitulé du cours, l'autre l'enseignant, l'autre l'étudiant, le suivant le matricule, puis la promotion
    f_affi_pres_ou_tdp_etud(chaine_formatee,mat,acro,pres_str) # cette fonction va s'occuper de tout arranger en fournissant une valeur à chaque paramètre



def b(str,n=30,c=' '):                  # écrit un chaine de caractère sur un nombre n de 
    return str + (c * (n - len(str)))   # caractère ou plus, si la chaine est plus longue
