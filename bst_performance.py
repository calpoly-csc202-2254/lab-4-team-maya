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

sizes = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]

# returns the average time of a function on a binary tree out of 5 runs
def avg_time(sizes : list, func : Callable[BinarySearchTree, any]) -> Union[BinarySearchTree, bool]:
    for size in sizes:
        times = []
        for i in range(5):
            bst = gen_tree(size)
            start = time.perf_counter()
            func(tree, random.random())
            end = time.perf_counter()
            times.append(end - start)
            i += 1
        print(sum(times)/5)
    return

print('Average Running Times for insert()')
avg_time(sizes, insert)

print('Average Running Times for lookup()')
avg_time(sizes, lookup)