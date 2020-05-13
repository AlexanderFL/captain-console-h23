
window.onload = function(){
    $("#loader").hide()

    function loginUser(){
        let email = $("#email").val()
        let password = $("#password").val()

        M.Toast.dismissAll();
        // If password is empty or contains only spaces
        if (email.trim().length === 0){
            $("#email").addClass('invalid')
            return;
        }
        if(password.trim().length === 0){
            $('#password').addClass('invalid')
            return;
        }

        $("#loader").show()

        $.ajax({
            url: "",
            type: "POST",
            data: {
                email: email,
                password: password
            },
            success : function(response){
                $("#loader").hide()
                if (response.status === 0){
                    M.toast({html: response.message, classes: "red"})
                } else if(response.status === 1){
                    window.location.replace(response.message)
                }
                console.log(response)
            }
        })
    }

    // If user clicks on login button
    $('#sign-in-button').on('click', function(){
        loginUser()
    });

    // If user presses enter while inside any form
    $('#email, #password').on('keyup', function(event){
        if(event.keyCode === 13){
            loginUser()
        }
    });
}