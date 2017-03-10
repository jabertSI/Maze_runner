###
### Auteurs : Val, Samir et Jabo
### License : Osef
###
from random import randint
from time import time
game = True
from math import *
import  os

labyrinth_un = [
    '#############',
    '#.....B#....#',
    '###.O####.###',
    '#B##...##..##',
    '#.##....T.#B#',
    '#.#######.#.#',
    '#....B.##.#.#',
    '###.##......#',
    '##B##...#.###',
    '#T....#.....#',
    '#############',
]
#labyrinth du mode DIEU
labyrinth_o = [
    '#############',
    '#.....B.....#',
    '#...........#',
    '#B..........#',
    '#.......T..B#',
    '#...........#',
    '#....B......#',
    '#...........#',
    '#.B.........#',
    '#T..........#',
    '#############',
]
labyrinth = labyrinth_un


#calcul du modul pour les distance
def modul_pos(a_position):
    return sqrt(a_position[0]**2 + a_position[1]**2)
#calcul d'angle entre notre position et celle du tresore en utilisant la fonction modul
def calcul_angle(current_user_position, treasure_position):
    return degrees(atan(modul_pos(current_user_position)/modul_pos(treasure_position)))

#Commande '?' affiche le labyrinth sans les B et le T
def circuit():
    cpt_x = 0
    cpt_y = 0

    for i in labyrinth_un:
        cpt_x = 0
        for j in i:
            if current_user_position[0] == cpt_x and current_user_position[1] == cpt_y :
                print('X', end="")
            elif j == 'B' or j == 'T':
                print('.', end="")
            else :
                print(j, end="")
            cpt_x += 1
        cpt_y += 1
        print()

# On défini une fonction q


#ça sert à test si deux positions ont les meme coordonnées avec current pos un tableau d'entier de 2 elements
# et past_pos un tableau contenant un tableau d'entier de 2 élements ainsi qu'un petit compteur de ma confection
#le retour de la fonction va enregistrer les coordonnées de la position dans letableau des past_positions
def compare_position(current_user_position, past_positions):
    cpt_tourne_en_rond = 0
    for pos in past_positions:
        if current_user_position[0] == pos[0] and pos[1] == current_user_position[1] :
            cpt_tourne_en_rond += 1
    if cpt_tourne_en_rond == 0:
        print()
    elif cpt_tourne_en_rond == 1:
        print("vous êtes déjà passé par ici")
    elif cpt_tourne_en_rond == 2:
        print("Ce n'est pas la premiere fois que vous passez par ici, attention de ne pas tourner en rond")
    elif cpt_tourne_en_rond == 3:
        print(" Tu reviens sur tes pas")
    elif cpt_tourne_en_rond == 4:
        print("attention tu as deja visité cette case")
    elif cpt_tourne_en_rond == 5:
        print("tu te trompe de route, pense au petit poucet !")
    elif cpt_tourne_en_rond == 6:
        print("Ta le sens d'orientation d'un poisson rouge dans ton bocal sans vouloir te vexe.")
    else:
        print("Cesse d'y mettre de la mauvaise volontee veux tu!")

    past_positions.append(list(current_user_position))







#(circuit()) Code triche pour afficher le circuit avec l'emplacement des B et T
def cheat():
    cheat_code = 'abracadabra'
    code_user = str(input("Entrer le cheat code"))
    if code_user == cheat_code:
        for i in labyrinth:
            print(i)
    else:
        print('Ce code n'"'"'existe pas')

