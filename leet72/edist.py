class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int

        """
        d = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]
        for i in range(len(word1)+1): d[0][i] = i
        for i in range(len(word2)+1): d[i][0] = i
        for i in range(1, len(word2)+1):
        	for j in range(1, len(word1)+1):
        		if word2[i-1] != word1[j-1]:
	        		d[i][j] = 1 + min(
	        			d[i-1][j-1],
	        			d[i][j-1],
	        			d[i-1][j],
	        		)
        return d[len(word2)][len(word1)]


def test():
	solution = Solution()
	print(solution.minDistance("word1", "word2"), "=1")
	print(solution.minDistance("wor", "word"), "=1")
	print(solution.minDistance("kitten", "sitting"),"=5")

if __name__ == '__main__': test()