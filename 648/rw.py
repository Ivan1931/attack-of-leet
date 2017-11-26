import re

def construct_trie(words):
    words.sort(key=len)
    trie = {}
    for word in words:
        current = trie
        for c in word:
            if c in current:
                if len(current[c]) == 0:
                    break
                else:
                    current = current[c]
            else:
                current[c] = {}
                current = current[c]
    return trie

def prefixed(trie, word):
    prefix = ""
    for c in word:
        if c in trie:
            prefix += c
            trie = trie[c]
        elif len(trie) == 0:
            return True, prefix
        else:
            break
    return False, ""


class Solution(object):
    def replaceWords(self, words, sentence):
        if len(words) == 0:
            return sentence
        trie = construct_trie(words)
        sentence = re.split(r'(\s+)', sentence)
        for i in range(len(sentence)):
            word = sentence[i]
            if " " not in word:
                is_prefixed, prefix = prefixed(trie, word)
                if is_prefixed:
                    sentence[i] = prefix
        return "".join(sentence)


solution = Solution()

dict1 = ["a", "aa", "aaa", "aaaa"]
sentence1 = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
a1 = solution.replaceWords(dict1,  sentence1)
print(a1)

assert(a1 == "a a a a a a a a bbb baba a")
