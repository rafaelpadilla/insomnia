class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def to_array(self):
        ret = []
        nodes = [self]
        while (len(nodes) != 0):
            n = nodes.pop()
            if n is None:
                continue
            else:
                ret.append(n.val)
            if n.left is None and n.right is None:
                continue
            nodes.insert(0, n.left)
            nodes.insert(0, n.right)
        return ret

    def __str__(self):
        if self is None:
            return str([])
        return str(self.to_array())

    def __eq__(self, other):
        return str(self) == str(other)


class BinaryTree(object):
    '''Esta classe transforma um array em uma estrutura de árvore com objetos TreeNode'''
    def __init__(self, arr):
        self.arr = arr
        self.levels = self._create_levels(arr)

        if len(arr) == 0:
            self.root = None
        else:
            children = self.get_children(0)
            self.root = TreeNode(val=self.arr[0], right=children['right'], left=children['left'])

    def get_children(self, current_position):
        return {
            'left': self._get_node_left(current_position),
            'right': self._get_node_right(current_position)
        }

    def _get_node_left(self, current_position):
        position_left = self._get_pos_left_child(current_position)
        # It has no left child
        if position_left >= len(self.arr) or self.arr[position_left] is None:
            return None
        val_left = self.arr[position_left]
        return TreeNode(val=val_left,
                        right=self._get_node_right(position_left),
                        left=self._get_node_left(position_left))

    def _get_node_right(self, current_position):
        position_right = self._get_pos_right_child(current_position)
        # It has no right child
        if position_right >= len(self.arr) or self.arr[position_right] is None:
            return None
        val_right = self.arr[position_right]
        return TreeNode(val=val_right,
                        right=self._get_node_right(position_right),
                        left=self._get_node_left(position_right))

    def _get_pos_left_child(self, current_position):
        return (2 * current_position) + 1

    def _get_pos_right_child(self, current_position):
        return (2 * current_position) + 2

    def _create_levels(self, arr):
        levels = []
        for i, el in enumerate(arr):
            for _ in range(2**i):  # 2 ** i => math.pow(2, i)
                if len(levels) >= len(arr):
                    break
                levels.append(i)
        return levels
