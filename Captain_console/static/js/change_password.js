
function setInvalid(form){
    $(form).removeClass('valid').addClass('invalid')
    $('#loader').hide()
}
function setValid(form){
    $(form).removeClass('invalid').addClass('valid')
}

$(document).ready(function () {
    let password_form = $('#current-password')
    let new_password_form = $('#new-password')
    let new_password_form_repeat = $('#repeat-new-password')

    new_password_form.focusout(function(){
        let new_pass_helper = $('#new-password-helper-text')

        let new_password_form = $('#new-password')
        let new_password = new_password_form.val()
        let strength = Verification.get_password_strength(new_password)

        if (strength === "strong"){
            new_pass_helper.attr('data-success', "Strong password")
        } else if (strength === "medium"){
            new_pass_helper.attr('data-success', "Medium password")
        } else {
            new_password_form.removeClass('valid').addClass('invalid')
            new_pass_helper.attr('data-error', "Weak password - needs to contain letters and numbers and be at least 6 characters")
        }
    });

    new_password_form_repeat.focusout(function(){
        let new_pass = new_password_form.val().trim()
        let repeat = new_password_form_repeat.val().trim()

        console.log("" !== "")

        if (new_pass !== repeat){
            setInvalid(new_password_form_repeat)
        }else{
            setValid(new_password_form_repeat)
        }
    })

    $('#password-save-button').click(function () {
        let password_form = $('#current-password')
        let new_password_form = $('#new-password')
        let new_password_form_repeat = $('#repeat-new-password')

        let current_password = password_form.val().trim()
        let new_password = new_password_form.val().trim()
        let new_password_repeat = new_password_form_repeat.val().trim()

        if (current_password.length === 0){
            setInvalid(password_form)
            return
        }
        if (!new_password_form.hasClass('valid')){
            setInvalid(new_password_form)
            return
        }
        if (new_password !== new_password_repeat){
            setInvalid(new_password_form_repeat)
            return
        }

        $.ajax({
            url: '',
            method: 'POST',
            data: {
                current_password: current_password,
                new_password: new_password
            },
            success : function(response){
                // status 200: Ok, continue
                // status 0:   Invalid current password
                if (response.status === 200){
                    window.location.replace(response.message)
                } else if (response.status === 0){
                    console.log('Incorrect password')
                }
            }
        });
    });
});
