# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    
    def __eq__(self, that):
        return self.start == that.start and self.end == that.end

    def __gt__(self, that):
        if self.start == that.start:
            return self.end < that.end
        else:
            return self.start < that.start


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
        if 0 == len(intervals):
            return []
        new_intervals = [intervals[0]]
        for interval in intervals[1:]:
            if overlaps(new_intervals[-1], interval):
                new_intervals[-1] = merge(new_intervals[-1], interval)
            elif overlaps(new_intervals[-1], newInterval):
                new_intervals[-1] = merge(new_intervals[-1], newInterval)
            else:
                new_intervals.append(interval)
        return new_intervals
        