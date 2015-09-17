function genfib(){
    var factors = [0, 1];

    return function* fib() {
        var prev = factors.shift();
        factors.push(prev + factors[0]);
        return prev;
    }
}
