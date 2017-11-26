class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1: return s
        best = (0, 0)
        for c in range(1, len(s)):
            i = c
            j = c
            while 0 <= i and j < len(s) and s[i] == s[j]:
                if best[1] - best[0] < j - i:
                    best = (i, j)
                i -= 1
                j += 1
            i = c - 1
            j = c
            while 0 <= i and j < len(s) and s[i] == s[j]:
                if best[1] - best[0] < j - i:
                    best = (i, j)
                i -= 1
                j += 1
        return s[best[0]:best[1]+1]

def test():
    solver = Solution()
    assert(solver.longestPalindrome("babad") in ["bab", "aba"])
    assert(solver.longestPalindrome("cbbd") in ["bb"])
    assert(solver.longestPalindrome("bb") == "bb")
    assert(solver.longestPalindrome("s") == "s")
    assert(solver.longestPalindrome("") == "")

if __name__ == "__main__": test()
        
