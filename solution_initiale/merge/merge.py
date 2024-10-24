from typing import List
from tree.tree import Tree
from node.node import Node

class MergeBST():
    '''
    Class to merge two binary search trees using tuple comparison.
    '''

    def __init__(self, tree1: Tree, tree2: Tree) -> None:
        self.tree1 = tree1
        self.tree2 = tree2

    def _flatten_tree(self, tree: Tree, order: str) -> List[int]:
        '''
        Génère une liste aplatie des valeurs de l'arbre selon le type de parcours.

        Args:
            tree: Tree: L'arbre à aplatir.
            order: str: Le type de parcours ('inorder', 'preorder', 'postorder').
        
        Returns:
            List[int]: Liste aplatie des valeurs de l'arbre selon l'ordre de parcours spécifié.
        '''
        if order == 'inorder':
            traversal = tree._in_order_traversal(tree.root)
        elif order == 'preorder':
            traversal = tree._pre_order_traversal(tree.root)
        elif order == 'postorder':
            traversal = tree._post_order_traversal(tree.root)
        else:
            raise ValueError(f"Ordre de parcours non supporté : {order}")
        
        return self._flatten_tuple(traversal)

    def _flatten_tuple(self, t: tuple) -> List[int]:
        '''
        Aplatie un tuple imbriqué en une liste plate de valeurs entières.

        Args:
            t: tuple: Le tuple à aplatir.
        
        Returns:
            List[int]: Liste plate des valeurs extraites du tuple.
        '''
        result = []
        for item in t:
            if isinstance(item, tuple):
                result.extend(self._flatten_tuple(item))  # Appel récursif pour aplatir
            elif item is not None:
                result.append(item)
        return result

    def _merge_tuples(self, list1: List[int], list2: List[int]) -> List[int]:
        '''
        Fusionne deux listes triées en une seule liste triée.

        Args:
            list1: List[int]: La première liste triée.
            list2: List[int]: La deuxième liste triée.
        
        Returns:
            List[int]: La liste fusionnée et triée.
        '''
        result = []
        i, j = 0, 0

        # Fusionner les listes comme deux listes triées
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1

        # Ajouter les éléments restants
        result.extend(list1[i:])
        result.extend(list2[j:])

        return result

    def merge(self, p1: str, p2: str) -> Tree:
        '''
        Fusionne les deux arbres en utilisant les parcours spécifiés P1 et P2.

        Args:
            p1: str: Le type de parcours pour l'arbre 1 ('inorder', 'preorder', 'postorder').
            p2: str: Le type de parcours pour l'arbre 2 ('inorder', 'preorder', 'postorder').
        
        Returns:
            Tree: L'arbre fusionné respectant les propriétés d'un ABR.
        '''
        # Générer les listes aplaties pour les deux arbres
        list1 = self._flatten_tree(self.tree1, p1)
        list2 = self._flatten_tree(self.tree2, p2)

        # Fusionner les listes
        merged_list = self._merge_tuples(list1, list2)

        # Créer un nouvel arbre à partir de la liste fusionnée
        merged_tree = Tree(None)
        for value in merged_list:
            merged_tree.insert(value)

        return merged_tree
