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
    def __eq__(self, t2):
        if self.root is None and t2.root is None:
            return True
        if sorted(self.inorder(self.root, [])) == sorted(t2.inorder(t2.root, [])):
            return True
        else:
            return False

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
        if node.right:
            newroot = Node(node.right.value)
            newroot.left = Node(node.value)
            newroot.left.left = node.left
            newroot.left.right = node.right.left
            newroot.right = node.right.right
            return newroot
        return node

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
        if node.left:
            newroot = Node(node.left.value)
            newroot.right = Node(node.value)
            newroot.right.right = node.right
            newroot.right.left = node.left.right
            newroot.left = node.left.left
            return newroot
        return node

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
            print(1)
            self.root = Node(value)
        else:
            self.root = AVLTree._helper(value, self.root)
        if AVLTree._balance_factor(self.root) > 1 or AVLTree._balance_factor(self.root) < -1:
            print(7, self.root, AVLTree._balance_factor(self.root))
            self.root = AVLTree._rebalance(self.root)
            print(7, self.root, AVLTree._balance_factor(self.root))

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
                print(2, node, AVLTree._balance_factor(node))
                node = AVLTree._helper(value, node.left)
                print(2, node, AVLTree._balance_factor(node))
            else:
                print(3, node, AVLTree._balance_factor(node))
                node.left = Node(value)
                print(3, node, AVLTree._balance_factor(node))
        elif value > node.value:
            if node.right:
                print(4, node, AVLTree._balance_factor(node))
                node = AVLTree._helper(value, node.right)
                print(4, node, AVLTree._balance_factor(node))

            else:
                print(5, node, AVLTree._balance_factor(node))
                node.right = Node(value)
                print(5, node, AVLTree._balance_factor(node))
        if AVLTree._balance_factor(node) > 1 or AVLTree._balance_factor(node) < -1:
            print(6, node, AVLTree._balance_factor(node))
            node = AVLTree._rebalance(node)
            print(6, node, AVLTree._balance_factor(node))
        return node

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
                return node
            else:
                node = AVLTree._left_rotate(node)
                return node
        elif AVLTree._balance_factor(node) > 0:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._left_rotate(node.left)
                return node
            else:
                node = AVLTree._right_rotate(node)
                return node

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
