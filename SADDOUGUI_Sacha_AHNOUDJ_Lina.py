
#####################################################
############## AHNOUDJ Lina #########################
############## SADDOUGUI Sacha ######################
#####################################################

#####################################################
############ FONCTIONS AUXILIAIRES   ###############
#####################################################

def verif_triee(L):
    #Algo de verification de liste triée
    for i in range(len(L)-1):
        if L[i] > L[i+1]:

            return False

    return True

def gestion_date(date):
    #on convertit chaque mois en son numéro
    liste_date= date.split(" ")
    if liste_date[1] == "Jan":
        liste_date[1] = "01"
    elif liste_date[1] == "Feb":
        liste_date[1] = "02"
    elif liste_date[1] == "Mar":
        liste_date[1] = "03"
    elif liste_date[1] == "Apr":
        liste_date[1] = "04"
    elif liste_date[1] == "May":
        liste_date[1] = "05"
    elif liste_date[1] == "Jun":
        liste_date[1] = "06"
    elif liste_date[1] == "Jul":
        liste_date[1] = "07"
    elif liste_date[1] == "Aug":
        liste_date[1] = "08"
    elif liste_date[1] == "Sep":
        liste_date[1] = "09"
    elif liste_date[1] == "Oct":
        liste_date[1] = "10"
    elif liste_date[1] == "Nov":
        liste_date[1] = "11"
    elif liste_date[1] == "Dec":
        liste_date[1] = "12"
    for i in range(len(liste_date)-1):
        if liste_date[i] == "":
            liste_date.remove(liste_date[i])
    return liste_date[2] + "/" + liste_date[1] + "/" + liste_date[4]

#################################################
############ FONCTIONS PRINCPALE ################
#################################################

####LES IMPORTS

import os
import re
import datetime
import time

############ EXEERCICE 1 ################

def intersection_2_listes(L1 ,L2):
    #On verifie que les listes sont triées
    assert (verif_triee(L1) and verif_triee(L2)), "les listes ne sont pas triées, il faut les modifier"
    #On initialise la liste qui va contenir les valeurs communes
    L3 = []
    #On parcourt la liste L1
    for i in range(len(L1)):
        #Si la valeur de L1 est dans L2 et n'est pas dans L3, on l'ajoute à L3
        if L1[i] in L2 and L1[i] not in L3:
            L3.append(L1[i])
    #On retourne la liste L3
    return L3

def intersection(L):
    #on vérifie que chaque liste de liste est triée
    for i in range(len(L)):
        assert (verif_triee(L[i])), "les listes ne sont pas triées, il faut les modifier"
    #On initialise la liste qui va contenir les valeurs communes et le compteur
    L3 = L[0]
    compteur=0
    #On parcourt chaque element de la liste L
    while compteur < len(L):
        #on incrémente le compteru afin de voir chaque sous liste de L
        L3 = intersection_2_listes(L3,L[compteur])
        compteur += 1
    #On retourne la liste L3
    return L3

############ EXEERCICE 2 ################

class Pile:
    #implémentation de la pile
    def pile_vide(self):
        return []

    def est_vide(self,p):
        return p == []

    def sommet(self,p):
        #on verifie que la pile n'est pas vide
        assert not len(p)==0, "La pile est vide"
        #on renvoie le dernier élément de la pile
        return p[-1]

    def empiler(self,p,e):
        #on ajoute un element à la pile
        p.append(e)

    def depiler(self,p):
        #on verifie que la pile n'est pas vide
        assert not len(p)==0, "La pile est vide"
        #on enleve le dernier element de la pile
        return p.pop()

def convertion_dec_bin(nombreDécimal):
    #initialisation de la pile et de la liste contenant le resultat binaire
    pile=Pile()
    liste=[]
    listeBis=[]
    #on fait une division par 2 tant que le nombre n'est pas nul
    while nombreDécimal != 0:
        #on empile le reste de la division par 2
        pile.empiler(liste,nombreDécimal%2)
        #on divise le nombre par 2
        nombreDécimal = nombreDécimal//2

    #on dépile la pile et on ajoute les éléments à la liste
    while not pile.est_vide(liste):
        #on depile dans une liste
        listeBis.append(pile.depiler(liste))

    return listeBis

############ EXEERCICE 3 ################

#on importe la librairie regex qui est très efficace pour ce genre de cas

def mot_de_passe(passwd):
    #on verifie que le mot de passe contient une minuscile
    min=re.search("[a-z]",passwd)
    #on verifie que le mot de passe contient une majuscule
    maj=re.search("[A-Z]",passwd)
    #on verifie que le mot de passe contient un chiffre
    chiffre=re.search("[0-9]",passwd)
    #on verifie que le mot de passe contient un caractère spécial
    spe=re.search("[!@#$%^&*()_+={}|:;'<>.?]",passwd)

    if min and maj and chiffre and spe:
        #si toutes les conditions sont respectées, on retourne True
        return True
    else:
        return False

######
#la fonction mot_de_passe et tester dans la rebrique test
######

############ EXEERCICE 4 ################

