"""
class Node(object):
    def __init__(self, c):
        self.c = c
        self.children = {}

    def add_child(self, c):
        if c in self.children:
            child = self.children[c]
        else:
            child = Node(c)
            self.children[c] = child
        return child

    def has_child(self, c):
        return c in self.children

    def get_child(self, c):
        return self.children.get(c)

    def get_children(self):
        return self.children.values()

    def empty(self):
        return 0 < len(self.children)

    def count_wild(self, string, idx=0):
        current = self
        if idx < len(string):
            c = string[idx]
            if c == "*":
                total = 0
                for child in current.get_children():
                    total += child.count_wild(string, idx+1)
                return total
            else:
                if current.has_child(c):
                    return current.get_child(c).count_wild(string, idx+1)
                else:
                    return 0
        else:
            return 1

class MagicDictionary(object):

    def __init__(self):
        self.root = Node('*')
        self.lengths = set()


    def buildDict(self, strings):
        self.root = Node('*')
        for string in strings:
            self.lengths.add(len(string))
            child = self.root
            for c in string:
                child = child.add_child(c)
        

    def search(self, word):
        if len(word) not in self.lengths:
            return False
        word = list(word)
        contained = self.root.count_wild(word) == 1
        for i in range(len(word)):
            c = word[i]
            word[i] = "*"
            wild_count = self.root.count_wild(word)
            word[i] = c
            if 1 < wild_count:
                return True
            elif not contained and wild_count == 1:
                return True
        return False
"""

def test_1():
    magic = MagicDictionary()
    magic.buildDict(["hello", "leetcode"])
    assert(magic.search('hhllo'))
    assert(not magic.search("hello"))
    assert(magic.search("hallo"))
    assert(not magic.search("hell"))
    assert(not magic.search("leetcoded"))
    hello = "hello"
    for i in range(len(hello)):
        h = list(hello)
        h[i] = "x"
        assert(magic.search("".join(h)))

def test_2():
    magic = MagicDictionary()
    magic.buildDict(["hello", "hallo", "leetcode"])
    assert(magic.search("hello"))
    assert(magic.search("hhllo"))
    assert(magic.search("hallo"))
    assert(not magic.search("hell"))
    assert(not magic.search("leedcoded"))
    assert(magic.search("eeetcode"))
    assert(magic.search("leetcodd"))
    assert(not magic.search("leetcode"))
    hello = "hello"
    for i in range(len(hello)):
        h = list(hello)
        h[i] = "x"
        assert(magic.search("".join(h)))


def test():
    test_1()
    test_2()

if __name__ == "__main__": test()
