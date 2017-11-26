"""
* This will be a dynamic programming problem
* Essentially the problem can be broken down into the following recurence relation
  * The current player either takes from the front or the end
  * The next player attempts to maximise there score by taking from the front and end
  * Once a value has been taken from the front or the end we have the same subproblem again that is overlapping
  * We can cache the score of each player from each game
  * We will need to fill out the table which will take up Omega(n^2) space - that is the lower bound. We must visit each one at least once
  * The upper bound of the problem will depend on what algorithm we end up designing
  * Since the max size of the array is n this table will use O(2 * n^2) extra space
"""

def upper_triange(n):
    nums = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        nums[i][i] = 'n'
    c = 0
    for i in range(1, n):
        for j in range(n-i):
            nums[j][i+j] = c
            c+= 1
    return nums

def lower_triangle(n):
    nums = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        nums[i][i] = 'n'
    c = 0
    for i in range(1, n):
        for j in range(n-i):
            nums[i+j][j] = c
            c+=1
    return nums
    

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # First item is the best score for the person going first
        # Second item is the best score for the person going second
        memo = [[(0,0) for i in nums] for j in nums]
        # The middle section of our dp array is the score for a single game
        for i, n in enumerate(nums):
            memo[i][i] = (n, 0)
        for i in range(1, len(nums)):
            for j in range(len(nums) - i):
                # Best score for person going first is the best
                # best pick of their options if they go second in the next round
                end = i+j
                start = j
                print(f"{start} {end}")
                go_first_best = max(
                    memo[start+1][end][1] + nums[start], 
                    memo[start][end-1][1] + nums[end]
                )
                go_second_best = max(
                    memo[start+1][end][0] + nums[start], 
                    memo[start][end-1][0] + nums[end]
                )
                memo[start][end] = (go_first_best, go_second_best)
        first, second = memo[len(nums)-1][0]
        return second <= first

                

def test():
    solver = Solution()
    example1 = [1,5,2]
    assert(not solver.PredictTheWinner(example1))
    example2 = [1,5,33,7]
    assert(solver.PredictTheWinner(example2))


if __name__ == "__main__": test()