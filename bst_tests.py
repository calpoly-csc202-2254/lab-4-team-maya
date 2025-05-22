import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

from bst import *

# Data Definitions

@dataclass
class XYCoords:
    x : float
    y : float

def num_ord(x : float, y : float) -> bool:
    return x < y

def str_ord(a : str, b : str) -> bool:
    return a < b

def euc_dist(c : XYCoords) -> float:
    return ((c.x ** 2) + (c.y ** 2)) ** (0.5)

def dist_ord(c1 : XYCoords, c2 : XYCoords) -> bool:
    return euc_dist(c1) < euc_dist(c2)

# Test Cases

class BSTTests(unittest.TestCase):
    def test_is_empty(self):
        nbst_empty = BinarySearchTree(num_ord, None)
        nbst_nonempty = BinarySearchTree(num_ord, Node(1, None, Node(2, None, None)))

        self.assertTrue(is_empty(nbst_empty))
        self.assertFalse(is_empty(nbst_nonempty))

        sbst_empty = BinarySearchTree(str_ord, None)
        sbst_nonempty = BinarySearchTree(str_ord, Node('a', None, Node('b', None, None)))

        self.assertTrue(is_empty(sbst_empty))
        self.assertFalse(is_empty(sbst_nonempty))

        cbst_empty = BinarySearchTree(dist_ord, None)
        cbst_nonempty = BinarySearchTree(dist_ord, Node(XYCoords(3, 4), None, Node(XYCoords(10, 8), None, None)))

        self.assertTrue(is_empty(cbst_empty))
        self.assertFalse(is_empty(cbst_nonempty))
    
    def test_insert(self):
        num_bstree_none = BinarySearchTree(num_ord, None)
        num_bstree = BinarySearchTree(num_ord, Node(1, None, Node(3, None, None)))

        num_bstree_none_result = BinarySearchTree(num_ord, Node(0, None, None))
        bstree_0_result = BinarySearchTree(num_ord, Node(1, Node(0, None, None), Node(3, None, None)))
        bstree_2_result = BinarySearchTree(num_ord, Node(1, None, Node(3, Node(2, None, None), None)))
        bstree_4_result = BinarySearchTree(num_ord, Node(1, None, Node(3, None, Node(4, None, None))))

        self.assertEqual(num_bstree_none_result, insert(num_bstree_none, 0))
        self.assertEqual(bstree_0_result, insert(num_bstree, 0))
        self.assertEqual(bstree_2_result, insert(num_bstree, 2))
        self.assertEqual(bstree_4_result, insert(num_bstree, 4))

        str_bstree_none = BinarySearchTree(str_ord, None)
        str_bstree = BinarySearchTree(str_ord, Node('acdfev', None, Node('dog', None, None)))

        str_bstree_none_result = BinarySearchTree(str_ord, Node('abc', None, None))
        bstree_abc_result = BinarySearchTree(str_ord, Node('acdfev', Node('abc', None, None), Node('dog', None, None)))
        bstree_bigger_result = BinarySearchTree(str_ord, Node('acdfev', None, Node('dog', Node('bigger', None, None), None)))
        bstree_zebra_result = BinarySearchTree(str_ord, Node('acdfev', None, Node('dog', None, Node('zebra', None, None))))

        self.assertEqual(str_bstree_none_result, insert(str_bstree_none, 'abc'))
        self.assertEqual(bstree_abc_result, insert(str_bstree, 'abc'))
        self.assertEqual(bstree_bigger_result, insert(str_bstree, 'bigger'))
        self.assertEqual(bstree_zebra_result, insert(str_bstree, 'zebra'))

        dist_bstree_none = BinarySearchTree(dist_ord, None)
        dist_bstree = BinarySearchTree(dist_ord, Node(XYCoords(-2, 3), None, Node(XYCoords(-5, -5), None, None)))

        dist_bstree_none_result = BinarySearchTree(dist_ord, Node(XYCoords(1, -1), None, None))
        bstree_result1 = BinarySearchTree(dist_ord, Node(XYCoords(-2, 3), Node(XYCoords(1, -1), None, None), Node(XYCoords(-5, -5), None, None)))
        bstree_result2 = BinarySearchTree(dist_ord, Node(XYCoords(-2, 3), None, Node(XYCoords(-5, -5), Node(XYCoords(4, 3), None, None), None)))
        bstree_result3 = BinarySearchTree(dist_ord, Node(XYCoords(-2, 3), None, Node(XYCoords(-5, -5), None, Node(XYCoords(-10, 12), None, None))))

        self.assertEqual(dist_bstree_none_result, insert(dist_bstree_none, XYCoords(1, -1)))
        self.assertEqual(bstree_result1, insert(dist_bstree, XYCoords(1, -1)))
        self.assertEqual(bstree_result2, insert(dist_bstree, XYCoords(4, 3)))
        self.assertEqual(bstree_result3, insert(dist_bstree, XYCoords(-10, 12)))
    
    def test_lookup(self):
        num_bstree = BinarySearchTree(num_ord, Node(1, None, Node(3, None, Node(4, None, None))))
        str_bstree = BinarySearchTree(str_ord, Node('acdfev', None, Node('dog', None, None)))
        dist_bstree = BinarySearchTree(dist_ord, Node(XYCoords(-2, 3), None, Node(XYCoords(-5, -5), None, None)))

        self.assertTrue(lookup(num_bstree, 1))
        self.assertFalse(lookup(num_bstree, 0))

        self.assertTrue(lookup(str_bstree, 'dog'))
        self.assertFalse(lookup(str_bstree, 'cat'))

        self.assertTrue(lookup(dist_bstree, XYCoords(-2, 3)))
        self.assertFalse(lookup(dist_bstree, XYCoords(1, 1)))
    
    def test_largest(self):
        num_bintree = Node(7, Node(5, Node(3, Node(2, None, None), None), Node(6, Node(4, None, None), None)), Node(10, Node(8, None, Node(9, None, None)), Node(12, None, None)))
        str_bintree = Node('food', Node('dog', Node('bingo', Node('apple', None, None), None), Node('ear', Node('cat', None, None), None)), Node('yellow', Node('georgia', None, Node('lemon', None, None)), Node('zebra', None, None)))
        dist_bintree = Node(XYCoords(6, 8), Node(XYCoords(-5, 4), Node(XYCoords(-2, 1), Node(XYCoords(1, -1), None, None), None), Node(XYCoords(-7, -6), Node(XYCoords(3, 4), None, None), None)), Node(XYCoords(-20, -25), Node(XYCoords(10, -11), None, Node(XYCoords(15, 14), None, None)), Node(XYCoords(100, -50), None, None)))

        self.assertEqual(12, largest(num_bintree))
        self.assertEqual('zebra', largest(str_bintree))
        self.assertEqual(XYCoords(100, -50), largest(dist_bintree))
    
    def test_rem_largest(self):
        num_bintree = Node(7, Node(5, Node(3, Node(2, None, None), None), Node(6, Node(4, None, None), None)), Node(10, Node(8, None, Node(9, None, None)), Node(12, None, None)))
        str_bintree = Node('food', Node('dog', Node('bingo', Node('apple', None, None), None), Node('ear', Node('cat', None, None), None)), Node('yellow', Node('georgia', None, Node('lemon', None, None)), Node('zebra', None, None)))
        dist_bintree = Node(XYCoords(6, 8), Node(XYCoords(-5, 4), Node(XYCoords(-2, 1), Node(XYCoords(1, -1), None, None), None), Node(XYCoords(-7, -6), Node(XYCoords(3, 4), None, None), None)), Node(XYCoords(-20, -25), Node(XYCoords(10, -11), None, Node(XYCoords(15, 14), None, None)), Node(XYCoords(100, -50), None, None)))

        num_bintree_res = Node(7, Node(5, Node(3, Node(2, None, None), None), Node(6, Node(4, None, None), None)), Node(10, Node(8, None, Node(9, None, None)), None))
        str_bintree_res = Node('food', Node('dog', Node('bingo', Node('apple', None, None), None), Node('ear', Node('cat', None, None), None)), Node('yellow', Node('georgia', None, Node('lemon', None, None)), None))
        dist_bintree_res = Node(XYCoords(6, 8), Node(XYCoords(-5, 4), Node(XYCoords(-2, 1), Node(XYCoords(1, -1), None, None), None), Node(XYCoords(-7, -6), Node(XYCoords(3, 4), None, None), None)), Node(XYCoords(-20, -25), Node(XYCoords(10, -11), None, Node(XYCoords(15, 14), None, None)), None))

        self.assertEqual(num_bintree_res, rem_largest(num_bintree))
        self.assertEqual(str_bintree_res, rem_largest(str_bintree))
        self.assertEqual(dist_bintree_res, rem_largest(dist_bintree))
    
    def test_delete(self):
        num_bintree = Node(7, Node(5, Node(3, Node(2, None, None), None), Node(6, Node(4, None, None), None)), Node(10, Node(8, None, Node(9, None, None)), Node(12, None, None)))
        str_bintree = Node('food', Node('dog', Node('bingo', Node('apple', None, None), None), Node('ear', Node('cat', None, None), None)), Node('yellow', Node('georgia', None, Node('lemon', None, None)), Node('zebra', None, None)))
        dist_bintree = Node(XYCoords(6, 8), Node(XYCoords(-5, 4), Node(XYCoords(-2, 1), Node(XYCoords(1, -1), None, None), None), Node(XYCoords(-7, -6), Node(XYCoords(3, 4), None, None), None)), Node(XYCoords(-20, -25), Node(XYCoords(10, -11), None, Node(XYCoords(15, 14), None, None)), Node(XYCoords(100, -50), None, None)))

        num_bintree_res = Node(6, Node(5, Node(3, Node(2, None, None), None), Node(4, None, None)), Node(10, Node(8, None, Node(9, None, None)), Node(12, None, None)))
        str_bintree_res = Node('food', Node('dog', Node('apple', None, None), Node('ear', Node('cat', None, None), None)), Node('yellow', Node('georgia', None, Node('lemon', None, None)), Node('zebra', None, None)))
        dist_bintree_res = Node(XYCoords(6, 8), Node(XYCoords(-5, 4), Node(XYCoords(-2, 1), Node(XYCoords(1, -1), None, None), None), Node(XYCoords(-7, -6), Node(XYCoords(3, 4), None, None), None)), Node(XYCoords(-20, -25), Node(XYCoords(15, 14), None, None), Node(XYCoords(100, -50), None, None)))

        self.assertEqual(BinarySearchTree(num_ord, num_bintree_res), delete(BinarySearchTree(num_ord, num_bintree), 7))
        self.assertEqual(BinarySearchTree(str_ord, str_bintree_res), delete(BinarySearchTree(str_ord, str_bintree), 'bingo'))
        self.assertEqual(BinarySearchTree(dist_ord, dist_bintree_res), delete(BinarySearchTree(dist_ord, dist_bintree), XYCoords(10, -11)))


if (__name__ == '__main__'):
    unittest.main()
