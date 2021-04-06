"""
    Shifumi (BigBangTheory)
    Emilien BIDET
    17 novembre 2020
    python 3.7.7
"""
from random import *
from math import *

listeRep = ["Lézard", "Papier", "Spock", "Pierre", "Ciseaux"]
commandeQuitter = "exit"

# Deux chaines de caractères correspondant aux réponses de chaque joueur et qui annonce le joueur gagnant
def QuiGagne(listeRep, rep1, rep2) :
    matriceResultat =   [["nul", "joueur1", "joueur1", "joueur2", "joueur2"],
                        ["joueur2" , "nul" , "joueur1", "joueur1", "joueur2"],
                        ["joueur2", "joueur2", "nul", "joueur1", "joueur1"],
                        ["joueur1" , "joueur2", "joueur2" , "nul" , "joueur1"],
                        ["joueur1" , "joueur1", "joueur2", "joueur2", "nul"]]
    posJoueur1 = listeRep.index(rep1)
    posJoueur2 = listeRep.index(rep2)
    return matriceResultat[posJoueur1][posJoueur2]


# Demande à l'utilisateur ce qu'il joue, vérifie si elle est conforme,
# il redemande à l'utilisateur tant que la réponse n'est pas conforme.
def traitementRep(listeRep) :
    repConforme = False
    # On boucle tant que la réponse n'est pas conforme
    while not repConforme :
        print("Lézard, Papier, Spock, Pierre, Ciseaux")
        rep = input("Que voulez jouez ?\n")
        if rep in listeRep:
            repConforme = True
            return rep
        elif rep == commandeQuitter:
            exit()

# Réponse de l'Ordinateur (aléatoire)
def reponseOrdi(listeRep) :
    return choice(listeRep)

# Représente une manche de shifumi
def jeux(listeRep, nbCoup) :
    #[nbCoupGagnésParJoueur, nbCoupGagnésParOrdi]
    resultats = [0,0]
    for i in range(nbCoup):

        # Obtention des réponses
        repJoueur = traitementRep(listeRep)
        repOrdi = reponseOrdi(listeRep)

        # On compare les deux réponses
        res = QuiGagne(listeRep, repJoueur, repOrdi)

        # Mise à jour du compteur
        if res == "joueur1":
            resultats[0] += 1
        else:
            resultats[1] += 1

        print("------------- Coup " + str(i + 1) + "/" + str(nbCoup) + " -------------")
        print("Réponse du joueur        : " + repJoueur)
        print("Réponse de l'ordinateur  : " + repOrdi)
        # Affiche le score courant sous la forme Joueur nbCoupGagnésParJoueur/nbCoupGagnésParOrdi Ordinateur
        # ex: Joueur 5/4 Ordinateur
        print("Scores : Joueur " + str(resultats[0]) + "/" + str(resultats[1]) + " Ordinateur")

    if resultats[0] > resultats[1]:
        print("Victoire du joueur !!")
    elif resultats[0] == resultats[1]:
        print("Egalité")
    else:
        print("Victoire de l'ordinateur !!")


#Defini le nombre de jeux
def main() :
    print("Jeu du shifumi créé par Emilien BIDET")

    repConforme = False

    nbCoup = 0
    # On boucle tant que la réponse n'est pas conforme
    while not repConforme :
        nbCoup = input("Combien de coups ?\n")

        if nbCoup == commandeQuitter:
            exit()

        try:
            nbCoup = int(nbCoup)
            if nbCoup > 0:
                repConforme = True
            else:
                print("Veuillez entrer une valeur numérique entière positive non nulle")
        except Exception as e:
            print("Veuillez entrer une valeur numérique entière positive non nulle")

    print("Début de la partie !")
    jeux(listeRep, nbCoup)
    print("Fin de la partie ! créé par Emilien BIDET")

main()
