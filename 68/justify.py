def sprinkle_spaces(words, letter_count, length):
    if len(words) == 0:
        return []
    spaces_to_add = length - letter_count
    number_of_gaps = max(1, len(words) - 1)
    space_idx = 0
    for i in range(spaces_to_add):
        words[space_idx] += " "
        space_idx = (space_idx + 1) % number_of_gaps
    return "".join(words)

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if len(words) == 0:
            return []
        if maxWidth == 0:
            return words
        text = []
        line_words = [words[0]]
        letter_count = len(words[0])
        for word in words[1:]:
            line_characters = len(line_words) + letter_count + len(word)
            if maxWidth < line_characters:
                justified_line = sprinkle_spaces(line_words, letter_count, maxWidth)
                text.append(justified_line)
                line_words = [word]
                letter_count = len(word)
            else:
                letter_count += len(word)
                line_words.append(word)
        last_line_width = letter_count + len(line_words) - 1
        last_line = sprinkle_spaces(line_words, letter_count, last_line_width)
        last_line += " " * (maxWidth - last_line_width)
        if 0 < len(last_line):
            text.append(last_line)
        return text


def test():
    solution = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    L = 16
    result = [
       "This    is    an",
       "example  of text",
       "justification.  "
    ]
    solution_result = solution.fullJustify(words, L)
    assert(solution.fullJustify(words, L) == result)
    assert(solution.fullJustify([""], 0) == [""])
    assert(solution.fullJustify(["a", "b", "c"], 1) == ["a", "b", "c"])
    assert(solution.fullJustify(["a", "b", "c", "d", "e"], 3) == ["a b", "c d", "e  "])
    assert(solution.fullJustify(["a", "b", "c", "d"], 4) == ["a  b", "c d "])

if __name__ == "__main__":
    test()
