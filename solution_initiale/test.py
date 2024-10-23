from typing import List
from tree.tree import Tree

class Solution:
    def __init__(self, tree1: Tree, tree2: Tree):
        self.tree1 = tree1
        self.tree2 = tree2

    def choisir_parcours(self, arbre: Tree, numero_arbre: int) -> None:
        '''
        Demande à l'utilisateur de choisir le type de parcours pour un arbre.
        Args:
            arbre: Tree: l'arbre pour lequel on choisit le parcours
            numero_arbre: int: le numéro de l'arbre (1 ou 2)
        '''
        print(f"\nChoisissez le type de parcours pour l'arbre {numero_arbre}:")
        print("1. Infixe")
        print("2. Préfixe")
        print("3. Postfixe")
        
        choix = input("Votre choix (1, 2, ou 3) : ")

        if choix == "1":
            print(f"\nAffichage de l'arbre {numero_arbre} en ordre infixe :")
            arbre.print_in_order()
        elif choix == "2":
            print(f"\nAffichage de l'arbre {numero_arbre} en ordre préfixe :")
            arbre.print_pre_order()
        elif choix == "3":
            print(f"\nAffichage de l'arbre {numero_arbre} en ordre postfixe :")
            arbre.print_post_order()
        else:
            print("Choix invalide, affichage en ordre infixe par défaut.")
            arbre.print_in_order()

    def run(self) -> None:
        '''
        Exécute la génération et l'affichage des arbres en fonction des choix de parcours.
        '''
        print('Génération et affichage des arbres...')

        # Demande le type de parcours pour l'arbre 1
        self.choisir_parcours(self.tree1, 1)

        # Demande le type de parcours pour l'arbre 2
        self.choisir_parcours(self.tree2, 2)
