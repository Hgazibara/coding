function sumOfN(n) {
    var numbers = [0],
        sign = Math.abs(n)/n;

    for (var i = 1; i <= Math.abs(n); i++) {
        numbers.push(numbers[numbers.length - 1] + i*sign);
    }

    return numbers;
};
