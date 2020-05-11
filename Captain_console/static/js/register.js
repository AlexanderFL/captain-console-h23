
window.onload = function(){

    function registerUser(){
        let username = $("#id_username").val()
        let email_form = $("#email")
        let email = email_form.val()
        let password = $("#password").val()
        let re_password = $("#re-password").val()

        M.Toast.dismissAll();
        // Username is at least 4 characters long
        if (username.length < 4) {
            M.toast({html: "Username needs to be at least 4 characters long", classes: "red"})
            return
        }
        // Email is in a valid format
        if (!email_form.hasClass("valid")) {
            M.toast({html: "Email format is incorrect", classes: "red"})
            return
        }
        // Password is not just spaces and contains at least 6 characters
        if (password.trim() === "" || password.length < 6) {
            M.toast({html: "Password needs to be at least 6 characters long", classes: "red"})
            return
        }
        // Passwords match
        if (password !== re_password) {
            M.toast({html: "Password do not match", classes: "red"})
            return
        }

        $.ajax({
            url: "register",
            method: "POST",
            data: {
                username: username,
                email: email,
                password: password
            },
            success: function (response) {
                if (response.status === 200){
                    window.location.replace(response.message)
                } else if(response.status === 0){
                    M.toast({html: response.message, classes: "red"})
                }
            }
        })
    }

    // Onclick triggers when user clicks on 'register'
    $("#register-button").on('click', function() {
        registerUser();
    });

    // Bind keyup on every form and execute when user presses enter
    $('#id_username, #email, #email, #password, #re-password').on('keyup', function(event){
        if (event.keyCode === 13){
            registerUser();
        }
    });
}