def code_coffre():
    code_coffre = randint(1,9)
    code_user = 0
    while code_user != code_coffre:
        try:
            code_user = int(input("Entrer un nombre pour ouvrir le coffre"))
        except:
            print('pas un chiffre')
            continue

        if code_user == code_coffre:
            print("Bravo vous avez trouvé la combinaison du coffre")
            print("""
                                         _.--.
                                    _.-'_:-'||
                                _.-'_.-::::'||  \033[1;32m!!!!!! GG WP !!!!!!\033[1;m
                           _.-:'_.-::::::'  ||  \033[1;32m!!!!!! GG WP !!!!!!\033[1;m
                         .'`-.-:::::::'     ||  \033[1;32m!!!!!! GG WP !!!!!!\033[1;m
                        /.'`;|:::::::'      ||_ \033[1;32m!!!!!! GG WP !!!!!!\033[1;m
                       ||   ||::::::'     _.;._'-._
                       ||   ||:::::'  _.-!oo @.!-._'-.
                       \/'.  ||:::::.-!()oo @!()@.-'_.|
                        '.'-;|:.-'.&$@.& ()$%-'o.' U||
                          `>'-.!@%()@'@_%-'_.-o _.|'||
                           ||-._'-.@.-'_.-' _.-o  |'||
                           ||=[ '-._.-\ /.-'    o |'||
                           || '-.]=|| |'| GG wp   |'||
                           ||      || |'|        _| ';
                           ||      || |'|    _.-'_.-'
                           |'-._   || |'|_.-'_.-'
                            '-._'-.|| |' `_.-'
                                '-.||_/.-'
            """)
        elif code_user < code_coffre:
            print("Plus")
        elif code_user > code_coffre:
            print("Moins")
        else:
            print('commande non valide')





