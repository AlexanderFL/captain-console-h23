/* Regex function that checks if email is valid, provided by user 'rnevius' on stackoverflow */
function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}
function setInvalid(form){
    $(form).removeClass('valid').addClass('invalid')
    $('#loader').hide()
}
function setValid(form){
    $(form).removeClass('invalid').addClass('valid')
}

window.onload = function(){
    $('#loader').hide()

    function registerUser(){
        let preloader = $('#loader')
        preloader.show()

        let username_form = $("#id_username")
        let username = username_form.val()

        let email_form = $("#email")
        let email = email_form.val()

        let password_form = $('#password')
        let password = password_form.val()

        let re_password_form = $('#re-password')
        let re_password = re_password_form.val()

        M.Toast.dismissAll();
        // Username is at least 4 characters long
        if (username.length < 4) {
            setInvalid(username_form)
            return
        }
        setValid(username_form)
        // Email is in a valid format
        if (!email_form.hasClass("valid")) {
            setInvalid(email_form)
            return
        }
        setValid(email_form)
        // Password is not just spaces and contains at least 6 characters
        if (password.trim() === "" || password.length < 6) {
            setInvalid(password_form)
            return
        }
        setValid(password_form)
        // Passwords match
        if (password !== re_password) {
            setInvalid(re_password_form)
            return
        }
        setValid(re_password_form)

        $.ajax({
            url: "register",
            method: "POST",
            data: {
                username: username,
                email: email,
                password: password
            },
            success: function (response) {
                // Status: 200, OK continue
                // Status: 0    Email is already in use
                if (response.status === 200){
                    window.location.replace(response.message)
                } else if(response.status === 0){
                    $('#email-helper-text').attr('data-error', response.message)
                    setInvalid(email_form)
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

    $("#email").on('focusout', function () {
        if (!validateEmail($('#email').val())){
            $('#email-helper-text').attr('data-error', "Please enter a valid email address")
        }
    });
}

