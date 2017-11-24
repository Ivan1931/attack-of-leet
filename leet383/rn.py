from collections import Counter

class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom = Counter(ransomNote)
        magazine = Counter(magazine)
        return all(c in magazine and magazine[c] - f >= 0 for (c, f) in ransom.items())

        