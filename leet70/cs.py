def stair_permutations(n):
    one_twos = []
    for twos in range(n//2+1):
        ones = n - twos * 2
        one_twos.append((ones, twos))
    return one_twos

def factoral(n):
    i = 1
    for x in range(1, n+1):
        i *= x
    return i

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        for ones, twos in stair_permutations(n):
            n = factoral(ones+twos)
            d = factoral(ones) * factoral(twos)
            total += n // d
        return total
