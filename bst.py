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
    val : any
    left : BinTree
    right : BinTree
    comes_before : Callable[[Node, Node], bool]

# Functions

def example_fun(x : int) -> bool:
    return x < 142

# Test Cases
