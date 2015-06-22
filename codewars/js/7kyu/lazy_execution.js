var make_lazy = function () {
    var fn_arguments = arguments;
    return function () {
        return fn_arguments[0].apply(null, Array.prototype.slice.call(fn_arguments, 1));
    };
};
