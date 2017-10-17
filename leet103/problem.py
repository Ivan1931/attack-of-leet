from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        queue = deque([root, 1])
        level = []
        levels = [[root.val]]
        reverse = True
        while len(queue) != 0:
            node = queue.popleft()
            if node == 1:
                if len(queue) != 0:
                    queue.append(1)
                    if reverse:
                        level.reverse()
                        reverse = False
                    else:
                        reverse = True
                    levels.append(level)
                    level = []
            else:
                if node.left:
                    level.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    level.append(node.right.val)
                    queue.append(node.right)
        return levels
