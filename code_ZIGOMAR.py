#Jonathan et Jessyka (oui j'ai utilisée l'accompte a mon copain)

import random
from os import remove


def newDay(objets_dans_sac):                       # Fonction pour la nouvelle journée
    random_nb =  random.randrange(1, 3)
    for i in range (random_nb):
        random_items = random.randint(1, 3)
        for i in range (random_items):
            objets_dans_sac.append("potions scintillantes")
        random_items = random.randint(1, 3)
        for i in range (random_items):
            objets_dans_sac.append("clés mystérieuses")
        random_items = random.randint(1, 3)
        for i in range (random_items):
            objets_dans_sac.append("boules brillantes")
        random_items = random.randint(1, 3)
        for i in range (random_items):
            objets_dans_sac.append("squelettes miniatures")
    text_inventaire(objets_dans_sac)
    print("debut de la nouvelle journée: \n", ls_inventaire)
    print("allons a l'aventure!")


def sac_plein(objets_dans_sac):
    print("Mon sac est plein!")
    random_nb =  random.randint(0, 1)
    if random_nb == 1 and :
        for i in range (len(objets_dans_sac)):
            text_inventaire(objets_dans_sac)
            print(ls_inventaire)
            if objets_dans_sac[i].find("boules brillantes"):
                objets_dans_sac.pop(i)
                print("on enlève cet objet abjecte!")

    else:
        while True:
            text_inventaire(objets_dans_sac)
            print(ls_inventaire)
            objet_enlever = str(input("Bah, toi choisis,j'arrive pas à me décider!"))
            try:
                objet_enlever is str
                if objet_enlever in objets_dans_sac:
                    objets_dans_sac.remove(objet_enlever)
                    print("on enlève ", objet_enlever, " alors!")
                    break
                else:
                    print("C’est pas dans mon sac ça!")
            except:
                print(" ")


def randomSac(objet_dans_sac):                # Randomiser le sac
    random.shuffle(objet_dans_sac)

def randomChoice(objet_dans_sac):                       # C'est pour choisir un objet random pour le mini-quiz
    choice_random = random.choice(objet_dans_sac)       # Choix random pour Mini-quiz
    choice_zigomar = random.choice(objet_dans_sac)      # Choix zigomar pour mini-quiz
    if choice_random != choice_zigomar:
        print("Tu as triché! Je suis sûre que je l'avais!")
    else:
        print("AHa! Je le savais! Mes sens d'aventurière ne me mentent jamais!")

def start_sac(objets_dans_sac, ls_inventaire):
    random_items = random.randint(0, 3)
    for i in range (random_items):
        objets_dans_sac.append("potions scintillantes")
    ls_inventaire.append(f"{random_items} potions scintillante")
    random_items = random.randint(0, 3)
    for i in range (random_items):
        objets_dans_sac.append("clés mystérieuses")
    ls_inventaire.append(f"{random_items} clés mystérieuses")
    random_items = random.randint(0, 3)
    for i in range (random_items):
        objets_dans_sac.append("boules brillantes")
    ls_inventaire.append(f"{random_items} boules brillantes")
    random_items = random.randint(0, 3)
    for i in range (random_items):
        objets_dans_sac.append("squelettes miniatures")
    ls_inventaire.append(f"{random_items} squelettes miniatures")

def text_inventaire(objets_dans_sac) :                       # Convertion du sac en texte genre 3 potions, instead of ["potion", "potion", "potion"]
    ls_inventaire = []

    inventaire_en_texte = objets_dans_sac.count("potions scintillantes")
    ls_inventaire.append(f"{inventaire_en_texte} potions scintillante")

    inventaire_en_texte = objets_dans_sac.count("clés mystérieuses")
    ls_inventaire.append(f"{inventaire_en_texte} clés mystérieuses")

    inventaire_en_texte = objets_dans_sac.count("boules brillantes")
    ls_inventaire.append(f"{inventaire_en_texte} boules brillantes")

    inventaire_en_texte = objets_dans_sac.count("squelettes miniatures")
    ls_inventaire.append(f"{inventaire_en_texte} squelettes miniatures")

def sort_end_day(objets_dans_sac):
    print("ALORS! avant de finir cette splendide journée d'aventure, FAUT TRIER MON SAC!")
    sorted(objets_dans_sac)
    text_inventaire(objets_dans_sac)
    print(ls_inventaire)



#Listes
objets_dans_sac = []                      # C'est les objets qui sont déja dans le sac
objets_a_mettre_d_sac = []                # C'est les objets à mettre dans la sac
ls_inventaire = []                        # C'est le texte de l'inventaire
ls_nb_items = []                          # C'est le nombre d'items de chaque dans l'inventaire

#Variables
new_object = ""                          # C'est les nouveaux objets qu'elle ramasse dans une nouvelle journée
random_items = 0                         # Nombre random d'items à ajouté/présent
random_nb = 0                            # Nombre random

if __name__ == '__main__':
    start_sac(objets_dans_sac, ls_inventaire)
    for i in range(1):
        newDay(objets_dans_sac)
        while len(objets_dans_sac) > 15:
            if len(objets_dans_sac) > 15:
                sac_plein(objets_dans_sac)
            else:
                break
        text_inventaire(objets_dans_sac)
        sort_end_day(objets_dans_sac)
        randomSac(objets_dans_sac)
        randomChoice(objets_dans_sac)





'''  

TODO:faire un desing. embellisement, affichage des liste est du texte.


'''


