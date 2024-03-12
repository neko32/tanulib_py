from unittest import TestCase, main
from tlib.tree import *


class TreeTest(TestCase):

    def test_trav_preorder(self):

        root = BinaryTreeNode(v=1)
        buf = []
        for i in range(2, 11):
            add(root, i)
        trav_preorder(root, buf, verbose=False)
        self.assertListEqual(buf, [i for i in range(1, 11)])

    def test_trav_inorder(self):

        root = BinaryTreeNode(v=50)
        buf = []
        ipts = [50, 12, 39, 72, 4, 58, 60, 120, 37, 51, 60, 1, 100]
        [add(root, ipt) for ipt in ipts[1:]]
        trav_inorder(root, buf, verbose=False)
        self.assertListEqual(buf, sorted(ipts))

    def test_trav_postorder(self):

        root = BinaryTreeNode(v=50)
        buf = []
        ipts = [50, 30, 70, 40, 100, 60, 80, 20, 10, 120, 110]
        [add(root, ipt) for ipt in ipts[1:]]
        trav_postorder(root, buf, verbose=False)
        expected = [10, 20, 40, 30, 60, 80, 110, 120, 100, 70, 50]
        self.assertListEqual(buf, expected)

    def test_nonbst(self):

        root = build_non_bst_tree(
            [
                ("", 1),
                ("ls", 2),
                ("lmls", 3),
                ("lmlmls", 4),
                ("lmlmlmls", 5),
                ("rs", 6),
                ("rmrs", 7),
                ("rmrmrs", 8),
                ("lmrs", 9),
                ("lmlmrs", 10),
                ("rmls", 11),
                ("rmrmls", 12),
                ("rmrmlmrs", 13)
            ]
        )

        buf = []
        trav_preorder(root, buf, True)
        print(buf)


if __name__ == "__main__":
    main()
