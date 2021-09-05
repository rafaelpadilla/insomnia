# https://leetcode.com/problems/search-in-a-binary-search-tree/

# You are given the root of a binary search tree (BST) and an integer val.
# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

from utils import BinaryTree as Tree


class Solution_1(object):
    def evaluate(self, root, val):

        if root.val == val:
            self.res = root
            return

        if root.left is not None:
            self.evaluate(root.left, val)
        if self.res is not None:
            return
        if root.right is not None:
            self.evaluate(root.right, val)

    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        self.res = None
        self.evaluate(root, val)
        return self.res


def test_func():
    test_cases = [{
        'input': {
            'root': Tree([4, 2, 7, 1, 3]).root,
            'val': 2
        },
        'output': Tree([2, 1, 3]).root
    }, {
        'input': {
            'root': Tree([4, 2, 7, 1, 3]).root,
            'val': 5
        },
        'output': Tree([]).root
    }]

    solution = Solution_1()

    for test_case in test_cases:
        assert solution.searchBST(**test_case['input']) == test_case['output']
