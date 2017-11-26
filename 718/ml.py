class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        d = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    d[j][i] = 1 + d[j-1][i-1]
        return max(max(row) for row in d)


def test():
    solver = Solution()
    test_input_1 = [
        [1,2,3,2,1],
        [3,2,1,4,7],
    ]
    print(solver.findLength(*test_input_1))
    test_input_2 = [
        [1,2,2,3],
        [2,2,1,3],
    ]
    print(solver.findLength(*test_input_2))
    test_input_3 = [
        [1,2,3],
        [1,2],
    ]
    print(solver.findLength(*test_input_3))
    


if __name__ == "__main__": test()
