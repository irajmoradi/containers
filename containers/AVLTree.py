'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the functions in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes have a balance factor in [-1,0,1].
        '''
        if self.root is None:
            return True
        else:
            return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        if AVLTree._balance_factor(node) > 1 or AVLTree._balance_factor(node) < -1:
            return False
        if node.left:
            if AVLTree._is_avl_satisfied(node.left) is False:
                return False
        if node.right:
            if AVLTree._is_avl_satisfied(node.right) is False:
                return False
        return True

    @staticmethod
    def listofbalfactors(node, start, traversal):
        if start:
            traversal.append(start.balance_factor())
            traversal = node.preorder(start.left, traversal)
            traversal = node.preorder(start.right, traversal)
        return traversal

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        tempvalue = Node(node.right.value)
        tempvalue2 = node.right.left
        tempvalue3 = Node(node.value)
        tempvalue.right = node.right.right
        tempvalue.left = tempvalue3
        tempvalue.left.left = node.left
        tempvalue.left.right = tempvalue2
        return tempvalue

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        tempvalue = Node(node.left.value)
        tempvalue2 = node.left.right
        tempvalue3 = Node(node.value)
        tempvalue.left = node.left.left
        tempvalue.right = tempvalue3
        tempvalue.right.right = node.right
        tempvalue.right.left = tempvalue2
        return tempvalue

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        if self.root is None:
            self.root = Node(value)
        else:
            AVLTree._helper(value, self.root)

    def insert_list(self, xs):
        for x in xs:
            if self.root is None:
                self.root = Node(x)
            else:
                self.root = AVLTree._helper(x, self.root)

    @staticmethod
    def _helper(value, node):
        if value <= node.value:
            if node.left:
                node.left = AVLTree._helper(value, node.left)
            else:
                node.left = Node(value)
        elif value > node.value:
            if node.right:
                node.right = AVLTree._helper(value, node.right)
            else:
                node.right = Node(value)
        if AVLTree._balance_factor(node) > 1 or AVLTree._balance_factor(node) < -1:
            AVLTree._rebalance(node)

    @staticmethod
    def _findpath(value, string, node):
        if node is None:
            return string
        if value < node.value:
            string.append(0)
            AVLTree._findpath(value, string, node.left)
        if value > node.value:
            string.append(1)
            AVLTree._findpath(value, string, node.right)
        if value == node.value:
            return string
        return string

    @staticmethod
    def _checkpath(path, node):
        bal = AVLTree._balance_factor(node)
        if len(path) == 0:
            pass
        elif node is None:
            return
        elif path[0] == 0:
            path = path[1:]
            AVLTree._checkpath(path, node.left)
        elif path[0] == 1:
            path = path[1:]
            AVLTree._checkpath(path, node.right)
        if bal > 1 or bal < -1:
            node = AVLTree._rebalance(node)

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        if AVLTree._balance_factor(node) < 0:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
                node = AVLTree._left_rotate(node)
            else:
                node = AVLTree._left_rotate(node)
        elif AVLTree._balance_factor(node) > 0:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._left_rotate(node.left)
                node = AVLTree._right_rotate(node)
            else:
                node = AVLTree._right_rotate(node)
