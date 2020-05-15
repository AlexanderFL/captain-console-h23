class Verification {
    
    /*
    * Returns the strength of the password given,
    * return: "strong" if password contains lower case, upper case, numbers, symbols and is at least 8 characters long
    * return: "medium" if password contains at least lower case, numbers and is at least 6 characters long
    * Regex strings were provided in this blog post https://www.thepolyglotdeveloper.com/2015/05/use-regex-to-test-password-strength-in-javascript/
    * */
    static get_password_strength(password){
        password = password.trim()
        let strong_regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})/g
        let medium_regex = /^(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9])))(?=.{6,})/g

        if(strong_regex.test(password)){
            return "strong"
        } else if(medium_regex.test(password)){
            return "medium"
        } else {
            return "weak"
        }
    }
}