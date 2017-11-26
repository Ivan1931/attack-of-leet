# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return f"[{self.start}, {self.end}]"

def interval_order(this, that):
    if this.start < that.start:
        return True
    elif this.start == that.start:
        return this.end < that.end
    else:
        return False

def overlaps(this, that):
    return (that.start <= this.start <= that.end or
            this.start <= that.start <= this.end or
            that.start <= this.end   <= that.end or
            this.start <= that.end   <= this.end)

def merge_intervals(this, that):
    return Interval(
        min(this.start, that.start),
        max(this.end, that.end),
    )

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda i: [i.start, i.end])
        merged_intervals = [intervals[0]]
        for i in intervals[1:]:
            last = merged_intervals[-1]
            if overlaps(last, i):
                merged_intervals[-1] = merge_intervals(last, i)
            else:
                merged_intervals.append(i)
        return merged_intervals

def test():
    solution = Solution()
    test_array = [
        Interval(1,3),
        Interval(2,6),
        Interval(8,10),
        Interval(15,18),
    ]
    expected_outcome = [
        Interval(1, 6),
        Interval(8, 10),
        Interval(15, 18),
    ]
    print(list(map(str, solution.merge(test_array))))

test()
