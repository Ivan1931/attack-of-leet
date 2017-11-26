import pprint

pp = pprint.PrettyPrinter(indent=4)

class Solution:
    def minDistance(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        d = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]

        for j in range(len(A)+1): d[0][j] = j
        for i in range(len(B)+1): d[i][0] = i


        for i in range(1, len(B)+1):
            for j in range(1, len(A)+1):
                m = min(
                    d[i-1][j-1], # edit
                    d[i][j-1], # insert into A
                    d[i-1][j] # insert into B
                )
                if B[i-1] == A[j-1]: # characters are equal so do nothing
                    d[i][j] = d[i-1][j-1]
                else: # otherwise if they are different we need to make an edit at this point
                    d[i][j] = 1 + m
        return d[len(B)][len(A)]

def test():
    solution = Solution()
    test_1 = ["word1", "word2"]
    print(solution.minDistance(*test_1), "= 1")
    test_2 = ["word2", "sword1"]
    print(solution.minDistance(*test_2), "= 2")
    test_3 = ["word", ""]
    print(solution.minDistance(*test_3), "= 4")
    test_4 = ["aabaa", "aaaaaa"]
    print(solution.minDistance(*test_4), "= 2")

if __name__ == "__main__": test()
