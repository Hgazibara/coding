import re

def abbreviate(s):
    p = re.compile(r'[^\w]+')
    for w in p.split(s):
        s = s.replace(w, transform(w))
    return s
    
def transform(w):
    return w if len(w) < 4 else w[0] + str(len(w) - 2) + w[-1]
