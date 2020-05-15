
window.onload = function(){
  //  $('.modal').modal();

    function markOrderConfirmed() {
        const path = window.location.pathname

        $.ajax({
                url: path + '?confirmed',
                type: 'POST',
                success : function(response){
                    if (response.status === 200){
                        window.location.replace(response.message)
                    } else if(response.status === 900){

                        console.log(response.message)
                    }
                }
            });

        if ($('#remember_creditcard').is(':checked')){
             M.toast({html: "We saved your card for next time", classes: "green"})
        }
    }

    function validDate(date){
        var re = /(0[1-9]|1[0-2])\/2[0-9]/g
        return re.test(String(date))
    }

    function validCvc(cvc){
        let re = /^([0-9]{3})\b/g
        return re.test(String(cvc))
    }

    function validateOrder(){
        let cardHolder = $('#card_nameholder').val()
        let cardNumber = $('#card_number').val()
        let expireDate = $('#exp_date').val()
        let cvc = $('#cvc_number').val()
        const path = window.location.pathname

        // If card holder name is less than 4 characters
        if (cardHolder.trim().length < 4){
            M.toast({html: "Cardholder name can't be shorter than 4 letters", classes: "red"})
            return
        }
        // If card number is less than 15 letters or bigger than 19
        if (cardNumber.trim().length < 15 || cardNumber.trim().length > 19){
            M.toast({html: "Please enter a correct card number", classes: "red"})
            return
        }
        // If date is not on the format (01/20 -> 12/29)
        if (expireDate.trim().length !== 5 || !validDate(expireDate.trim())){
            M.toast({html: "Please enter your card expire date", classes: "red"})
            return;
        }
        // If cvc is not consecutive 3 numbers
        if (!validCvc(cvc.trim())){
            M.toast({html: "Please enter your CVC number", classes: "red"})
            return;
        }

         // Check if user checked remember card details
        if ($('#remember_creditcard').is(':checked')){
            let cardHolder = $('#card_nameholder').val()
            let cardNumber = $('#card_number').val()
            let expireDate = $('#exp_date').val()
            let cvc = $('#cvc_number').val()
            const path = window.location.pathname

            $.ajax({
                url: path + '?save_card',
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
                        console.log(response.message)
                    }
                }
            });
        }
        markOrderConfirmed()
    }

    $('#confirm-payment').on('click', function(){
        //Þarf að tékka hér hvort það sé örugglega eitthvað í körfu
        const path = window.location.pathname

         $.ajax({
        url: path + '?check_cart',
        type: 'GET',
        success: function(resp){
            console.log("checking if there are products in cart")
                console.log(resp.status)
                console.log(resp.message)

            if (resp.message == "empty") {
                M.toast({html: "Your shopping cart is empty", classes: "red"})
            }
            else {
                validateOrder()
            }
        },
        error: function(xhr, status, error) {
            console.log(error)
        }
        });
    });
}