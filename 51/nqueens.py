def left(n, placements, i):
    for p in reversed(placements):
        i -= 1
        if p == i:
            return True
        if i == 0:
            break
    return False

def right(n, placements, i):
    for p in reversed(placements):
        i += 1
        if p == i:
            return True
        if i == n-1:
            break
    return False

def valid_placements(n, placements):
    valids = []
    for i in range(n):
        if i not in placements:
            if not left(n, placements, i):
                if not right(n, placements, i):
                    valids.append(i)
    return valids


def stringify(n, solution):
    strings = []
    for x in solution:
        first_half = "." * x
        second_half = (n - x - 1) * "."
        line = first_half + "Q" + second_half
        strings.append(line)
    return strings


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n == 0:
            return [[]]
        solutions = [[i] for i in range(n)]
        for i in range(1, n):
            new_sols = []
            for sol in solutions:
                valids = valid_placements(n, sol)
                for v in valids:
                    new = sol[::]
                    new.append(v)
                    new_sols.append(new)
            solutions = new_sols
        return map(lambda sol: stringify(n, sol), solutions)


def test():
    solver = Solution()
    solutions = solver.solveNQueens(4)
    for sol in solutions:
        print("\n".join(sol))
        print("*" * 4)

if __name__ == "__main__":
    test()
