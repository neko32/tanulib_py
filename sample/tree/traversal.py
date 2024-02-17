from tlib.tree import *

def main():
    r = BinaryTreeNode(1)
    for v in range(2, 11):
        add(r, v)

    buf = []
    trav_preorder(r, buf)
    print(buf)

if __name__ == "__main__":
    main()
