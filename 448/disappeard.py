class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for n in nums:
        	n = abs(n)
        	nums[n-1] = -abs(nums[n-1])
        missing = []
        for i, n in enumerate(nums):
        	if 0 < n:
        		missing.append(i+1)
        return missing

"""
[2,1,1,3]
[2,-1,1,3]
[-2,-1,1,3]
[-2,-1,1,3]
[-2,-1,-1,3] :)
"""

def test():
	solution = Solution()
	print(solution.findDisappearedNumbers([2,1,1,3]))

if __name__ == '__main__':
	test()