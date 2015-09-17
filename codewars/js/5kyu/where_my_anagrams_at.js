var sort = word => word.split('').sort().join('');

function anagrams(word, words) {
    return words.filter(w => sort(word) === sort(w));
}