if __name__ == "__main__":


    print('Bienvenue au Super Labyrinthe v1.04, un jeu tout perrave qui sent le pathé !')
    #print('Nom du joueur ?')
    nomjoueur = (input())
    print('Bienvenue', nomjoueur)
    mirror_mode = False
    god_mode = False
    print("""Liste des commandes :
    Pour aller à  \033[0;34mgauche\033[0;m : L
    Pour aller à  \033[0;34mdroite\033[0;m : R
    Pour  \033[0;34mmonter\033[0;m : U
    Pour  \033[0;34mdescendre\033[0;m : D
    Pour  \033[0;34mafficher votre position\033[0;m : ?
    Pour  \033[0;34mouvrir la commande des cheat codes\033[0;m : C""")

    # Dans la variable qui définit la position de l'user dans le labyrinthe, le premier élement est X et le second est Y.
    # La position initiale est toujours [1,1]
    current_user_position = [1,1]
    next_position = [1,1]

    cptmove = 0
    treasure_position = [1,9]
    past_positions = []
    # Calcul de la largeur et hauteur
    W = len(labyrinth[0])
    H = len(labyrinth)

    time_start = time()

    while game == True:
        #Mode dieu lorsque le joeur tombe sur la case 'o' il peut traversé les mur !
        if god_mode :
            labyrinth = labyrinth_o

        #avant que l'utilisateur ne boue on cherche a savoir s'il a deja ete sur la case apparavant.
        compare_position(current_user_position, past_positions)

        # Avant que l'utilisateur ne bouge, la position suivante est la position actuelle de l'utilisateur.
        next_position[0] = current_user_position[0]
        next_position[1] = current_user_position[1]


        #Cbalcul distance entre le joueur et le trésor
        distance = sqrt((current_user_position[0] - treasure_position[0])**2 +(current_user_position[1]- treasure_position[1])**2)
        # Demander le mouvement de l'utilisateur, le convertir en majuscules.
        move = input("Où veux-tu aller ?").upper()

        # Selon l'input de l'utilisateur, calculer la prochaine position
        # Les coordonnées sont prises avec origine le coin haut gauche, et ne sont que des valeurs positives
        if move == 'L':
            if mirror_mode:
                print('Tu te déplace en \033[1;34mdroite\033[1;m.')
                next_position[0] += 1
            else:
                print('Tu te déplace en \033[1;34mgauche\033[1;m.')
                next_position[0] -= 1
            cptmove += 1
            print('Tu es à', ceil(distance), 'cases du trésor.')
            print('l angle entre toi et le trésore est ', calcul_angle(current_user_position, treasure_position), 'degres')
        elif move == 'R':
            if mirror_mode:
                print('Tu te déplace en \033[1;34mgauche\033[1;m.')
                next_position[0] -= 1
            else:
                print('Tu te déplace en \033[1;34mdroite\033[1;m.')
                next_position[0] += 1
            cptmove += 1
            print('Tu es à', ceil(distance), 'cases du trésor.')
            print('l angle entre toi et le trésore est ', calcul_angle(current_user_position, treasure_position), 'degres')
        elif move == 'U':
            if mirror_mode:
                print('Tu te déplace en \033[1;34mbas\033[1;m.')
                next_position[1] += 1
            else:
                print('Tu te déplace en \033[1;34mhaut\033[1;m.')
                next_position[1] -= 1
            cptmove += 1
            print('Tu es à', ceil(distance), 'cases du trésor.')
            print('l angle entre toi et le trésore est ', calcul_angle(current_user_position, treasure_position), 'degres')
        elif move == 'D':
            if mirror_mode:
                print('Tu te déplace en \033[1;34mhaut\033[1;m.')
                next_position[1] -= 1
            else:
                print('Tu te déplace en \033[1;34mbas\033[1;m.')
                next_position[1] += 1
            cptmove += 1
            print('Tu es à', ceil(distance), 'cases du trésor.')
            print('l angle entre toi et le trésore est ', calcul_angle(current_user_position, treasure_position), 'degres')
        elif move == '?':
            circuit()
            continue
        elif move == 'C':
            cheat()
            continue
        #elif move == 'RESET':
            #next_position = [1,1]  #Jabo, ne pas touché

        else:
            print('Commande non valide, rééssaye.')
            continue


        # Vérifier si on sort du labyrinthe
        if next_position[0] >= W or next_position[0] < 0 \
                or next_position[1] < 0 or next_position[1] >= H:
            print('Tu es sorti du labyrinthe. Essaye encore !')
            continue

        # Procéder différenment selon le contenu de la prochaine position.
        if labyrinth[next_position[1]][next_position[0]] == 'T':
            print('Tu as fais', cptmove,'mouvements pour y arriver')
            print("""

     .--------.
    / .------. \\
   / /        \ \\
   | |        | | \033[1;32m!!!!! BRAVO !!!!!\033[1;m
  _| |________| |_\033[1;32mTu as trouvé le trésor !\033[1;m
.' |_|        |_| '. \033[5;31mMaintenant il faut déverouiller le coffre ! :)\033[5;m'
'._____ ____ _____.'
|     .'____'.     |
'.__.'.'    '.'.__.'
'.__  | LOCK |  __.'
|   '.'.____.'.'   |
'.____'.____.'____.'
'.________________.'""")
            code_coffre()
            print("resolu en",round(time() - time_start,3), 'sec', 'et',cptmove,'mouvements')
            input("Appuyer sur entrer pour quitter")

            break
        elif labyrinth[next_position[1]][next_position[0]] == '.':
            print('Le trésor n est pas ici, continues !')
            current_user_position[0] = next_position[0]
            current_user_position[1] = next_position[1]
        elif labyrinth[next_position[1]][next_position[0]] == '#':
            print('Tu viens de manger un mur...')
        elif labyrinth[next_position[1]][next_position[0]] == 'M': #MODE MIRROR
            print('Tu viens de tomber sur un piege...')
            current_user_position[0] = next_position[0]
            current_user_position[1] = next_position[1]
            mirror_mode = True

        elif labyrinth[next_position[1]][next_position[0]] == 'O': #MODE DIEU
            print('\033[5;31mMODE DIEU\033[5;m')
            god_mode = True
            current_user_position[0] = next_position[0]
            current_user_position[1] = next_position[1]

        elif labyrinth[next_position[1]][next_position[0]] == 'B' :
            print('\033[5;31mBOoooOOOOOoom ! Tu as marché sur une bombe, Game Over !\033[5;m')
            print("""  _____
 /     \\
| () () |
 \\  ^  /   Daaaaammmmnnnn
  |||||
  |||||""")
            print("TEMP DE JEU :",round(time() - time_start,3), 'sec')
            restart = str(input("Vouslez vous recommencer ? (oui/non)"))
            if restart == "oui" :
                print('Nouvelle partie !')
                current_user_position = [1,1]
                cptmove = 0
            elif restart == "non":
                game = False
            else:
                print('Commande non gérée')
                restart = str(input("Vouslez vous recommencer ? (oui/non)"))


        else:
            print('On dirait qu il y a un problème avec le labyrinthe...')
            break
os.system("pause")