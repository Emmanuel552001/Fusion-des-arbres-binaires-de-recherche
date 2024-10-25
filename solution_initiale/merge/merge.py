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
        result = []
        for item in t:
            if isinstance(item, tuple):
                result.extend(self._flatten_tuple(item))  
            elif item is not None:
                result.append(item)
        return result

    def _merge_tuples(self, list1: List[int], list2: List[int]) -> List[int]:

        result = []
        i, j = 0, 0

        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1

        result.extend(list1[i:])
        result.extend(list2[j:])

        return result

    def merge(self, p1: str, p2: str) -> Tree:

        list1 = self._flatten_tree(self.tree1, p1)
        list2 = self._flatten_tree(self.tree2, p2)

        merged_list = self._merge_tuples(list1, list2)


        merged_tree = Tree(None)
        for value in merged_list:
            merged_tree.insert(value)

        return merged_tree
