class Node(object):

    def __init__(self, c, word_end=False):
        self._c = c
        self._word_end = word_end
        self._children = {}

    def has_child(self, c):
        return c in self._children

    def set_end_word(self):
        self._word_end = True

    def is_end_word(self):
        return self._word_end

    def get_child(self, c):
        return self._children.get(c)

    def get_c(self):
        return self._C

    def add_child(self, c):
        new_child = Node(c)
        if c not in self._children:
            self._children[c] = new_child
            return new_child
        else:
            return self.get_child(c)

    def empty(self):
        return len(self._children) == 0


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__root = Node("*")
        self._has_empty = False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if len(word) == 0:
            self._has_empty = True
            return
        current = self.__root
        for c in word:
            current = current.add_child(c)
        current.set_end_word()
                

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return self._has_empty
        current = self.__root
        for c in word:
            if current.has_child(c):
                current = current.get_child(c)
            else:
                return False
        return current.is_end_word()
        
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.__root
        for c in prefix:
            if current.has_child(c):
                current = current.get_child(c)
            else:
                return False
        return True


def test():
    t = Trie()
    t.insert("app")
    t.insert("apple")
    t.insert("beer")
    t.insert("add")
    t.insert("jam")
    t.insert("rental")
    assert(not t.search("apps"))

if __name__ == "__main__":
    test()