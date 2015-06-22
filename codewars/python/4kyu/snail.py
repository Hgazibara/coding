def snail(array):
    if len(array) == 1: return array[0]
    return traverse(array, 0, len(array) - 1)


def traverse(array, left, right):
    if left == right:
        return [array[left][right]]
    if left > right:
        return []

    return outer_ring(array, left, right) + traverse(array, left + 1, right - 1)


def outer_ring(array, left, right):
    top_row = array[left][left : right+1]
    right_column = [row[right] for row in array[left+1 : right+1]]

    bottom_row = list(reversed(array[right][left:right]))
    left_column = list(reversed([row[left] for row in array[left+1:right]]))

    return top_row + right_column + bottom_row + left_column
