import collections
import string

class Solution(object):
    def findLadders(self, begin_word, end_word, word_dict):
        word_dict.add(begin_word)
        word_dict.add(end_word)

        self.word_dict = word_dict

        current_level = set([begin_word])
        next_level = set()

        self.parents = collections.defaultdict(set)
        self.found_paths = []

        self.path = collections.deque()
        self.path.append(end_word)

        while True:
            for word in current_level:
                self.word_dict.remove(word)

            for word in current_level:
                for next_word in self.findNextWords(word):
                    next_level.add(next_word)

            if not next_level:
                break

            if end_word in next_level:
                self.buildPaths(begin_word, end_word)
                break

            current_level = next_level
            next_level = set()

        return self.found_paths

    def findNextWords(self, current_word):
        for i, __ in enumerate(current_word):
            for next_char in string.ascii_lowercase:
                if current_word[i] == next_char:
                    continue

                new_word = current_word[:i] + next_char + current_word[i+1:]

                if new_word in self.word_dict:
                    self.parents[new_word].add(current_word)
                    yield new_word

    def buildPaths(self, begin_word, end_word):
        if begin_word == end_word:
            self.found_paths.append(list(reversed(self.path)))
            return

        for next_word in self.parents[end_word]:
            self.path.append(next_word)
            self.buildPaths(begin_word, next_word)
            self.path.pop()
