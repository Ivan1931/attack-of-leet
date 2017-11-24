def dfs(root, n, level, levels):
    if root is None:
        return
    if level not in levels:
        levels[level] = (n, n)
    left, right = levels[level]
    left = min(n, left)
    right = max(n, right)
    levels[level] = (left, right)
    dfs(root.left, n * 2, level+1, levels)
    dfs(root.right, n * 2 + 1, level+1, levels)


class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        levels={}
        dfs(root, 0, 0, levels)
        return max(abs(x - y) for x, y in levels.values()) + 1
        