# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

from utils import BinaryTree as Tree


class Solution_1(object):
    # Solução utilizando uma função recursiva.
    def verify_node(self, node, k):
        return node.val in self.my_dict

    def evaluate_children(self, node, k):
        ret = 0
        ret += node.val in self.my_dict
        self.my_dict.append(k - node.val)

        if ret == 0 and node.left is not None:
            ret = self.evaluate_children(node.left, k)
        if ret == 0 and node.right is not None:
            ret = self.evaluate_children(node.right, k)
        return ret > 0

    def findTarget(self, root, k):
        self.my_dict = []
        return self.evaluate_children(root, k)


class Solution_2(object):
    # Solução loop.
    def findTarget(self, root, k):
        s = set()
        if root is None:
            return False
        bfs = [root]
        for i in bfs:
            if k - i.val in s:
                return True
            s.add(i.val)
            if i.left:
                bfs.append(i.left)
            if i.right:
                bfs.append(i.right)
        return False


from collections import deque

# https://www.geeksforgeeks.org/deque-in-python/


class Solution_3:
    def findTarget(self, root, k):
        s = set()
        q = deque()
        q.append(root)
        #when q has elements on it, it will return True; otherwise, it's false.
        while q:
            temp = q.popleft()
            if temp.val in s:
                return True
            s.add(k - temp.val)
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)
        return False


def test_func():
    test_cases = [{
        'input': {
            'root': Tree([5, 3, 6, 2, 4, None, 7]).root,
            'k': 9
        },
        'expected': True,
    }, {
        'input': {
            'root': Tree([5, 3, 6, 2, 4, None, 7]).root,
            'k': 28
        },
        'expected': False
    }, {
        'input': {
            'root': Tree([2, 1, 3]).root,
            'k': 4
        },
        'expected': True
    }, {
        'input': {
            'root': Tree([2, 1, 3]).root,
            'k': 1
        },
        'expected': False
    }, {
        'input': {
            'root': Tree([2, 1, 3]).root,
            'k': 3
        },
        'expected': True
    }]

    # solution = Solution_1()
    # solution = Solution_2()
    solution = Solution_3()

    for test_case in test_cases:
        assert solution.findTarget(**test_case['input']) == test_case['expected']
