from functools import reduce
import sys

def product(nums):
    return reduce(lambda a, b: a * b, nums, 1)

def max_product(nums):
    if len(nums) == 0: return -sys.maxsize
    if len(nums) == 1: return nums[0]
    negatives = [i for i in range(len(nums)) if nums[i] < 0]
    if len(negatives) % 2 == 0:
        return product(nums)
    else:
        if len(negatives) == 1:
            idx = min(negatives[0]+1, len(nums) - 1)
            return max(product(nums[0:negatives[0]]), product(nums[idx:]))
        else:
            first = min(negatives[0]+1, len(nums) - 1)
            last = negatives[-1]
            return max(product(nums[0:last]), product(nums[first:]))

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return None
        if len(nums) == 1: return nums[0]
        zeros = []
        current = []
        for n in nums:
            if n != 0:
                current.append(n)
            else:
                zeros.append(current)
                zeros.append([0])
                current = []
        zeros.append(current)
        products = list(map(max_product, zeros))
        return max(products)


if __name__ == "__main__":
    solver = Solution()
    assert(solver.maxProduct([2,3,-2,4]) == 6)
    assert(solver.maxProduct([2,-2, 3,-2,4, -3]) == 96)
    assert(solver.maxProduct([2, 0]) == 2)
    assert(solver.maxProduct([0]) == 0)
    assert(solver.maxProduct([-2, 0, -1]) == 0)
