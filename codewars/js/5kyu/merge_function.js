function mergesorted(a, b) {
    var output = [],
        m = a.length,
        n = b.length;

    var i = 0,
        j = 0;

    while (i < m || j < n) {
        if (i == m) {
            output.push(b[j++]);
        } else if (j == n) {
            output.push(a[i++]);
        } else if (a[i] < b[j]) {
            output.push(a[i++]);
        } else {
            output.push(b[j++]);
        }
    }

    return output;
}
