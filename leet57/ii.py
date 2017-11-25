# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return f"[{self.start}, {self.end}]"

def mkintervals(intervals):
    return [Interval(s, e) for s, e in intervals]    

def print_intervals(intervals):
    print(",".join(map(str, intervals)))

import bisect
from functools import reduce

def overlaps(this, that):
    return any([
        this.start <= that.start <= this.end,
        this.start <= that.end <= this.end,
        that.start <= this.start <= that.end,
        that.start <= this.end <= that.end,
    ])
        
def merge(this, that):
    return Interval(
        s = min(this.start, that.start),
        e = max(this.end, that.end)
    )

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        starts = [i.start for i in intervals]
        ends = [i.end for i in intervals]
        i = bisect.bisect_left(ends, newInterval.start)
        j = bisect.bisect(starts, newInterval.end)
        while 0 <= i < len(intervals) and overlaps(intervals[i], newInterval): i -= 1
        while 0 <= j < len(intervals) and overlaps(intervals[j], newInterval): j += 1
        if i == j:
            intervals.insert(i, newInterval)
            return intervals
        else:
            if i < 0:
                m = reduce(merge, intervals[0:j], newInterval)
                return [m] + intervals[j:]
            else:
                m = reduce(merge, intervals[i+1:j], newInterval)
                return intervals[0:i+1] + [m] + intervals[j:]



        

def main():
    solution = Solution()
    example2 = [mkintervals([[1,3], [6,9]]), Interval(2,5)]
    print_intervals(solution.insert(*example2))
    example1 = [mkintervals([[1,2],[3,5],[6,7],[8,10],[12,16]]), Interval(4,9)]
    print_intervals(solution.insert(*example1))
    example3 = [mkintervals([[1,3],[3,4],[5,9]]), Interval(2,5)]
    print_intervals(solution.insert(*example3))
    example4 = [mkintervals([[1,5]]), Interval(6,8)]
    print_intervals(solution.insert(*example4))
    example5 = [mkintervals([[1,5]]), Interval(5,7)]
    print_intervals(solution.insert(*example5))


if __name__ == '__main__':
    main()
        