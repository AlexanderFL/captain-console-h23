
window.onload = function(){
    $('#sign-in-button').on('click', function(){
        let email = $("#id_username").val() //TODO: Change to email
        let password = $("#password").val()

        M.Toast.dismissAll();
        if(email.trim().length === 0){
            M.toast({html: "Please enter your email", classes: "red"})
            return
        }
        if(password.trim().length === 0){
            M.toast({html: "Please enter your password", classes: "red"})
            return
        }

        $.ajax({
            url: "",
            type: "POST",
            data: {
                email: email,
                password: password
            },
            success : function(response){

            }
        })
    });
}