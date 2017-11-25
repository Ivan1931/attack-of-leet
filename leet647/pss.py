class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        palindromes = set()
        for i in range(len(s)):
            k = 1
            palindromes.add((i,i))
            while 0 <= i - k and i + k < len(s):
                if s[i-k] == s[i+k]:
                    palindromes.add((i-k,i+k))
                else:
                    break
                k += 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                k = 1
                palindromes.add((i, i+1))
                while 0 <= i - k and i + k + 1 < len(s):
                    if s[i - k] == s[i + k + 1]:
                        palindromes.add((i-k, i+k+1))
                    else:
                        break
                    k += 1
        print(palindromes)
        return len(palindromes)

def test():
    solution = Solution()
    test1 = "abc"
    print(solution.countSubstrings(test1))
    test2 = "aaa"
    print(solution.countSubstrings(test2))
    test3 = "a" * 1000
    # print(solution.countSubstrings(test3))
    


if __name__ == "__main__": test()
        
