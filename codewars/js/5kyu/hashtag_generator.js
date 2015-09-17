function transform(sentence) {
    var words = sentence.split(' ').filter(word => word.length > 0);
    return words.map(word => word[0].toUpperCase() + word.slice(1)).join('');
}

function generateHashtag (str) {
    if (str === '') {
        return false;
    }
    hashtag = `#${transform(str)}`;
}
