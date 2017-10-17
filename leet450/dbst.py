class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return root
        if root.left is None and root.right is None:
            if root.val == key: return None
            return root
        node = root
        prev = None
        found = False
        went_left = False
        while not found and node is not None:
            if key < node.val:
                prev = node
                node = node.left
                went_left = True
            elif key == node.val:
                found = True
            else:
                prev = node
                node = node.right
                went_left = False

        if not found:
            return root
        if node.left is None and node.right is None:
            if went_left:
                prev.left = None
            else:
                prev.right = None
            return root
        elif node.left is None and node.right:
            node.val = node.right.val
            node.left = node.right.left
            node.right = node.right.right
            return root
        elif node.right is None and node.left:
            node.val = node.left.val
            node.right = node.left.right
            node.left = node.left.left
            return root
        else: # Neither node is null
            # We must find the min value in the right subtree
            # Min right subtree is the left most item of the right subtree
            # By definition it can be a leaf or have a right child
            rightnode = node.right
            if rightnode.left is None and rightnode.right is None:
                node.val = rightnode.val
                node.right = None
            elif rightnode.left:
                min_subtree_node = rightnode.left
                previous = rightnode
                while min_subtree_node.left:
                    previous = min_subtree_node
                    min_subtree_node = min_subtree_node.left
                if min_subtree_node.right is None: # leaf node
                    node.val = min_subtree_node.val
                    previous.left = None
                else: # A right parent node
                    node.val = min_subtree_node.val
                    previous.left = min_subtree_node.right
            else: # Right node has only right subtree - cut and paste remove it
                node.val = rightnode.val
                node.right = rightnode.right
            return root
            


def mk_example1():
    tree = {}
    tree[(0, 0)] = TreeNode(5)
    ## First layer
    tree[(1, 0)] = TreeNode(3)
    tree[(1, 1)] = TreeNode(6)
    ## Second layer
    tree[(2, 0)] = TreeNode(2)
    tree[(2, 1)] = TreeNode(4)
    tree[(2, 2)] = TreeNode(7)
    ## root
    tree[(0,0)].left = tree[(1,0)]
    tree[(0,0)].right = tree[(1,1)]
    ## left child
    tree[(1,0)].left = tree[(2,0)]
    tree[(1,0)].right = tree[(2,1)]
    ## right child
    tree[(1,1)].right = tree[(2,2)]

    return tree[(0,0)]

def mk_example2():
    root = TreeNode(1)
    root.right = TreeNode(2)
    return root

def test():
    solver = Solution()
    example1 = mk_example1()
    solver.deleteNode(example1, 3)
    # import ipdb ; ipdb.set_trace()
    example2 = mk_example2()
    solver.deleteNode(example2, 2)
    return example1, example2

if __name__ == "__main__":
    test()

