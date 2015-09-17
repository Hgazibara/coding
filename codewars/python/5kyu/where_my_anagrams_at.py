def anagrams(word, words):
    word = sorted(word)
    return filter(lambda w: word == sorted(w), words)
