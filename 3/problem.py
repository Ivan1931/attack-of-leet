class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = 0
        j = 0
        window = set()
        maxlen = 0
        while i < n and j < n:
            if s[j] not in window:
                window.add(s[j])
                j += 1
                maxlen = max(maxlen, len(window))
            else:
                window.remove(s[i])
                i += 1
        return maxlen



def test():
    solver = Solution()
    assert(solver.lengthOfLongestSubstring("abcabcbb") == 3)
    assert(solver.lengthOfLongestSubstring("bbbbb") == 1)
    assert(solver.lengthOfLongestSubstring("pwwkew") == 3)
    assert(solver.lengthOfLongestSubstring("aab") == 2)
    assert(solver.lengthOfLongestSubstring("dvdf") == 3)
    assert(solver.lengthOfLongestSubstring("au") == 2)
    assert(solver.lengthOfLongestSubstring("a") == 1)
    assert(solver.lengthOfLongestSubstring("") == 0)

if __name__ == "__main__":
    test()
