function slope(points) {
    var dx = points[2] - points[0],
        dy = points[3] - points[1];

    return dx === 0 ? "undefined" : (dy/dx).toString();
}
