class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def traverse(duplicates, seen, node):
    if node is None:
        return "n"
    else:
        left = traverse(duplicates, seen, node.left)
        right = traverse(duplicates, seen, node.right)
        node_path = "{} {} {}".format(node.val, left, right)
        if node_path in seen:
            duplicates[node_path] = node
        else:
            seen.add(node_path)
        return node_path
            


class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        seen = set()
        duplicates = {}
        traverse(duplicates, seen, root)
        return list(duplicates.values())

