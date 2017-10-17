from collections import defaultdict


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 2:
            return []
        cache = defaultdict(list)
        for idx, i in enumerate(nums):
            for jdx, j in enumerate(nums):
                if idx != jdx:
                    cache[i + j].append((idx, jdx))
        found = set()
        for idx, n in enumerate(nums):
            if -n in cache:
                matches = cache[-n]
                for adx, bdx in matches:
                    if adx != idx and bdx != idx:
                        x = [nums[idx], nums[adx], nums[bdx]]
                        x.sort()
                        a, b, c = x
                        found.add((a, b, c))
        found = list(found)
        return list(map(list, found))


def test():
    solution = Solution()
    test_input = [-1, 0, 1, 2, -1, -4]
    result = solution.threeSum(test_input)
    print(result)
    test_input = [0, 0, 0]
    result = solution.threeSum(test_input)
    print(result)


if __name__ == "__main__":
    test()
