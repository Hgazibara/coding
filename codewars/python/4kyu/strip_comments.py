def solution(text, markers):
    output = []

    for line in text.split('\n'):
        if any([marker in line for marker in markers]):
            marker_index = min([line.index(m) for m in markers if m in line])
            output.append(line[:marker_index].strip())
        else:
            output.append(line.strip())

    return '\n'.join(output)
