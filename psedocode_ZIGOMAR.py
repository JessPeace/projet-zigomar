#Jessyka et Jonathan
'''

donc au moins un bool pour si Zigomar devine bien ou non.
coder le dialogue et faire apparaitre la liste une fois bien organisée pour terminer la journée.
choix de selection d'objet a retirer du sac en cas de trop pleins d'objets:
rappel: AUTO TOUT OBJETS QUI COMMENCE PAR B OU CONTIENS UN CHIFFRE. else OUR CHOICE.
donc:

PPSEUDOCODE A LA BOURRE:

def mini_jeu():
    print({liste des objets dans sac})
    liste d'objets.random.randint:
    print({objet a indice random})

def zigomar(mini_jeu, sac, liste d'objets):
    if mini_jeu==False:
    zigomar == >:(
    elif mini_jeu == True:
    zigomar == :)

    afficher ls_inventaire
    afficher dialogue('voyons voir nos précieux items!')
    >if inventaire >15:
    inventaire for in range(quantitée necessaire a retirer) (???)                      parceque si on decide vraiment de faire un nombre random faut coder une limite impenetrable.
    afficher dialogue ('MON SAC EST PLEINS! vite! qu'on retire un item! J'AI PAS FINI DE PILLER! >:D ')
    si objet count('B','b'): ON PEUT AUSSI UTLISER ---> e in liste : retourne True si l'élément e appartient à la liste liste, ou retourne False sinon.
 ls_inventaie= remove(boulles)
 else input('BAH! toi choisis! je ne peux pas me décider!!)                       < la on rentrerais le nom de l'item a retirer ou le nombre de
                                                                                 l'indice parceque faut pas écrire 'squelette' et tout les 4 squelettes (exemple) sois retirer.
on peut aussi faire afficher le random integer de chaques indices de la liste d'inventaire, comme sa Zigomar peux retirer 1 objets de la liste selon son program.


def inventaire:
invetaire égal [randomSac(objet_dans_sac)                # Randomiser le sac]

so:

[randomChoice                            # C'est pour choisir un objet random pour le mini-quiz]
       [ random.choice(objet_dans_sac)]

ls_inventaire.random.choice = (potions.random.randint , clees.random.randint, boulles.random.randint, squelettes.random.randint)

exemple:                                                                    ###on veux que le nombre random apparais aussi avec l'item comme sa on sais combien elle retire si elle retire tout ou plus que 1.
ls_inventaire["potions",'clees', 'boulles', 'squelettes']
ls_nb_items[3,3,3,3]
ls_sac(ls_random_item, ls_inventaire)
print({random choice})                                                      ###est-ce qu'on donne des guess a zigomar? 3 chances genre? a revoir
zigomar = random choice
if zigomar.random.choice = random.choice:
mini_jeu = True
print('HAHA JE LE SAVAIS! >:D )
else:
print('tu as tricher! je suis sure que j'avais raison! >:( ')

-------------------------------------------------------------------------------------------
notes en classe:
for in inventaire(b,B):

** ls_inventaire[i].find("B", "b")
ls_inventaire.remove('boulles')
find item print nb item
if potion ajoute +(nb) to object index.


'''



"""
Les listes
    objets_dans_sac []                      # C'est les objets qui sont déja dans le sac
    objets_a_mettre_d_sac []                # C'est les objets à mettre dans la sac
    

Variables
    new_object                              # C'est les nouveaux objets qu'elle ramasse dans une nouvelle journée
    random_items                            # Nombre random d'items à ajouté/présent
    
    
Fonctions
   newDay(objets_dans_sac, new_object)                       # Fonction pour la nouvelle journée
   
   
   sac_plein(objet_dans_sac, objet_a_mettre_d_sac)
   
   
   randomSac(objet_dans_sac)                # Randomiser le sac
        random.shuffle(objet_dans_sac)
        
   randomChoice                            # C'est pour choisir un objet random pour le mini-quiz
        random.choice(objet_dans_sac)
        
   start_sac(random_items, objets_dans_sac)
        new random_items
        for i in range of random_items
"""