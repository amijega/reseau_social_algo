#!/usr/bin/python3


def cree_reseau(liste):
    """
    Créer un dictionnaire d'amitié à partir d'une liste.
    Chaque couple représente une interaction d'amitié entre deux personnes
    Le réseau est représenté sous forme de dictionnaire où les clés sont les noms des personnes,
    et les valeurs sont les listes de leurs amis.
    """
    dico={}    #Crée un ditionnaire vide
    for a in range(len(liste)//2):  #Si la pemière personne du couple n'est pas dans le réseau, on l'ajoute en tant que clé dans le dico
        if liste[a*2] not in dico:
            dico[liste[a*2]]=[]
       
        if liste[a*2+1] not in dico:  #Si la deuxième personne du couple n'est pas dans le réseau, on l'ajoute en tant que clé dans le dico
            dico[liste[a*2+1]]=[]
       
        if liste[a*2] not in dico[liste[a*+1]]:   #Ajout des amis dans leur listes
            dico[liste[a*2]].append(liste[a*2+1])
            dico[liste[a*2+1]].append(liste[a*2])
        
        if liste[a*2+1] not in dico[liste[a*2]]:   #Ajout des amis dans leur listes
            dico[liste[a*2+1]].append(liste[a*2])
            dico[liste[a*2]].append(liste[a*2+1])
       
    return dico



def liste_personne(dico):
    """
    Obtenir la liste des personnes présentes dans un réseau.
    Le réseau est représenté sous forme de dictionnaire.
    Retourne une liste contenant les noms de toutes les personnes.
    """
    #Retourne la liste des clés du dictionnaire
    return list(dico.keys())



def sont_amis(reseau,a,b):
    """
    Vérifier si deux personnes sont amies dans le réseau.
    Prend en entrée le réseau, ainsi que les noms des deux personnes.
    Retourne True si elles sont amies, sinon False.
    """
    #Vérifie si 'b' est dans la liste des amis de 'a'
    return (b in reseau[a])



def sont_amis_de(a,groupe,reseau):
    """
    Vérifier si une personne est amie avec tous les membres d'un groupe.
    Prend en entrée le nom de la personne, un groupe de personnes, et le réseau.
    Retourne True si la personne est amie avec chaque membre du groupe, sinon False.
    """
    for i in groupe:        #Vérifie si 'a' est ami avec tous les membres du groupe
        if not sont_amis(reseau,a,i):
            return False      #Si une personne n'est pas amie, retourne False
    return True       #Sinon, retourne True
    


def est_comu(groupe, reseau):
    """
    Vérifier si un groupe est une communauté.
    Un groupe est une communauté si tous ses membres sont amis entre eux.
    Prend en entrée une liste de personnes et le réseau.
    Retourne True si le groupe est une communauté, sinon False.
    """
    commu=[k for k in groupe]  #copie du groupe passé en paramètre dans le tableau commu
    
    for i in range(len(groupe)-1):     #Parcoure le groupe de personnes
        commu.pop(0)         #Retire les personnes qui doivent être vérifiées comme étant amis avec le groupe restant
        if not sont_amis_de(groupe[i],commu,reseau):   
            return False        #Si la personne n'est pas ami avec le groupe restant, retourne False
    return True      #Sinon, retourne True



def comu(groupe,reseau):
    """
    Construire une communauté à partir d'un groupe de personnes et d'un réseau.
    Ajoute successivement des personnes à la communauté si elles sont amies avec tous ses membres.
    Retourne une liste représentant la communauté maximale trouvée.
    """
    #Initialise une communauté avec la première personne
    communaute=[groupe[0]]
  
    for pers in range(1,len(groupe)):        #Ajoute la personne si elle est amie avec tous les membres actuels de la communauté
        if sont_amis_de(groupe[pers],communaute,reseau):
            communaute.append(groupe[pers])
    return communaute         #Retourne la communauté maximale trouvée



def tri_insertion_desc(tab):
    """
    Fonction prend en paramètre un tableau et retourne le tableau trié dans l'ordre décroissant.
    Algorithme de tri par insertion.
    """
    for i in range(1, len(tab)):
        tmp = tab[i]
        j = i
        while j > 0 and tab[j - 1] < tmp:   #Décalage des éléments du tableau
            tab[j] = tab[j - 1]
            j -= 1
        tab[j] = tmp     #Insère l'élément à sa place 
        
    return tab


def tri_popu(groupe, reseau):
    """
    Trier un groupe de personnes par popularité décroissante (nombre d'amis).
    Prend en entrée une liste de prénoms et le réseau.
    Retourne une liste triée des noms, de la personne la plus populaire à la moins populaire.
    """
    #Calcul du nombre d'amis pour chaque personne
    tab = []
    for personne in groupe:
        nb = len(reseau[personne])  #Nombre d'amis de la personne
        tab.append([nb, personne])  #Ajoute le couple Nombre d'amis et la personne
        
    #Tri de tab en fonction du Nombre d'amis
    tab_tri=tri_insertion_desc(tab)
    
    #Récupère uniquement les prénoms triés
    resultat = [personne for _, personne in tab_tri]
    
    return resultat  



def comu_dans_reseau(reseau):
    """
    Construire une communauté maximale en triant les membres du réseau par popularité décroissante.
    Prend en entrée le réseau sous forme de dictionnaire.
    Retourne une communauté maximale sous forme de liste.
    """
    #Trie les membres du groupe par popularité décroisante
    tab=tri_popu(reseau,reseau)
    return comu(tab,reseau)   #Retourne la comu



def comu_dans_amis(personne, reseau):
    """
    Construire une communauté maximale à partir d'une personne et de ses amis.
    Trie les amis de la personne par popularité décroissante et les ajoute successivement à la communauté.
    Prend en entrée le nom de la personne et le réseau.
    Retourne une liste représentant la communauté maximale formée.
    """
    # On commence avec la personne dans la communauté
    communaute=[personne]
    amis=tri_popu(reseau[personne],reseau)   #liste les amis de la personne triés par popularité décroissante
   
    for i in amis:              #ajoute les amis à la communnaute
        communaute.append(i) 
    communaute_finale=comu(communaute,reseau)   #détermine la communaute_final
    return communaute_finale        



def comu_max(reseau):
    """
    Trouver la plus grande communauté possible dans un réseau.
    Applique la fonction comu_dans_amis pour chaque personne du réseau.
    Retourne la communauté maximale trouvée, sous forme d'une liste.
    """
    #Initialise une liste pour stocker la communauté maximale
    maxi=[]
    for i in reseau:
        tmp=maxi  #Sauvegarde la communauté actuelle
        maxi=comu_dans_amis(i,reseau)
        if len(maxi) <= len(tmp):  #Conserve la plus grande communauté
            maxi=tmp
    return maxi  #Retrouve la plus grande communauté touvée
