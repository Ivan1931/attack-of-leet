class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return n
        table = [1 for i in range(n+1)]
        table[2] = 2
        for i in range(3, n+1):
            total = 0
            for j in range(0, i):
                total += table[i - j - 1] * table[j]
            table[i] = total
        return table[n]

if __name__ == "__main__":
    solver = Solution()
    assert(solver.numTrees(3) == 5)
    assert(solver.numTrees(4) == 14)
    assert(solver.numTrees(6) == 132)
