
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
            //Save card into database
        }


    }

    $('#confirm-payment').on('click', function(){
       makeOrder()
    });
}