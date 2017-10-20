class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def length(self, node):
        current = node
        length = 0
        while current is not None:
            current = current.next
            length += 1
        return length

    def rotateRight(self, head, k):
        if head is None or head.next is None:
            return head
        k = k % self.length(head)
        if k == 0:
            return head
        kth = head
        for i in xrange(k):
            kth = kth.next or head
        if kth is head:
            return head
        klast = head
        while kth.next is not None:
            kth = kth.next
            klast = klast.next
        new_head = klast.next
        klast.next = None
        kth.next = head
        return new_head

