class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.previous = None

class Queue(object):

    def __init__(self):
        self.start = None
        self.end = None
        self.items = 0

    def dequeue(self):
        old_end = self.end
        if self.items <= 1:
            self.items = max(0, self.items-1)
            self.end = None
            self.start = None
            return old_end
        else:
            self.items -= 1
            self.end.previous.next = None
            self.end = self.end.previous
            old_end.next = None
        return old_end

    def enqueue(self, node):
        if self.start is None:
            self.start = node
            self.end = node
            self.items = 1
        else:
            self.items += 1
            old_start = self.start
            node.next = old_start
            node.previous = None
            old_start.previous = node
            self.start = node

    def move_to_front(self, node):
        if self.start is not node:
            if node is self.end:
                self.end = self.end.previous
                self.end.next = None
                self.enqueue(node)
            else:
                node.previous.next = node.next
                node.next.previous = node.previous
                node.previous = None
                node.next = None
                self.enqueue(node)

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity
        self.items = 0
        self.queue = Queue()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            value, node = self.cache[key]
            if 1 < self.items: # we only move to front for more than 1 item
                self.queue.move_to_front(node)
            return value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return
        if key in self.cache:
            _, node = self.cache[key]
            self.cache[key] = (value, node)
            self.queue.move_to_front(node)
        else:
            node = Node(key)
            self.cache[key] = (value, node)
            self.queue.enqueue(node)
            if self.capacity == self.items:
                to_delete = self.queue.dequeue()
                del self.cache[to_delete.val]
            else:
                self.items += 1


def test():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)
    cache.get(2)
    cache.put(4, 4)
    cache.get(1)
    cache.get(3)
    cache.get(4)

def test_2():
    cache = LRUCache(1)
    cache.put(2, 1)
    cache.get(2)
    cache.put(3, 2)
    cache.get(2)
    cache.get(3)

def test_3():
    cache = LRUCache(2)
    cache.put(1,1)
    cache.get(1)
    cache.get(1)
    cache.put(2,2)
    cache.get(2)
    cache.get(1)
    cache.put(3,3)
    cache.get(2)
    cache.get(1)
    cache.get(3)

def test_4():
    cache = LRUCache(0)
    cache.put(2,2)
    cache.get(2)
    cache.get(1)

def test_5():
    cache = LRUCache(3)
    cache.put(1,1)
    cache.put(2,2)
    cache.get(2)
    cache.get(2)
    cache.put(3,3)
    cache.put(3,3)
    cache.get(3)
    cache.put(4,4)
    cache.get(1)

def test_6():
    cache = LRUCache(2)
    cache.put(2,1)
    cache.put(2,2)
    cache.get(2)
    cache.put(1,1)
    cache.put(4,1)
    cache.get(2)

def test_7():
    cache = LRUCache(2)
    cache.put(2,1)
    cache.put(1,1)
    cache.put(2,3)
    cache.put(4,1)
    cache.get(1)
    cache.get(2)

def test_all():
    test()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
    test_7()

test_all()
