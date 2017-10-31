from collections import Counter
from sys import maxsize

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        freqs = Counter(t)
        seen = len(t)
        start, end = 0, 0
        min_interval = (0, 0)
        min_len = maxsize
        while end < len(s):
            c = s[end]
            if c in freqs:
                freqs[c] -= 1
                seen -= 1
            end += 1
            while seen == 0:
                c = s[start]
                if c in freqs:
                    freqs[c] += 1
                    seen += 1
                if end - start < min_len:
                    min_len = end - start
                    min_interval = (start, end)
                start += 1
        if min_len == maxsize:
            return ""
        else:
            start, end = min_interval
            return s[start:end]

def test():
    solver = Solution()
    test_1 = ["ADOBECODEBANC", "ABC"]
    result_1 = solver.minWindow(*test_1)
    print(result_1)
    test_2 = ["12345", "678"]
    result_2 = solver.minWindow(*test_2)
    print(result_2)

if __name__ == '__main__':
    test()
