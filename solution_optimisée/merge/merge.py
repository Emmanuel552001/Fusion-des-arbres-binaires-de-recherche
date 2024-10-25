from node.node import Node
from tree.tree import Tree

class MergeBST():


    def __init__(self, tree1: Tree, tree2: Tree) -> None:
        self.tree1 = tree1
        self.tree2 = tree2

    def merge(self, p1: str, p2: str) -> Tree:

        iter1 = self._traverse_tree(self.tree1.root, p1)
        iter2 = self._traverse_tree(self.tree2.root, p2)

        val1 = next(iter1, None)
        val2 = next(iter2, None)

        # Créer un arbre fusionné vide
        merged_tree = Tree(None)

        while val1 is not None or val2 is not None:
            if val1 is not None and (val2 is None or val1 <= val2):
                merged_tree.insert(val1)
                val1 = next(iter1, None)
            elif val2 is not None:
                merged_tree.insert(val2)
                val2 = next(iter2, None)

        return merged_tree

    def _traverse_tree(self, node, order):

        if node:
            if order == 'preorder':
                yield node.value
                yield from self._traverse_tree(node.left, order)
                yield from self._traverse_tree(node.right, order)
            elif order == 'inorder':
                yield from self._traverse_tree(node.left, order)
                yield node.value
                yield from self._traverse_tree(node.right, order)
            elif order == 'postorder':
                yield from self._traverse_tree(node.left, order)
                yield from self._traverse_tree(node.right, order)
                yield node.value
