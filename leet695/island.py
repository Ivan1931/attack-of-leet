def get(grid, i, j):
    width = len(grid)
    height = len(grid[0])
    if 0 <= i < width and 0 <= j < height:
        return grid[i][j]
    else:
        return None

def fanout(grid, i, j, visited):
    stack = [(i, j)]
    area = 0
    old_visited = len(visited)
    while 0 < len(stack):
        i, j = stack.pop()
        visited.add((i,j))
        potential = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        for x, y in potential:
            if (x, y) not in visited and get(grid, x, y) == 1:
                stack.append((x, y))
    return len(visited) - old_visited

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        max_area = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if (i, j) not in visited and val == 1:
                    area = fanout(grid, i, j, visited)
                    max_area = max(area, max_area)
        return max_area

def test():
    solver = Solution()

    test_1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
              [0,0,0,0,0,0,0,1,1,1,0,0,0],
              [0,1,1,0,1,0,0,0,0,0,0,0,0],
              [0,1,0,0,1,1,0,0,1,0,1,0,0],
              [0,1,0,0,1,1,0,0,1,1,1,0,0],
              [0,0,0,0,0,0,0,0,0,0,1,0,0],
              [0,0,0,0,0,0,0,1,1,1,0,0,0],
              [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(solver.maxAreaOfIsland(test_1) == 6)


if __name__ == "__main__":
    test()