def verif_HTML(htmlTXT):
    #on ouvre le fichier
    fichier = open(htmlTXT, "r")
    fichiertxt = fichier.read()

    #on initialise les listes qui vont contenir les balises ouvrantes et fermantes
    listeManip=[]
    listeBaliseOuvrante=[]
    listeBaliseFermante=[]

    #on parcourt le fichier
    for i in range(len(fichiertxt)):

        #on verifie si on a une balise ouvrante
        if fichiertxt[i] == "<" and fichiertxt[i+1] != "/":
            i+=1
            while fichiertxt[i] != ">":
                listeManip.append(fichiertxt[i])
                i+=1

                #on verifie si c'est une balise qui ce ferme elle meme
                if fichiertxt[i] == "/":
                    listeManip=[]
                    break

                #on verifie si il y a un espace dans la balise pour ne pas prendre en compte les attributs, classes, id, etc...
                if fichiertxt[i] == " ":
                    break

            #on verifie que la balise n'est pas une balise meta ou doctype
            if ''.join(listeManip) != "meta" and ''.join(listeManip) != "!DOCTYPE":
                #on ajoute dans la liste ouvrant chaque balise
                listeBaliseOuvrante.append(''.join(listeManip))
                listeManip=[]
            listeManip=[]

        #on verifie si on a une balise fermante
        elif fichiertxt[i] == "<" and fichiertxt[i+1] == "/":
            i+=2
            while fichiertxt[i] != ">":
                listeManip.append(fichiertxt[i])
                i+=1

            #on ajoute dans la liste fermante chaque balise
            listeBaliseFermante.append(''.join(listeManip))
            listeManip=[]

    #on verifie que chaque balise ouvrante a une balise fermante
    if len(listeBaliseFermante) == len(listeBaliseOuvrante):
        for i in range(len(listeBaliseFermante)):
           #on verifie que la balise fermante est bien la balise ouvrante
           if listeBaliseFermante[i] in listeBaliseOuvrante:
                listeBaliseOuvrante.remove(listeBaliseFermante[i])

    #on verifie que la liste ouvrante est vide
    if len(listeBaliseOuvrante) == 0:
        return True
    else:
        return False

def copmteur_occurence(htmlTXT):
    #on ouvre le fichier
    fichier = open(htmlTXT, "r")
    fichiertxt = fichier.read()

    #on verifie que le fichier est bien un fichier html
    if verif_HTML(htmlTXT)!=True:
        return "Le fichier n'est pas un fichier html"
    else:
        #on initialise la liste qui va contenir les balises
        listeBalise=[]
        listeBaliseOuvrante=[]
        #on parcourt le fichier
        for i in range(len(fichiertxt)):
            #on verifie si on a une balise ouvrante
            if fichiertxt[i] == "<" and fichiertxt[i+1] != "/":
                i+=1
                while fichiertxt[i] != ">":
                    listeBalise.append(fichiertxt[i])
                    i+=1

                    #on verifie si il y a un espace dans la balise pour ne pas prendre en compte les attributs, classes, id, etc...
                    if fichiertxt[i] == " ":
                        break

                #on ajoute dans la liste ouvrant chaque balise
                listeBaliseOuvrante.append(''.join(listeBalise))
                listeBalise=[]

        #on initialise le dictionnaire qui va contenir les balises et leurs occurences
        dico={}
        #on parcourt la liste des balises ouvrantes
        for i in range(len(listeBaliseOuvrante)):

            #on verifie si la balise est deja dans le dictionnaire
            if listeBaliseOuvrante[i] in dico:
                #si oui on incremente son occurence
                dico[listeBaliseOuvrante[i]]+=1
            else:
                #si non on l'ajoute au dictionnaire
                dico[listeBaliseOuvrante[i]]=1

        return dico





################ EXERCICE 5 ################

def fichier_repertoire():
    #l'utilisateur saisi le nom du répertoire et son chemin, ainsi UNE date de modification
    chemin_du_repertoire = input("Entrez le nom du répertoire et son chemin: ")
    date= input("Entrez la date de modification du fichier: ")

    # Listez les fichiers et dossiers dans un répertoire donné
    element_du_doss = os.listdir(chemin_du_repertoire)

    #parcours de la liste des fichiers et dossiers
    for i in range(len(element_du_doss)):

        #récuperation de la date de modification du fichier, on utilise la fonction auxiliaire gestion_date pour convertir la date en format jj/mm/aaaa
        temps_modification = time.ctime(os.path.getctime(element_du_doss[i]))
        dateFinal = (gestion_date(temps_modification))

        dateComp= dateFinal.split("/")
        dateDemande= date.split("/")

        #on compare les dates en dehors du if pour un code plus lisible
        cond = int(dateComp[2]) > int(dateDemande[2])
        cond0 = int(dateComp[2]) >= int(dateDemande[2])
        cond1 = int(dateComp[1]) > int(dateDemande[1])
        cond2 = int(dateComp[1]) >= int(dateDemande[1])
        cond3 = int(dateComp[0]) >= int(dateDemande[0])
        
        if (cond) or (cond0 and cond1) or (cond0 and cond2 and cond3):
            print("le fichier " + element_du_doss[i] + " correspond à la demande")

