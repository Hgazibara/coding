def spin_words(sentence):
    return ' '.join(map(modify, sentence.split()))
    
def modify(word):
    return word if len(word) < 5 else word[::-1]
