def determinant(matrix):
    assert len(matrix) >= 1

    if len(matrix) == 1:
        return matrix[0][0]

    pivots = enumerate(matrix[0])
    return sum(v * (-1)**i * determinant(submatrix(matrix, i)) for i,v in pivots)


def submatrix(matrix, index):
    return [[v for i,v in enumerate(row) if i != index] for row in matrix[1:]]
