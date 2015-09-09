var findAverage = function (nums) {
    return nums.reduce(
        (x, y) => x + y,
        0
    ) / nums.length;
};
