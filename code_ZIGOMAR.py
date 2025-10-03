#Jonathan et Jessyka (oui j'ai utilisée l'accompte a mon copain)

import random
from os import remove


def newDay(objets_dans_sac):
    random_nb =  random.randrange(1, 3)                          # Début de la nouvelle journée : randomisation des items de départ.
    for i in range (random_nb):
        random_items = random.randint(1, 3)                          #ici on a coder chaques variable a random pour chaques items.
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
    ls_inventaire = text_inventaire(objets_dans_sac)
    print("debut de la nouvelle journée:")
    print("allons a l'aventure! \n", ls_inventaire)


def sac_plein(objets_dans_sac):
    print("Mon sac est plein!")                                         #fonction pour que zigomar nous fasses signe quands son sac est plein et les choix qu'elle fait (random entre vrais et faux).
    random_nb =  random.randint(0, 1)                              #partie codée pour qu'elle retire automatiquement l'item avec un 'b' dedans.
    if random_nb == 1 and 'boules brillantes' in objets_dans_sac:
        for i in range (len(objets_dans_sac)):  # LA TAILLE EST VÉRIFIÉE SEULEMENT AU DÉBUT
            ls_inventaire = text_inventaire(objets_dans_sac)
            print(ls_inventaire)
            try:
                if objets_dans_sac[i].find("boules brillantes"): # CETTE LIGNE CAUSE UNE EXCEPTION
                    objets_dans_sac.pop(i) # COMME ON RETIR DES OBJETS DANS LA BOUCLE, LA LISTE RAPETISSE
                    print("on enlève cet objet abjecte!")
            except:
                print("fin de la liste")

    else:
        while True:
            ls_inventaire = text_inventaire(objets_dans_sac)        #Partie codée pour qu'elle nous demande de faire un choix pour elle jusqu'à-ce que le sac soit en dessous de 15 items.
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

def randomChoice(objet_dans_sac):                       # C'est pour choisir un objet random pour le Mini-jeu de devinettes
    choice_random = random.choice(objet_dans_sac)       # Notre choix random pour Mini-jeu de devinettes
    choice_zigomar = random.choice(objet_dans_sac)      # Choix de Zigomar pour Mini-jeu de devinettes
    if choice_random != choice_zigomar:
        print("Tu as triché! Je suis sûre que je l'avais!")
    else:
        print("AHa! Je le savais! Mes sens d'aventurière ne me mentent jamais!")

def start_sac(objets_dans_sac, ls_inventaire):
    random_items = random.randint(0, 3)               #cette fonction programme le debut de la journée ainsi que le sac de départ (en chiffres randomisés).
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

def text_inventaire(objets_dans_sac) :     #fonction qui fait la convertion du sac en texte avec les quantitées : ["potion", "potion", "potion"] deviendras ['3 potions']
    ls_inventaire = []

    inventaire_en_texte = objets_dans_sac.count("potions scintillantes")
    ls_inventaire.append(f"{inventaire_en_texte} potions scintillantes")

    inventaire_en_texte = objets_dans_sac.count("clés mystérieuses")
    ls_inventaire.append(f"{inventaire_en_texte} clés mystérieuses")

    inventaire_en_texte = objets_dans_sac.count("boules brillantes")
    ls_inventaire.append(f"{inventaire_en_texte} boules brillantes")

    inventaire_en_texte = objets_dans_sac.count("squelettes miniatures")
    ls_inventaire.append(f"{inventaire_en_texte} squelettes miniatures")

    return ls_inventaire

def sort_end_day(objets_dans_sac):
    print("ALORS! avant de finir cette splendide journée d'aventure, FAUT TRIER MON SAC!")          #fin de la journée, fonction qui mets de l'ordre dans le sac d'items.
    sorted(objets_dans_sac)
    ls_inventaire = text_inventaire(objets_dans_sac)
    print(ls_inventaire)



#Listes
objets_dans_sac = []                      # C'est les objets qui sont déja dans le sac
objets_a_mettre_d_sac = []                # C'est les objets à mettre dans la sac
ls_inventaire = []                        # C'est le texte de l'inventaire
ls_nb_items = []                          # C'est le nombre d'items de chaque dans l'inventaire

#Variables
random_items = 0                         # Nombre random d'items à ajouté/présent
random_nb = 0                            # Nombre random

if __name__ == '__main__':
    start_sac(objets_dans_sac, ls_inventaire)
    for i in range(7):
        newDay(objets_dans_sac)
        while len(objets_dans_sac) > 15:
            if len(objets_dans_sac) > 15:
                sac_plein(objets_dans_sac)
            elif sac_plein(objets_dans_sac) == 15:
                print("On en a assez!Allons-y!")
            else:
                break
        ls_inventaire = text_inventaire(objets_dans_sac)
        sort_end_day(objets_dans_sac)
        randomSac(objets_dans_sac)                      #debut du mini-je de devinettes: notre choix random.
        randomChoice(objets_dans_sac)                   #zigomar devines.


