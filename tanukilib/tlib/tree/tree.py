from __future__ import annotations
from typing import TypeVar, Optional, List

T = TypeVar("T")

class BinaryTreeNode:
    def __init__(self, 
                v:Optional[T], 
                left:Optional[BinaryTreeNode] = None, 
                right:Optional[BinaryTreeNode] = None):
        self.value = v
        self.left = left
        self.right = right

def add(n:BinaryTreeNode, v:T) -> None:
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

def trav_preorder(n:BinaryTreeNode, buf:List[T], verbose:bool = True) -> None:
    if verbose:
        print(n.value)
    buf.append(n.value)
    if n.left is not None:
        trav_preorder(n.left, buf, verbose)
    if n.right is not None:
        trav_preorder(n.right, buf, verbose)

def trav_inorder(n:BinaryTreeNode, buf:List[T], verbose:bool = True) -> List[T]:
    if n.left is not None:
        trav_inorder(n.left, buf, verbose)
    if verbose:
        print(n.value)
    buf.append(n.value)
    if n.right is not None:
        trav_inorder(n.right, buf, verbose)

def trav_postorder(n:BinaryTreeNode, buf:List[T], verbose = True) -> List[T]:
    if n.left is not None:
        trav_postorder(n.left, buf, verbose)
    if n.right is not None:
        trav_postorder(n.right, buf, verbose)
    if verbose:
        print(n.value)
    buf.append(n.value)
