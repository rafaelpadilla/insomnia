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


test_cases = [{
    'inputs': {
        'root': Tree([4, 2, 7, 1, 3]).root,
        'val': 2
    },
    'expected': Tree([2, 1, 3]).root
}, {
    'inputs': {
        'root': Tree([4, 2, 7, 1, 3]).root,
        'val': 5
    },
    'expected': Tree([]).root
}]

solution = Solution_1()

for i, test_case in enumerate(test_cases):
    print(f'Test case {i+1}')
    ret = solution.searchBST(**test_case['inputs'])
    if ret == test_case['expected']:
        print('Passed')
    else:
        print('Failed!')
        print(f'Obtained: {ret} Expected: {test_case["expected"]}')
        break
