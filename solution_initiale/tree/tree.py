from node.node import Node
import matplotlib.pyplot as plt
import random

class Tree():
    '''
    Binary search tree class
    '''

    def __init__(self, root: Node)-> None:
        self.root = root
    
    # insertion dans arbre : créer racine si arbre vide sinon lancer récursivité

    def insert(self, value: int)-> None:
        '''
        Inserts a value into the tree
        Args:
            value: int: value to insert into the tree
        Returns:
            None
        '''
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    # méthode d'insertion récursive
   
    def _insert_recursive(self, node: Node, value: int) -> None:
        
        # valeur inférieur ? Gauche , créer noeud si pas de noeud et continuer récursivité à gauche
        if value < node.value:
            
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            # valeur supérieur ou égale ? Droite , créer noeud si pas de noeud et continuer récursivité à droite
            if node.right is None:
                node.right = Node(value) 
            else:
                self._insert_recursive(node.right, value)

    # Générateur d'ABR de valeur aléatoire avec random 

    def generate_random_tree(self, size: int)-> None:
            for _ in range(size):
                value = random.randint(0, 100)
                self.insert(value)
        
        # PAUSE

    def print_in_order(self)-> None:
        in_order_values = self._in_order_traversal(self.root)
        print(in_order_values)

    def print_pre_order(self)-> None:
        pre_order_values = self._pre_order_traversal(self.root)
        print(pre_order_values)

    def print_post_order(self)-> None:
        post_order_values = self._post_order_traversal(self.root)
        print(post_order_values)


    # Méthode additionnelles

        # récursivité in order : gauche , noeud puis droit

    def _in_order_traversal(self, node: Node) -> tuple:
        
        if node is None:
            return None
        return (self._in_order_traversal(node.left) , node.value , self._in_order_traversal(node.right))


        # récursivité pré order : noeud , gauche , droit
    
    def _pre_order_traversal(self, node: Node) -> tuple:
        
        if node is None:
            return None
        return(node.value , self._pre_order_traversal(node.left), self._pre_order_traversal(node.right))

        # récursivité post order : gauche , droit , noeud
    
    def _post_order_traversal(self, node: Node) -> tuple:

        if node is None:
            return None
        return (self._post_order_traversal(node.left), self._post_order_traversal(node.right), node.value)

            #AFFICHER
    def __str__(self) -> str:
        return ' '.join(map(str, self._in_order_values(self.root)))

    def _in_order_values(self, node: Node) -> list:
        if node is None:
            return []
        return self._in_order_values(node.left) + [node.value] + self._in_order_values(node.right)
    

    # REPRESENTATION EN 3D
    def plot_tree(self):
        '''
        Méthode pour dessiner l'arbre binaire de recherche en 2D avec Matplotlib.
        '''
        fig, ax = plt.subplots()
        ax.set_axis_off()  # Désactiver les axes
        
        def _plot_node(node, x, y, dx):
            '''
            Méthode récursive pour dessiner chaque nœud et ses enfants.
            
            Args:
                node: Node: Le nœud courant à dessiner.
                x, y: Coordonnées du nœud.
                dx: Décalage en x pour les enfants.
            '''
            if node:
                ax.text(x, y, str(node.value), ha='center', va='center', 
                        bbox=dict(facecolor='white', edgecolor='black', boxstyle='circle'))

                # Dessiner les enfants et les lignes
                if node.left:
                    ax.plot([x, x - dx], [y - 1, y - 2], 'k-')  # Lien vers le fils gauche
                    _plot_node(node.left, x - dx, y - 2, dx / 2)

                if node.right:
                    ax.plot([x, x + dx], [y - 1, y - 2], 'k-')  # Lien vers le fils droit
                    _plot_node(node.right, x + dx, y - 2, dx / 2)
        
        _plot_node(self.root, 0, 0, 4)  # Appel initial (x, y, et décalage en x)
        plt.show()
    
    


