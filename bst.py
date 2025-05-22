import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

# Data Definitions

BinTree : TypeAlias = Union['Node', None]

@dataclass(frozen = True)
class Node:
    val : any
    left : BinTree
    right : BinTree

@dataclass(frozen = True)
class BinarySearchTree:
    comes_before : Callable[[any, any], bool]
    tree : BinTree

# Functions

# returns True if a binary search tree is empty
def is_empty(bst : BinarySearchTree) -> bool:
    match bst.tree:
        case None:
            return True
        case Node:
            return False  

# inserts a value into a binary tree using a comes_before function
def insert_helper(bt : BinTree, new_val : any, comes_before : Callable[[any, any], bool]) -> BinTree:
    match bt:
        case None:
            return Node(new_val, None, None)
        case Node(v, l, r):
            if comes_before(new_val, v):
                return Node(v, insert_helper(l, new_val, comes_before), r)
            else:
                return Node(v, l, insert_helper(r, new_val, comes_before))

# inserts a value into a binary search tree
def insert(bst : BinarySearchTree, new_val : any) -> BinarySearchTree:
    return BinarySearchTree(bst.comes_before, insert_helper(bst.tree, new_val, bst.comes_before))

# uses the ordering function of a binary search tree to look for a specified value
def lookup_helper(bt : BinTree, val : any, comes_before : Callable[[any, any], bool]) -> bool:
    match bt:
        case None:
            return False
        case Node(v, l, r):
            if comes_before(val, v):
                return lookup_helper(l, val, comes_before)
            elif comes_before(v, val):
                return lookup_helper(r, val, comes_before)
            else:
                return True

# returns True if a value is stored in a binary search tree and False otherwise
def lookup(bst: BinarySearchTree, val : any) -> bool:
    return lookup_helper(bst.tree, val, bst.comes_before)

# returns a the largest value in a binary tree
def largest(bt : BinTree) -> any:
    match bt:
        case None:
            raise ValueError('No largest value in an empty tree')
        case Node(v, l, r):
            if r is None:
                return v
            else:
                return largest(r)

# returns a binary tree without the largest value
def rem_largest(bt : BinTree) -> BinTree:
    match bt:
        case None:
            raise ValueError('Cannot remove the largest value from an empty tree')
        case Node(v, l, r):
            if r is None:
                return l
            else:
                return Node(v, l, rem_largest(r))

# removes a value from a binary tree and replaces it with the largest value to the left
def delete_helper(bt : BinTree, val : any, comes_before : Callable[[any, any], bool]) -> BinTree:
    match bt:
        case None:
            raise ValueError('Value is not in Binary Search Tree')
        case Node(v, l, r):
            if comes_before(val, v):
                return Node(v, delete_helper(l, val, comes_before), r)
            elif comes_before(v, val):
                return Node(v, l, delete_helper(r, val, comes_before))
            else:
                if l is None:
                    return r
                else:
                    return Node(largest(l), rem_largest(l), r)

# removes a value from a binary search tree and returns the resulting binary search tree
def delete(bst : BinarySearchTree, val : any) -> BinarySearchTree:
    if lookup(bst, val):
        return BinarySearchTree(bst.comes_before, delete_helper(bst.tree, val, bst.comes_before))
    else:
        raise ValueError('Value is not in Binary Search Tree')

# Test Cases
class Tests(unittest.TestCase):
    def test_is_empty(self):
        def less_than(x : int, y : int) -> bool:
            return x < y
        
        test_bstree_empty = BinarySearchTree(less_than, None)
        test_bstree_nonempty = BinarySearchTree(less_than, Node(1, None, Node(2, None, None)))

        self.assertTrue(is_empty(test_bstree_empty))
        self.assertFalse(is_empty(test_bstree_nonempty))
    
    def test_insert(self):
        def less_than(x : int, y : int) -> bool:
            return x < y

        test_bstree_none = BinarySearchTree(less_than, None)
        test_bstree = BinarySearchTree(less_than, Node(1, None, Node(3, None, None)))

        bstree_none_result = BinarySearchTree(less_than, Node(0, None, None))
        bstree_0_result = BinarySearchTree(less_than, Node(1, Node(0, None, None), Node(3, None, None)))
        bstree_2_result = BinarySearchTree(less_than, Node(1, None, Node(3, Node(2, None, None), None)))
        bstree_4_result = BinarySearchTree(less_than, Node(1, None, Node(3, None, Node(4, None, None))))

        self.assertEqual(bstree_none_result, insert(test_bstree_none, 0))
        self.assertEqual(bstree_0_result, insert(test_bstree, 0))
        self.assertEqual(bstree_2_result, insert(test_bstree, 2))
        self.assertEqual(bstree_4_result, insert(test_bstree, 4))
    
    def test_lookup(self):
        def less_than(x : int, y : int) -> bool:
            return x < y
        
        test_bstree = BinarySearchTree(less_than, Node(1, None, Node(3, None, Node(4, None, None))))

        self.assertTrue(lookup(test_bstree, 1))
        self.assertTrue(lookup(test_bstree, 3))
        self.assertTrue(lookup(test_bstree, 4))
        self.assertFalse(lookup(test_bstree, 0))
    
    def test_largest(self):
        bintree = Node(7, Node(5, Node(3, Node(2, None, None), None), Node(6, Node(4, None, None), None)), Node(10, Node(8, None, Node(9, None, None)), Node(12, None, None)))
        
        self.assertEqual(12, largest(bintree))
        self.assertEqual(6, largest(bintree.left))
    
    def test_rem_largest(self):
        bintree1 = Node(7, Node(5, Node(3, Node(2, None, None), None), Node(6, Node(4, None, None), None)), Node(10, Node(8, None, Node(9, None, None)), Node(12, None, None)))
        bintree1_res = Node(7, Node(5, Node(3, Node(2, None, None), None), Node(6, Node(4, None, None), None)), Node(10, Node(8, None, Node(9, None, None)), None))
        
        bintree2 = Node(5, Node(3, Node(2, None, None), None), Node(6, Node(4, None, None), None))
        bintree2_res = Node(5, Node(3, Node(2, None, None), None), Node(4, None, None))

        self.assertEqual(bintree1_res, rem_largest(bintree1))
        self.assertEqual(bintree2_res, rem_largest(bintree2))
    
    def test_delete(self):
        def less_than(x : int, y : int) -> bool:
            return x < y

        bintree = Node(7, Node(5, Node(3, Node(2, None, None), None), Node(6, Node(4, None, None), None)), Node(10, Node(8, None, Node(9, None, None)), Node(12, None, None)))

        bintree_rem2 = Node(7, Node(5, Node(3, None, None), Node(6, Node(4, None, None), None)), Node(10, Node(8, None, Node(9, None, None)), Node(12, None, None)))
        bintree_rem7 = Node(6, Node(5, Node(3, Node(2, None, None), None), Node(4, None, None)), Node(10, Node(8, None, Node(9, None, None)), Node(12, None, None)))
        bintree_rem10 = Node(7, Node(5, Node(3, Node(2, None, None), None), Node(6, Node(4, None, None), None)), Node(9, Node(8, None, None), Node(12, None, None)))

        self.assertEqual(BinarySearchTree(less_than, bintree_rem2), delete(BinarySearchTree(less_than, bintree), 2))
        self.assertEqual(BinarySearchTree(less_than, bintree_rem7), delete(BinarySearchTree(less_than, bintree), 7))
        self.assertEqual(BinarySearchTree(less_than, bintree_rem10), delete(BinarySearchTree(less_than, bintree), 10))

if (__name__ == '__main__'):
    unittest.main()

