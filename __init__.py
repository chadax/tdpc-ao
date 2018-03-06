import sys                          #
from exec_cmd import *              #


# if __name__ == '__main__':
argv = sys.argv                      # le tableau argv contient des arguments passés à notre programme

args = argv[1:]                      # on retire le nom du fichier du tableau
if(args):                            # on vérifie si le tableau contient au moins quelque chose
    exe_cmd(args)                    # exécution de la commande
else:
    arg_help()                       # affichage de l'aide si aucune option n'est fourni au programme

