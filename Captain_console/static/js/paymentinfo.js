
window.onload = function(){
    $('.modal').modal();

    function validDate(date){
        var re = /(0[1-9]|1[0-2])\/2[0-9]/g
        return re.test(String(date))
    }

    function validCvc(cvc){
        let re = /^([0-9]{3})\b/g
        return re.test(String(cvc))
    }

    function makeOrder(){
        let cardHolder = $('#card_nameholder').val()
        let cardNumber = $('#card_number').val()
        let expireDate = $('#exp_date').val()
        let cvc = $('#cvc_number').val()

        // TODO: Verify all card details are correct
        // If card holder name is less than 4 characters
        if (cardHolder.trim().length < 4){
            return
        }
        // If card number is less than 16 letters or bigger than 19
        if (cardNumber.trim().length < 16 || cardNumber.trim().length > 19){
            return
        }
        // If date is not on the format (01/20 -> 12/29)
        if (expireDate.trim().length !== 5 || !validDate(expireDate.trim())){
            return;
        }
        // If cvc is not consecutive 3 numbers
        if (!validCvc(cvc.trim())){
            return;
        }

        // Check if user checked remember card details
        if ($('#remember-creditcard').prop('checked')){
            console.log("Hello?")
            $.ajax({
                url: '',
                type: 'POST',
                data: {
                    cardHolder: cardHolder,
                    cardNumber: cardNumber,
                    expireDate: expireDate,
                    cvc: cvc
                },
                success : function(response){
                    if (response.status === 999){
                        console.log(response.message)
                    } else if(response.status === 200){
                        console.log("Saved")
                    }
                }
            });
        }
    }

    $('#confirm-payment').on('click', function(){
       makeOrder()
    });
}