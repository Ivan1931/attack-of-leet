import json

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "[]"
        val = str(root.val)
        if root.left is None and root.right is None:
            return val
        else:
            left = self.serialize(root.left)
            right = self.serialize(root.right)
            return "[{},{},{}]".format(val, left, right)

    def deserialise_helper(self, data):
        if type(data) == int:
            return TreeNode(data)
        if len(data) == 0:
            return None
        else:
            new_node = TreeNode(data[0])
            new_node.left = self.deserialise_helper(data[1])
            new_node.right = self.deserialise_helper(data[2])
            return new_node


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = json.loads(data)
        return self.deserialise_helper(data)

        
