#!/usr/bin/python3


def test_cree_reseau():
    liste = ["Alice", "Bob", "Alice", "Dan", "Bob", "Carl"]
    attendu = {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl"],
        "Carl": ["Bob"],
        "Dan": ["Alice"]
    }
    resultat = cree_reseau(liste)
    assert resultat == attendu

    liste = ["Anna","Bob","Anna","Bob","Carl","Richard","Richard","Bob"]
    attendu = {
        "Anna": ["Bob"],
        "Bob": ["Anna"],
        "Carl": ["Richard"],
        "Richard": ["Carl", "Bob"]
    }
    resultat = cree_reseau(liste)
    assert resultat != attendu
    print("Test de la fonction cree_reseau : ok")
test_cree_reseau()




def test_liste_personne():
    reseau = {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }
    resultat = liste_personne(reseau)
    attendu = ["Alice", "Bob", "Carl", "Dan"]
    assert resultat == attendu
    print("Test de la fonction liste_personne : ok")
test_liste_personne()




def test_sont_amis():
    reseau = {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }
    assert sont_amis(reseau, "Alice", "Bob")
    assert not sont_amis(reseau, "Alice", "Carl")
    assert not sont_amis(reseau, "Dan","Renault")
    print("Test de la fonction sont_amis : ok")
test_sont_amis()




def test_sont_amis_de():
    reseau = {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }
    assert sont_amis_de("Alice", ["Bob", "Dan"], reseau)
    assert not sont_amis_de("Carl", ["Alice", "Dan"], reseau)
    print("Test de la fonction sont_amis_de : ok")
test_sont_amis_de()




def test_est_comu():
    reseau = {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }
    assert est_comu(["Alice", "Bob", "Dan"], reseau)
    assert not est_comu(["Alice", "Bob", "Carl"], reseau)
    print("Test de la fonction est_comu : ok")
test_est_comu()




def test_comu():
    reseau = {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }
    groupe = ["Alice", "Bob", "Carl", "Dan"]
    resultat = comu(groupe, reseau)
    attendu = ["Alice", "Bob", "Dan"]
    assert resultat == attendu
    print("Test de la fonction comu : ok")
test_comu()




def test_tri_insertion_desc():
    tab1 = [9,8,7,6,5,4]
    tab2 = [56,6,34,2,12]
    resultat1 = tri_insertion_desc(tab1)
    attendu1 = [4,5,6,7,8,9]
    resultat2 = tri_insertion_desc(tab2)
    attendu2 = [56,34,12,6,2]
    assert resultat1 != attendu1
    assert resultat2 == attendu2
    print("Test de la fonction tri_insertion_desc : ok")
test_tri_insertion_desc()




def test_tri_popu():
    reseau = {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }
    groupe = ["Alice", "Bob", "Carl", "Dan"]
    resultat = tri_popu(groupe, reseau)
    attendu = ["Bob", "Dan", "Alice", "Carl"]
    assert resultat == attendu
    print("Test de la fonction tri_popu : ok")
test_tri_popu()




def test_comu_dans_reseau():
    reseau = {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }
    resultat = comu_dans_reseau(reseau)
    attendu = ["Bob", "Dan", "Alice"]
    assert resultat == attendu
    print("Test de la fonction comu_dans_reseau : ok")
test_comu_dans_reseau()




def test_comu_dans_amis():
    reseau = {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }
    resultat = comu_dans_amis("Bob", reseau)
    attendu = ["Bob", "Dan", "Alice"]  
    assert resultat == attendu

    resultat = comu_dans_amis("Carl",reseau)
    attendu = ["Carl","Bob"]
    assert resultat == attendu

    resultat = comu_dans_amis("Dan",reseau)
    attendu = ["Dan","Carl"]
    assert resultat != attendu
    print("Test de la fonction comu_dans_amis : ok")
test_comu_dans_amis()




def test_comu_max():
    reseau = {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl","Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice","Bob"]
    }
    reseau2 = {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Carl"],
        "Carl": ["Bob"],
        "Dan": ["Alice","Bob"]
    }    
    resultat = comu_max(reseau)
    attendu = ["Alice", "Bob", "Dan"]
    assert resultat == attendu

    resultat = comu_max(reseau2)
    attendu = ["Alice", "Bob", "Dan"]
    assert resultat != attendu
    print("Test de la fonction comu_max : ok")
test_comu_max()
