import math

# hint: add divmod and textwrap

def justify(text, width):
    words = text.split()
    lines = []

    while words:
        chosen_words = choose_words(words, width)
        spaces = compute_spaces(chosen_words, width)
        lines.append(build_line(chosen_words, spaces))

    if lines:
        lines[-1] = ' '.join(lines[-1].split())

    return '\n'.join(lines)


def choose_words(words, width):
    line_length = 0
    chosen_words = []

    while line_length < width and words:
        min_length = len(words[0]) + 1 if chosen_words else len(words[0])

        if line_length + min_length > width:
            break

        word = words.pop(0)

        chosen_words.append(word)
        line_length += min_length

    return chosen_words


def compute_spaces(chosen_words, width):
    words_count = len(chosen_words)
    words_left = words_count

    spaces = []
    spaces_to_add = width - sum(len(w) for w in chosen_words)
    spaces_per_boundary = count_spaces(spaces_to_add, words_left)

    while spaces_to_add:
        spaces.append(' ' * spaces_per_boundary)
        spaces_to_add -= spaces_per_boundary
        words_left -= 1
        spaces_per_boundary = count_spaces(spaces_to_add, words_left)

    return spaces


def count_spaces(spaces_to_add, words_count):
    try:
        return int(math.ceil(float(spaces_to_add) / (words_count - 1)))
    except ZeroDivisionError as e:
        return spaces_to_add


def build_line(chosen_words, spaces):
    line = []
    spaces = iter(spaces)

    for word in chosen_words:
        line.append(word)
        line.append(next(spaces, ''))

    return ''.join(line).strip(' ')
