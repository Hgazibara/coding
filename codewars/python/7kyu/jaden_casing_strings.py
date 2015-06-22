def toJadenCase(string):
    return ' '.join([str.capitalize() for str in string.split()])
