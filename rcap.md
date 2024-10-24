Fichiers
1. node.py
Ce fichier définit la classe Node, qui représente un nœud dans un arbre binaire de recherche.

    Classe Node :
        Attributs :
        value: La valeur du nœud.
        left: Le sous-arbre gauche.
        right: Le sous-arbre droit.
    Méthodes :
        __repr__(): Retourne une représentation lisible du nœud pour le débogage.

2. tree.py
    Ce fichier contient la classe Tree, qui permet de créer et manipuler un arbre binaire de recherche.

Classe Tree :
    Attributs :
        root: La racine de l'arbre (instance de Node).
    Méthodes principales :
        insert(value): Insère une valeur dans l'arbre.
        generate_random_tree(size): Génère un arbre binaire aléatoire avec le nombre de nœuds spécifié.
        print_in_order(), print_pre_order(), print_post_order(): Affiche l'arbre en parcours infixe, préfixe, ou postfixe.
        plot_tree(): Représente l'arbre visuellement en 2D avec matplotlib.
3. merge.py
Ce fichier définit la classe MergeBST, qui permet de fusionner deux arbres binaires de recherche.

Classe MergeBST :
Attributs :
tree1: Le premier arbre à fusionner.
tree2: Le deuxième arbre à fusionner.
Méthodes :
_flatten_tree(tree, order): Génère une liste des valeurs de l'arbre selon le type de parcours (inorder, preorder, postorder).
_flatten_tuple(t): Aplati un tuple en une liste de valeurs.
_merge_tuples(list1, list2): Fusionne deux listes triées en une seule.
merge(p1, p2): Fusionne deux arbres en utilisant les types de parcours spécifiés.
4. main.py
Ce fichier est le point d'entrée du projet. Il permet à l'utilisateur d'entrer les valeurs des racines et la taille des deux arbres, puis de sélectionner le type de fusion souhaité.

Fonctionnement :
L'utilisateur entre la racine et la taille de chaque arbre.
L'utilisateur choisit le type de parcours pour la fusion des arbres.
Les arbres sont fusionnés et affichés en parcours infixe.