""""
Breadth First Search (BFS)
"""

import os
import sys
import queue
import numpy as np
import random

from lib.node import Node


class BFSNode(Node):
    def __init__(self, val, children=None):
        super().__init__(val, children)
        self._visited = False

    def visit():
        self._visited = True

    def visited():
        return self._visited


def bfs_search(root: Node):
    if root is None:
        return

    queue = queue.Queue()  # FIFO (First In First Out)
    queue.put(root)  # add to end of queue

    while q.empty():
        node = queue.get()  # get first item for queue
        for child in node.children:
            if child.visited():
                child.visit()
                queue.put(child)


def create_random_weights_tree(tree_size):
    """
    Creates a balanced tree structure of `tree_size` elements; inits each node
    with a random value between 0 and 1, and returns the root_node of the tree.
    """
    root_node = BFSNode(random.random())
    bottom_nodes = [
        root_node,
    ]  # holds nodes located at bottom of the tree
    nodes_count = 1  # counts total number of nodes in the tree
    while nodes_count < tree_size:
        next_bottom_nodes = []
        # iterate through bottom tree nodes
        for node in bottom_nodes:
            if nodes_count + 2 > tree_size:
                # put in a last single node
                child = BFSNode(random.random())
                node.children.append(child)
                next_bottom_nodes.append(child)
                nodes_count += 1
                break
            else:
                # add 2 children nodes
                children = [BFSNode(random.random()), BFSNode(random.random())]
                node.children.extend(children)
                next_bottom_nodes.extend(children)
                nodes_count += 2
        bottom_nodes = next_bottom_nodes
    return root_node


def print_tree(root: Node, max_depth=10):
    iter_count = 0
    bottom_nodes = [
        root,
    ]
    while iter_count < max_depth:
        line = []
        next_bottom_nodes = []
        for node in bottom_nodes:
            line.append("{:.3f}".format(node.val))
            next_bottom_nodes.extend(node.children)

        iter_count += 1
        if len(next_bottom_nodes) ==  0:
            break

        bottom_nodes = next_bottom_nodes
        print(" ".join(line))


if __name__ == "__main__":
    random.seed(1)
    root = create_random_weights_tree(100)
    print_tree(root, max_depth=10)
