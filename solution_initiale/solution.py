from tree.tree import Tree
from node.node import Node
from merge.merge import MergeBST

class Solution:
    def __init__(self):
        pass

    def choisir_parcours(self, arbre: Tree, numero_arbre: int) -> str:

        print(f"\nChoisissez le type de parcours pour l'arbre {numero_arbre}:")
        print("1. Infixe")
        print("2. Préfixe")
        print("3. Postfixe")
        
        choix = input("Votre choix (1, 2, ou 3) : ")

        if choix == "1":
            print(f"\nAffichage de l'arbre {numero_arbre} en ordre infixe :")
            arbre.print_in_order()
            return 'inorder'
        elif choix == "2":
            print(f"\nAffichage de l'arbre {numero_arbre} en ordre préfixe :")
            arbre.print_pre_order()
            return 'preorder'
        elif choix == "3":
            print(f"\nAffichage de l'arbre {numero_arbre} en ordre postfixe :")
            arbre.print_post_order()
            return 'postorder'
        else:
            print("Choix invalide, affichage en ordre infixe par défaut.")
            arbre.print_in_order()
            return 'inorder'

    def run(self) -> None:

        # Entrée des valeurs pour les racines et les tailles des arbres
        racine1_value = int(input("Entrez la valeur de la racine de l'arbre 1 : "))
        taille_arbre1 = int(input("Entrez la taille de l'arbre 1 (nombre de nœuds) : "))

        racine2_value = int(input("Entrez la valeur de la racine de l'arbre 2 : "))
        taille_arbre2 = int(input("Entrez la taille de l'arbre 2 (nombre de nœuds) : "))

        # Instancier les nœuds et les arbres
        arbre1 = Tree(Node(racine1_value))
        arbre2 = Tree(Node(racine2_value))

        # Génére nœuds aléatoires pour les deux arbres
        arbre1.generate_random_tree(taille_arbre1 - 1)
        arbre2.generate_random_tree(taille_arbre2 - 1)

        # Demande types de parcours
        p1 = self.choisir_parcours(arbre1, 1)
        p2 = self.choisir_parcours(arbre2, 2)

        # Fusionner les deux arbres
        print("\nFusion des deux arbres en cours...")
        merger = MergeBST(arbre1, arbre2)
        arbre_fusionne = merger.merge(p1, p2)

        # Affichage de l'arbre fusionné
        print("\nArbre fusionné (In-order):")
        arbre_fusionne.print_in_order()

        # Affichage graphique
        print("\nAffichage graphique de l'arbre 1 :")
        arbre1.plot_tree()
        print("\nAffichage graphique de l'arbre 2 :")
        arbre2.plot_tree()
        print("\nAffichage graphique de l'arbre fusionné :")
        arbre_fusionne.plot_tree()
