def in_board(board, position):
    height = len(board)
    width = len(board[0])
    y, x = position
    return 0 <= y < height and 0 <= x < width

def search(board, word, start, disallowed):
    y, x = start
    if len(word) == 0:
        return True
    if len(word) == 1:
        return board[y][x] == word
    elif word[0] != board[y][x]:
        return False
    else:
        right = (y+1, x)
        left  = (y-1, x)
        up    = (y, x-1)
        down  = (y, x+1) 
        disallowed.add(start)
        for direction in [left, right, up, down]:
            if direction not in disallowed and in_board(board, direction):
                if search(board, word[1:], direction, disallowed):
                    return True
        disallowed.remove(start)
        return False


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return True
        if len(board) == 0 or len(board[0]) == 0:
            return False
        for y in range(len(board)):
            for x in range(len(board[y])):
                if word[0] == board[y][x]:
                    if search(board, word, (y, x), set()):
                        return True
        return False


def make_board():
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    return board

def test():
    solution = Solution()
    # board = make_board()
    # assert(solution.exist(board, "ABCCED"))
    # assert(solution.exist(board, "SEE"))
    # assert(not solution.exist(board, "ABCB"))
    # trivial_case = [["a"]]
    # assert(solution.exist(trivial_case, "a"))
    non_trivial_case = [["a", "a"]]
    assert(solution.exist(non_trivial_case, "aa"))
    
if __name__ == "__main__":
    test()
