class Solution:
    def findNumberOfLIS(self, nums):
        """
        max(
            if i can be in current longest sequence:
                longest including i
            longest starting from i
        )
        
        :type nums: List[int]
        :rtype: int
        """
        d = [1 for i in range(len(nums))]
        c = [1 for i in range(len(nums))]
        result = 1
        max_len = 1
        for i, n in enumerate(nums):
            for j in range(i):
                if nums[j] < nums[i]:
                    if d[i] < d[i] + 1:
                        d[i] = d[j] + 1
                        c[i] = c[j]
                    elif d[j] + 1 == d[i]:
                        c[i] += c[j]
            max_len = max(max_len, d[i])
        res = 0
        for i, n in enumerate(d):
            if n == max_len:
                res += c[i]
        return res

def test():
    solver = Solution()
    test_1 = [1,3,5,4,7]
    print(solver.findNumberOfLIS(test_1), "= 2")
    test_2 = [2,2,2,2,2,2]
    print(solver.findNumberOfLIS(test_2), "= 6")
    test_3 = [1,3,5,4,7,8,2,3,4,5]
    print(solver.findNumberOfLIS(test_3), "= 3")


if __name__ == "__main__": test()

