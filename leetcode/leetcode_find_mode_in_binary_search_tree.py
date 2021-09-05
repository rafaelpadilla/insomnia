# https://leetcode.com/problems/find-mode-in-binary-search-tree/

# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it. If the tree has more than one mode, return them in any order.
# Assume a BST is defined as follows:
# * The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# * The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# * Both the left and right subtrees must also be binary search trees.

from utils2 import BinaryTree as Tree

# from utils import BinaryTree as Tree


class Solution_1(object):
    # Solução utilizando uma função recursiva.
    def evaluate(self, root):
        if root.val is not None:
            if root.val not in self.amounts:
                self.amounts[root.val] = 1
            else:
                self.amounts[root.val] += 1

            if self.amounts[root.val] >= self.max:
                self.max = self.amounts[root.val]

        if root.left is not None:
            self.evaluate(root.left)
        if root.right is not None:
            self.evaluate(root.right)

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.amounts = {}
        self.max = 0
        self.evaluate(root)
        return [k for k, v in self.amounts.items() if v == self.max]


def test_func():
    test_cases = [{
        'input': {
            'root': Tree([1, None, 2, 2]).root,
        },
        'output': [2]
    }, {
        'input': {
            'root': Tree([0]).root,
        },
        'output': [0]
    }, {
        'input': {
            'root': Tree([1, None, 2]).root,
        },
        'output': [1, 2]
    }]

    solution = Solution_1()

    for test_case in test_cases:
        assert solution.findMode(**test_case['input']) == test_case['output']
