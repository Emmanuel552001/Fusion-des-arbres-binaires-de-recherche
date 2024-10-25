import sys
from tree.tree import Tree
from node.node import Node
from merge.merge import MergeBST

sys.setrecursionlimit(100000)

def main():
    racine1_value = int(input("Entrez la valeur de la racine de l'arbre 1 : "))
    taille_arbre1 = int(input("Entrez la taille de l'arbre 1 (nombre de nœuds) : "))

    racine2_value = int(input("Entrez la valeur de la racine de l'arbre 2 : "))
    taille_arbre2 = int(input("Entrez la taille de l'arbre 2 (nombre de nœuds) : "))
   
    racine1 = Node(racine1_value)
    racine2 = Node(racine2_value)
    arbre1 = Tree(racine1)
    arbre2 = Tree(racine2)

    print("\nGénération de nœuds supplémentaires pour les arbres...")
    arbre1.generate_random_tree(taille_arbre1 - 1)  
    arbre2.generate_random_tree(taille_arbre2 - 1)

    print("\nChoisissez un cas de fusion :")
    print("1. P1 = Infixe, P2 = Préfixe")
    print("2. P1 = Infixe, P2 = Postfixe")
    print("3. P1 = Préfixe, P2 = Préfixe")

    choix = int(input("Entrez le numéro du cas (1, 2 ou 3) : "))

    if choix == 1:
        p1 = 'inorder'
        p2 = 'preorder'
    elif choix == 2:
        p1 = 'inorder'
        p2 = 'postorder'
    elif choix == 3:
        p1 = 'preorder'
        p2 = 'preorder'
    else:
        print("Choix invalide. Veuillez relancer le programme et entrer un choix valide.")
        return

    # Fusion des arbres avec les parcours choisis
    merger = MergeBST(arbre1, arbre2)
    arbre_fusionne = merger.merge(p1, p2)

    # Affichage de l'arbre fusionné
    print("\nArbre fusionné (In-order):")
    arbre_fusionne.print_in_order()

    # Affichage graphique des arbres
    print("\nAffichage graphique de l'arbre 1 :")
    arbre1.plot_tree()
    print("\nAffichage graphique de l'arbre 2 :")
    arbre2.plot_tree()
    print("\nAffichage graphique de l'arbre fusionné :")
    arbre_fusionne.plot_tree()


if __name__ == '__main__':
    main()
