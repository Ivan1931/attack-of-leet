from heapq import heappop, heappush

class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lowerheap = []
        self.higherheap = []
        self.items = 0

    def _pop_lower(self):
        return -heappop(self.lowerheap)

    def _pop_higher(self):
        return heappop(self.higherheap)

    def _peak_lower(self):
        return -self.lowerheap[0]

    def _peak_higher(self):
        return self.higherheap[0]

    def _push_lower(self, num):
        heappush(self.lowerheap, -num)

    def _push_higher(self, num):
        heappush(self.higherheap, num)

    def _insert_first_number(self, num):
        self.higherheap = [num]

    def _insert_second_number(self, num):
        t = (num, self._pop_higher())
        self.lowerheap = [-min(t)]
        self.higherheap = [max(t)]

    def _insert_number(self, num):
        """
        # Explanation:
        case 1:
            -> there are equally many elements in both halves
            -> to maintain the invariant we insert num into the list
               where it maintains the ordering of the two heaps
        case 2.1:
            -> high element then simply push into the lower elements
        case 2.2:
            -* This case is a tad more complex
            -> there is one less element in the lower list than the higher one
            -> num is larger than the smallest higher element
            -> if we insert lower in the smaller half list then our invarient will be violated
            -> so we must remove the smallest of the largest elements (higher) from the larger elements
            -> we insert it in the lower list
            -> now there is one more element in the lower list than the higher one
            -> we equalise the lengths by placing num in the higher list
        case 3:
            -> this case is a mirror of case 2 but in reverse
        """
        ll = len(self.lowerheap)
        hl = len(self.higherheap)
        higher = self._peak_higher()
        lower = self._peak_lower()
        if ll == hl:
            if num < higher:
                self._push_lower(num)
            else:
                self._push_higher(num)
        elif ll < hl: # abs(ll - hl) <= 1
            if num < higher:
                self._push_lower(num)
            else:
                self._pop_higher()
                self._push_lower(higher)
                self._push_higher(num)
        else:
            if num < lower:
                self._pop_lower()
                self._push_higher(lower)
                self._push_lower(num)
            else:
                self._push_higher(num)

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not self.higherheap:
            self._insert_first_number(num)
        elif not self.lowerheap:
            self._insert_second_number(num)
        else:
            self._insert_number(num)


    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.higherheap) == len(self.lowerheap):
            return (self._peak_higher() + self._peak_lower()) / 2
        elif len(self.higherheap) < len(self.lowerheap):
            return float(self._peak_lower())
        else:
            return float(self._peak_higher())

    def printout(self):
        print(", ".join(
            [str(-x) for x in self.lowerheap] 
          + [str(y) for y in self.higherheap]))

def main():
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(3)
    mf.addNum(8)
    mf.addNum(6)
    mf.printout()
    print(mf.findMedian())


if __name__ == '__main__':
    main()
