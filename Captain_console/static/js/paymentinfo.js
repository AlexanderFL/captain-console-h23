
window.onload = function(){
    $('.modal').modal();

    function makeOrder(){
        let cardHolder = $('#card_nameholder').val()
        let cardNumber = $('#card_number').val()
        let expireDate = $('#exp_date').val()
        let cvc = $('#cvc_number').val()

        // TODO: Verify all card details are correct

        // Check if user checked remember card details
        if ($('#remember-creditcard').prop('checked')){
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
            })
        }


    }

    $('#confirm-payment').on('click', function(){
       makeOrder()
    });
}