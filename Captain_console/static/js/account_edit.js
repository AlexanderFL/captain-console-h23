/* Regex function that checks if email is valid, provided by user 'rnevius' on stackoverflow */
function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}
function validateUrl(url){
    var re = /^(https|http):\/\/.*(jpg|png|jpeg|gif)/g
    return re.test(String(url))
}


$(document).ready(function(){
    $('.modal').modal();
    $('#loader').hide()
});

$('#accept-image').on('click', function () {
    let picture_url = $('#picture-url').val().trim()
    if (validateUrl(picture_url)){
        $('#user-image').attr('src', picture_url + "?rand=" + Math.random())
    } else {
        $('#picture-url').val("")
        M.toast({html: "Not a valid URL", classes: "red"})
    }
});

$("#email").on('focusout', function () {
   if (!validateEmail($('#email').val())){
       $('#email-helper-text').attr('data-error', "Please enter a valid email address")
   }
});

$('#account-save-button').on('click', function(){
    let preloader = $('#loader')
    let email = $('#email').val()
    let address = $('#address').val()
    let country = $('#country').val()
    let city = $('#city').val()
    let zip = $('#zip').val()
    let picture_url = $('#picture-url').val().trim()

    preloader.show()

    // Email needs to be in a valid format
    if (!validateEmail(email)) {
        preloader.hide()
        return
    }

    $.ajax({
        url: '',
        method: 'POST',
        data: {
            email: email,
            address: address,
            country: country,
            city: city,
            zip: zip,
            picture: picture_url
        },
        success: function(response){
            // status 0: Email already in use
            // status 200: OK, continue
            if (response.status === 0){
                $('#email-helper-text').attr('data-error', response.message)
                $('#email').removeClass('valid').addClass('invalid')
                preloader.hide()
            } else if (response.status === 200){
                window.location.replace(response.message)
            }
        }
    })
});