#############################################
############ FONCTIONS TESTS ################
#############################################

#test de la fonction intersection_2_listes
def test_intersection_2_listes():
    #On teste la fonction avec des cas spécifiques
    assert (intersection_2_listes([1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10]) == [1,2,3,4,5,6,7,8,9,10]),"verification1 exercice 1.1"
    assert (intersection_2_listes([1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9]) == [1,2,3,4,5,6,7,8,9]),"verification2 exercice 1.1"
    assert (intersection_2_listes([1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8]) != [1,2,4,5,6,7,8]),"verification3 exercice 1.1"
    assert (intersection_2_listes([1,2,3,4,5,6,7,8,9,10],[]) == []),"verification4 exercice 1.1"
    assert (intersection_2_listes([9,9,9,9,9,9],[9,9,9,9,9,9,9,9]) == [9]),"verification5 exercice 1.1"
    return True

def test_intersection():
    #On teste la fonction avec des cas spécifiques
    assert (intersection([[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10]]) == [1,2,3,4,5,6,7,8,9,10]),"verification1 exercice 1.2"
    assert (intersection([[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9]]) == [1,2,3,4,5,6,7,8,9]),"verification2 exercice 1.2"
    assert (intersection([[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8]]) != [1,2,4,5,6,7,8]),"verification3 exercice 1.2"
    assert (intersection([[1,2,3,4,5,6,7,8,9,10],[1,2,5],[]]) == []),"verification4 exercice 1.2"
    assert (intersection([[9,9,9,9,9,9],[9,9,9,9,9,9,9,9],[9,9,9]]) == [9]),"verification5 exercice 1.2"
    assert (intersection([[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7],[12]]) == []),"verification6 exercice 1.2"
    return True

def test_convertion_dec_bin():
    #On teste la fonction avec des cas spécifiques
    assert (convertion_dec_bin(10) == [1,0,1,0]),"verification1 exercice 2"
    assert (convertion_dec_bin(0) == []),"verification2 exercice 2"
    assert (convertion_dec_bin(1) == [1]),"verification3 exercice 2"
    assert (convertion_dec_bin(2) == [1,0]),"verification4 exercice 2"
    assert (convertion_dec_bin(3) == [1,1]),"verification5 exercice 2"
    assert (convertion_dec_bin(4) == [1,0,0]),"verification6 exercice 2"
    assert (convertion_dec_bin(5) == [1,0,1]),"verification7 exercice 2"
    assert (convertion_dec_bin(6) == [1,1,0]),"verification8 exercice 2"
    assert (convertion_dec_bin(7) == [1,1,1]),"verification9 exercice 2"
    assert (convertion_dec_bin(8) == [1,0,0,0]),"verification10 exercice 2"
    assert (convertion_dec_bin(9) == [1,0,0,1]),"verification11 exercice 2"
    assert (convertion_dec_bin(10) == [1,0,1,0]),"verification12 exercice 2"
    assert (convertion_dec_bin(11) == [1,0,1,1]),"verification13 exercice 2"
    assert (convertion_dec_bin(12) == [1,1,0,0]),"verification14 exercice 2"
    return True


def test_mot_de_passe():
    #On teste la fonction avec des cas spécifiques
    assert (mot_de_passe("azertyuiop") == False),"verification1 exercice 3"
    assert (mot_de_passe("AZERTYUIOP") == False),"verification2 exercice 3"
    assert (mot_de_passe("azertyuiopAZERTYUIOP") == False),"verification3 exercice 3"
    assert (mot_de_passe("azertyuiopAZERTYUIOP1234567890") == False),"verification4 exercice 3"
    assert (mot_de_passe("azertyuiopAZERTYUIOP1234567890!") == True),"verification5 exercice 3"
    assert (mot_de_passe("azertyuiopAZERTYUIOP1234567890!@#$%^&*()_+={}|:;'<>.?") == True),"verification6 exercice 3"
    assert (mot_de_passe("") == False),"verification7 exercice 3"
    return True
    
def test_verif_HTML():
    #On teste la fonction avec des cas spécifiques
    assert (verif_HTML("test.txt") == True),"verification1 exercice 4"
    assert (verif_HTML("test1.txt") == False),"verification2 exercice 4"
    return True

#############################################
#               lancement des tests         #
#############################################

def main():
    if test_intersection_2_listes() :
        print("test_intersection_2_listes() : OK")
    else:
        print("test_intersection_2_listes() : ERREUR")
    if test_intersection() :
        print("test_intersection() : OK")
    else:
        print("test_intersection() : ERREUR")
    if test_convertion_dec_bin() :
        print("test_convertion_dec_bin() : OK")
    else:
        print("test_convertion_dec_bin() : ERREUR")
    if test_mot_de_passe() :
        print("test_mot_de_passe() : OK")
    else:
        print("test_mot_de_passe() : ERREUR")
    if test_verif_HTML() :
        print("test_verif_HTML() : OK")
    else:
        print("test_verif_HTML() : ERREUR")




main()













