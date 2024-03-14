from __future__ import annotations
from typing import TypeVar, Optional, List, Tuple
from enum import Enum, auto

T = TypeVar("T")


class NodeInsertSide(Enum):
    """Which side of BTree to insert"""
    SIDE_LEFT = auto()
    SIDE_RIGHT = auto()


class BinaryTreeNode:
    """Represents a node in Binary Tree"""
    def __init__(
            self,
            v: Optional[T],
            left: Optional[BinaryTreeNode] = None,
            right: Optional[BinaryTreeNode] = None
    ):
        self.value = v
        self.left = left
        self.right = right


def add(n: BinaryTreeNode, v: T) -> None:
    """add a node in BST manner"""
    new_n = BinaryTreeNode(v)
    if v < n.value:
        if n.left is None:
            n.left = new_n
        else:
            add(n.left, v)
    else:
        if n.right is None:
            n.right = new_n
        else:
            add(n.right, v)


def add_nonbst(n: BinaryTreeNode, v: T, side: NodeInsertSide) -> None:
    """Add a node in non-BST manner"""
    new_n = BinaryTreeNode(v)
    if side == NodeInsertSide.SIDE_LEFT:
        n.left = new_n
    else:
        n.right = new_n


def build_non_bst_tree(directions: List[Tuple[str, T]]) -> BinaryTreeNode:
    """Build non-BST Tree based on directions"""
    root = BinaryTreeNode(directions[0][1])
    for direction in directions[1:]:
        t = root
        (command, v) = direction
        print(f"executing command {command} for {v}..")
        idx = 0
        while idx < len(command):
            action = command[idx:idx + 2]
            print(f"action:{action}")
            if action == 'lm':
                print("going left..")
                t = t.left
            elif action == 'rm':
                print("going right..")
                t = t.right
            elif action == 'ls':
                print(f"set {v} to left..")
                new_n = BinaryTreeNode(v)
                t.left = new_n
            elif action == 'rs':
                print(f"set {v} to right..")
                new_n = BinaryTreeNode(v)
                t.right = new_n
            else:
                raise ValueError(f"unknown action {action}")

            idx += 2
        print(f"command {command} done.")
    return root


def trav_preorder(n: BinaryTreeNode, buf: List[T], verbose: bool = True) -> None:
    """Traverse the tree with preorder traversal"""
    if verbose:
        print(n.value)
    buf.append(n.value)
    if n.left is not None:
        trav_preorder(n.left, buf, verbose)
    if n.right is not None:
        trav_preorder(n.right, buf, verbose)


def trav_inorder(n: BinaryTreeNode, buf: List[T], verbose: bool = True) -> List[T]:
    """Traverse the tree with inorder traversal"""
    if n.left is not None:
        trav_inorder(n.left, buf, verbose)
    if verbose:
        print(n.value)
    buf.append(n.value)
    if n.right is not None:
        trav_inorder(n.right, buf, verbose)


def trav_postorder(n: BinaryTreeNode, buf: List[T], verbose=True) -> List[T]:
    """Traverse the tree with postorder traversal"""
    if n.left is not None:
        trav_postorder(n.left, buf, verbose)
    if n.right is not None:
        trav_postorder(n.right, buf, verbose)
    if verbose:
        print(n.value)
    buf.append(n.value)
