# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # table[i][j] represents all possible trees
        # that can be constructed from i to j
        table = [[None for i in range(n+1)] for j in range(n+1)]
        if n == 0:
            return None
        if n == 1:
            return TreeNode(1)
        # Construct the diagonal of the tree nodes
        for i in range(1, n+1):
            table[i][i] = [TreeNode(i)]
            table[0][i] = [TreeNode(i)]
            table[i][0] = [TreeNode(i)]
        for i in range(2, n+1):
            for j in range(1, n-i+1):
                nodes = []
                # Find the center nodes
                for k in range(0, i):
                    node = TreeNode(j+k)
                    if 0 < k:
                        node.left = table[j][j+k-1]
                    if j+k <= j+i:
                        node.right = table[j+k+1][j+i]
                    nodes.append(node)
                table[j][j+i] = nodes
        import pprint; 
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(table)
        return table[1][n]


if __name__ == "__main__":
    solver = Solution()
    assert(len(solver.generateTrees(2)) == 2)
    assert(len(solver.generateTrees(3)) == 5)
    assert(len(solver.generateTrees(4)) == 14)
