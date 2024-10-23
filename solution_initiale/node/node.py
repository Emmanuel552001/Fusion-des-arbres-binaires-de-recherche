class Node():
    '''Node class for binary search tree'''

    def __init__(self, value: int)-> None:

        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"