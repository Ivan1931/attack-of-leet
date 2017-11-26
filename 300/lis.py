class Solution(object):

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        di = [1 for i in nums]
        for i in range(len(nums)):
            n = nums[i]
            for j in range(i):
                if nums[j] < nums[i]:
                    di[i] = max(di[i], di[j] + 1)
        return max(di)


def test():
    solve = Solution()
    example1 = [10, 9, 2, 5, 3, 7, 101, 18]
    assert(solve.lengthOfLIS(example1) == 4)
    example2 = [0]
    assert(solve.lengthOfLIS(example2) == 1)
    example3 = [10, 9, 2, 5, 3, 4]
    assert(solve.lengthOfLIS(example3) == 3)

if __name__ == "__main__":
    test()
