from collections import deque, Counter
from heapq import heappop, heappush, heapify

class Solution:
    def leastInterval(self, tasks, n):
        """
        [A]
        [A, A, B, B, C], n = 2
        [A, A, A, B, B, B], n = 2
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n == 0:
        	return len(tasks)
        heap = [(-freq, task) 
        	for (task, freq) in Counter(tasks).most_common()]
        heapify(heap)
        current_tasks = deque()
        finished_tasks = []
        i = 0
        while i < len(tasks):
        	if n < len(current_tasks):
	        	next_task = current_tasks.popleft()
	        	finished_tasks.append(next_task)
	        	if next_task != "I":
	        		(freq, task) = next_task
	        		if freq < -1:
		        		heappush(heap, (freq+1, task))
        	if len(heap) == 0:
        		current_tasks.append("I")
        	else:
        		desired_task = heappop(heap)
        		current_tasks.append(desired_task)
        		i+=1
        # print(current_tasks, finished_tasks)
        return len(finished_tasks) + len(current_tasks)


def test():
	solution = Solution()
	test_input_1 = [["A", "A", "A", "B", "B", "B"], 2]
	assert(solution.leastInterval(*test_input_1) == 8)
	test_input_2 = [["A", "A", "B", "B", "C"], 2]
	assert(solution.leastInterval(*test_input_2) == 5)

if __name__ == "__main__": test()