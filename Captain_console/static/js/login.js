
window.onload = function(){
    $("#loader").hide()
    $('#sign-in-button').on('click', function(){
        let email = $("#id_username").val() //TODO: Change to email
        let password = $("#password").val()

        M.Toast.dismissAll();
        // If email is empty or contains only spaces
        if(email.trim().length === 0){
            M.toast({html: "Please enter your email", classes: "red"})
            return
        }
        // If password is empty or contains only spaces
        if(password.trim().length === 0){
            M.toast({html: "Please enter your password", classes: "red"})
            return
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
                    console.log(response.message)
                    window.location.replace(response.message)
                }
                console.log(response)
            }
        })
    });
}