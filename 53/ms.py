class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = nums[0]
        current = nums[0]
        for n in nums:
            current = max(n, current + n)
            maximum = max(current, maximum)
        return maximum

if __name__ == "__main__":
    solver = Solution()
    assert(solver.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6)
