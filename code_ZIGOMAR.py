#Jonathan et Jessyka
import random

def newDay(objets_dans_sac, new_object):                       # Fonction pour la nouvelle journée
    print("test")

def sac_plein(objet_dans_sac, objet_a_mettre_d_sac):
    random_nb =  random.randint(0, 1)
    if random_nb == 1:
        for i in range (len_liste):
            if objets_dans_sac[i].find("B", "b"):
                objets_dans_sac.pop(i)
        i += 1
    else:
        print(text_inventaire)
        while True:
            objet_enlever = str(input("Bah, toi choisis,j'arrive pas à me décider!"))
            if objet_enlever is str:
                if objet_enlever in objets_dans_sac:
                    print("on enlève ", objet_enlever, " alors!")
                    break
                else:
                    print("C’est pas dans mon sac ça!")
            else:
                print(" ")


def randomSac(objet_dans_sac):                # Randomiser le sac
    random.shuffle(objet_dans_sac)

def randomChoice(objet_dans_sac):             # C'est pour choisir un objet random pour le mini-quiz
    choice_random = random.choice(objet_dans_sac) # Choix random pour Mini-quiz
    choice_zigomar = random.choice(objet_dans_sac)# Choix zigomar pour mini-quiz
    if choice_random != choice_zigomar:
        print("Tu as triché! Je suis sûre que je l'avais!")
    else:
        print("AHa! Je le savais! Mes sens d'aventurière ne me mentent jamais!")

def start_sac(random_items, objets_dans_sac):
    random_items = random.randint(0, 3)
    for i in range (random_items):
        objets_dans_sac.app

def text_inventaire() :                      # Convertion du sac en texte genre 3 potions, instead of ["potion", "potion", "potion"]
    print("test")


#Listes
objets_dans_sac = []                      # C'est les objets qui sont déja dans le sac
objets_a_mettre_d_sac = []                # C'est les objets à mettre dans la sac
ls_inventaire = []                        # C'est le texte de l'inventaire
ls_nb_items = []                          # C'est le nombre d'items de chaque dans l'inventaire

#Variables
new_object = ""                          # C'est les nouveaux objets qu'elle ramasse dans une nouvelle journée
random_items = 0                        # Nombre random d'items à ajouté/présent
random_nb = 0                           # Nombre random
len_liste = len.objets_dans_sac         # Longueur de l'inventaire
len_str_liste = objets_dans_sac [i]


