function validate(username, password){
    var valid = new Validator(),
        error = 'Wrong username or password!';


    if (password.indexOf('||') > -1 || password.indexOf('//') > -1) {
        return error;
    }

    return valid.login(username, password);
}
