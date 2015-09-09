var Person = function() {
    var person = {
        _name: "Leroy",
        _friends: [],
        fillFriends(f) {
            var p = this;
            f.map(friend => p._friends.push(friend))
        }
    }
    return person;
}
