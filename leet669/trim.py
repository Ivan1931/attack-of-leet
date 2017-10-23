def trim(node, L, R):
    if node.val < L:
        if node.right:
            return trim(node.right, L, R)
        else:
            return None
    elif R < node.val:
        if node.left:
            return trim(node.left, L, R)
        else:
            return None
    else:
        if node.left:
            node.left = trim(node.left, L, R)
        if node.right:
            node.right = trim(node.right, L, R)
        return node

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root is not None:
            return trim(root, L, R)
        else:
            return None
