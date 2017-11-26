class Solution:
    def findDuplicates(self, nums):
        """
        Walk through ever item in the list.
        If the item that is in its proper place is not equal to the item
        Then it must be a duplicate
        :type nums: List[int]
        :rtype: List[int]
        """
        dups = []
        for i in range(len(nums)):
            a = nums[i]
            if a < 0:
                a = -a
            if nums[a-1] < 0:
                dups.append(a)
            else:
                nums[a-1] = -nums[a-1]
        return dups


def test():
    solution = Solution()
    test_1 = [4,3,2,7,8,2,3,1]
    print(solution.findDuplicates(test_1))


if __name__ == '__main__':
   test()
