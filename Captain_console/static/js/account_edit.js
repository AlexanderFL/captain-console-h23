/* Regex function that checks if email is valid, provided by user 'rnevius' on stackoverflow */
function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

$('#account-save-button').on('click', function(){
    let email = $('#email').val()
    let address = $('#address').val()
    let country = $('#country').val()
    let city = $('#city').val()
    let zip = $('#zip').val()

    // Email needs to be in a valid format
    if (!validateEmail(email)) {
        M.toast({html: "Email format is incorrect", classes: "red"})
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
            zip: zip
        },
        success: function(response){
            if (response.status === 0){
                M.toast({html: response.message, classes: "red"})
            } else if (response.status === 200){
                window.location.replace(response.message)
            }
        }
    })
});