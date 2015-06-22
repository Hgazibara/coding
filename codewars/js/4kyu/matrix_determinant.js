function determinant(matrix) {
    if (matrix.length == 1) {
        return matrix[0][0];
    }

    if (matrix.length == 2) {
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0];
    }

    var result = 0;

    for (var j = 0; j < matrix.length; ++j) {
        result += Math.pow(-1, j) * matrix[0][j] * determinant(submatrix(matrix, j));
    }

    return result;
}

function submatrix(matrix, index) {
    var submatrix = [],
        n = matrix.length;

    for (var i = 1; i < n; ++i) {
        var row = [];

        for (var j = 0; j < n; ++j) {
            if (j != index) {
                row.push(matrix[i][j]);
            }
        }
        submatrix.push(row);
    }

    return submatrix;
}
