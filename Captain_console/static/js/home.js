//Updates cart qty in nav bar
function updateCartQty(items_in_cart) {
    document.getElementById("shopping-cart-quantity").innerHTML = "" + items_in_cart + ""
    console.log("SUCCESS: " + status)
}


$('.add-to-cart').on('click', function (e) {
        e.preventDefault()
        console.log("add to cart")
        var prod_id = $(this).data('prod')
        console.log(prod_id)
        var csrftoken = getCookie('csrftoken');
        var token = $("meta[name='_csrf']").attr("content");
        var header = $("meta[name='_csrf_header']").attr("content");

        //No quantity set, only "add to cart"
        var quantity = 1

         $.ajax({
            url: "?add_to_cart=" + prod_id,
            type: "GET",
            data: {prod_id: prod_id, quantity: quantity},

            success: function(resp, status){
                if (resp.status === 999){
                    window.location.replace(resp.message)
                }
                console.log("hello")
                items_in_cart = resp.data.length
                updateCartQty(items_in_cart)
                M.toast({html: "Product was added to cart", classes: "green"})
            },
            error: function(status){
                M.toast({html: "Something went wrong on our end", classes: "red"})
                console.log("ERROR: " + status.message)
            }
        })
    });

function getCookie(name) {
var cookieValue = null;
if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
        }
    }
}
return cookieValue;
}
