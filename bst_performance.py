import sys
import time
import random
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

from bst import *

# returns True if the first value is less than the second
def num_ord(x : float, y : float) -> bool:
    return x < y

# generates a binary search tree if the specified length with random float values between 0 and 1
def gen_tree(n : int) -> BinarySearchTree:
    rand_nums = [random.random() for _ in range(n)]
    bst = BinarySearchTree(num_ord, None)
    for num in rand_nums:
        bst = insert(bst, num)
    return bst

bst_100K = gen_tree(100000)
bst_200K = gen_tree(200000)
bst_300K = gen_tree(300000)
bst_400K = gen_tree(400000)
bst_500K = gen_tree(500000)
bst_600K = gen_tree(600000)
bst_700K = gen_tree(700000)
bst_800K = gen_tree(800000)
bst_900K = gen_tree(900000)
bst_1M = gen_tree(1000000)

bst_array = [bst_100K, bst_200K, bst_300K, bst_400K, bst_500K, bst_600K, bst_700K, bst_800K, bst_900K, bst_1M]

# returns the average time of a function on a binary tree out of 10 runs
def avg_time(bst_array : list, func : Callable[BinarySearchTree, any]) -> Union[BinarySearchTree, bool]:
    for tree in bst_array:
        times = []
        for i in range(10):
            start = time.perf_counter()
            func(tree, random.random())
            end = time.perf_counter()
            times.append(end - start)
            i += 1
        print(sum(times)/10)
    return

print('Average Running Times for insert()')
avg_time(bst_array, insert)

print('Average Running Times for lookup()')
avg_time(bst_array, lookup)