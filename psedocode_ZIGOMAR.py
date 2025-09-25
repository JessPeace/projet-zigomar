#Jessyka et Jonathan
'''
liste, boucles, fonctions. chaines de caractères
faut programmer un SAC avce des choses dui peuvent entrer et sortir du SAC: dont une liste de choses:

 todo: des potions scintillantes, des clés mystérieuses, des boules brillantes, et même des squelettes miniatures.



 TODO:on devras aussi définir une fonction pour arranger aléatoirement les items dans le sac pour ensuite les
  organiser la liste en ordre alphabétique!

TODO: fuat aussi programmer ZIGOMAR elle même: QUOTTE:
Quand la chasse au trésor est terminée, Zigomar veut jouer à son mini-quiz farfelu :
Tu mélanges tous les objets du sac de façon aléatoire.
Tu attrapes un objet au hasard et Zigomar doit deviner ce que c’est.
Si Elle devine juste, elle saute de joie et te remercie ; sinon, elle te lance un regard noir et grogne…

todo: mettre une limite de 15 items dans la liste MAIS aussi coder une liste avec plus de 15 items pour
todo:offrir la possibilitée d'en avoir trop!
dont plus de dialogue a coder. car elle nous demandent quel items retirer, donc faudrais faire un print de
la liste a chaques fois qu'elle dépasse 15 items dans son sac.
MAIS:
TODO: QUOTTE:
TODO: Parfois, il est automatique : elle retire tous les objets dont le nom contient un chiffre ou la lettre "b" (elle a clairement un toc!).
todo:Parfois, elle te regarde (oui, toi !), et te demande quel objet tu veux qu’elle retire pour continuer sa chasse sans s’encombrer
 (elle dira par le suite que c'est de ta faute si elle a perdu ses objets précieux!).

 y'as pas que sa! faudras coder l'action de selection automatique!

TODO: donc au moins un bool pour si Zigomar devine bien ou non.
todo:coder le dialogue et faire apparaitre la liste une fois bien organisée pour terminer la journée.
choix de selection d'objet a retirer du sac en cas de trop pleins d'objets:
rappel: AUTO TOUT OBJETS QUI COMMENCE PAR B OU CONTIENS UN CHIFFRE. else OUR CHOICE.
donc:

PSEUDOCODE A LA BOURRE:

def mini_jeu():
    print({liste des objets dans sac})
    liste d'objets.random.randint:
    print({oobjet a indice random})

def zigomar(mini_jeu, sac, liste d'objets):
    if mini_jeu==False:
    zigomar == >:(
    elif mini_jeu == True:
    zigomar == :)

def inventaire:


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