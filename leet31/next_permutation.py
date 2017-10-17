def reverse(nums, start_idx, end_idx):
    d = end_idx - start_idx + 1
    for i in range(0, d//2):
        temp = nums[start_idx + i]
        nums[start_idx + i] = nums[end_idx - i]
        nums[end_idx - i] = temp

class Solution(object):
    def nextPermutation(self, nums):
        """
        Explaination:
        The last element in a permutation ordered lexographically will be a list in descending
        order based on the elements that appear in the list.
        From that we can say that from the end of the list, any sublist that is ordered in descending
        order is the largest list that can appear up to that point.
        From that fact - we can look for the 
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        s = 0
        idx = len(nums) - 1
        is_reversed = True
        while 0 < idx:
            if nums[idx-1] < nums[idx]:
                s = idx-1
                is_reversed = False
                break
            idx -= 1
        if is_reversed:
            nums.reverse()
            return
        swap_idx = s
        i = s
        while i < len(nums):
            if nums[s] < nums[i]:
                swap_idx = i
            i += 1
        temp = nums[swap_idx]
        nums[swap_idx] = nums[s]
        nums[s] = temp
        reverse(nums, s+1, len(nums) - 1)

def test():
    solution = Solution()
    example4 = [1,2,4,3]
    solution.nextPermutation(example4)
    assert(example4 == [1,3,2,4])
    example1 = [1,2,3]
    solution.nextPermutation(example1)
    assert(example1 == [1,3,2])
    example2 = [3,2,1]
    solution.nextPermutation(example2) 
    assert(example2 == [1,2,3])
    # [0, 0, 1]
    # [0, 1, 0]
    example3 = [1,1,5]
    solution.nextPermutation(example3)
    assert(example3 == [1,5,1])
    example5 = [5,4,7,5,3,2]
    solution.nextPermutation(example5)
    assert(example5 == [5,5,2,3,4,7])
    example6 = [1,3,2]
    solution.nextPermutation(example6)
    assert(example6 == [2,1,3])
