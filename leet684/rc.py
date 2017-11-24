"""
This question is kind of dumb. Very specific to the type of method you use.
"""

from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        explored = set()
        answers = set()
        stack = [1]
        while stack:
            x = stack.pop()
            for n in graph[x]:
                if n in explored:
                    answers.add((min(x, n), max(x, n)))
                else:
                    stack.append(n)
            explored.add(x)
        for edge in reversed(edges):
            t = tuple(sorted(edge))
            if t in answers:
                return list(t)

def test():
    solution = Solution()
    example1 = [[1,2], [1,3], [2,3]]
    print(solution.findRedundantConnection(example1))
    example2 = [[1,2], [2,3], [3,4], [1,4], [1,5]]
    print(solution.findRedundantConnection(example2))

if __name__ == '__main__':
    test()  