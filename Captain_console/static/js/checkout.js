// Initializing date picker
//  document.addEventListener('DOMContentLoaded', function() {
//     var elems = document.querySelectorAll('.datepicker');
//     var instances = M.Datepicker.init(elems, options);
//   });



//Remove item from shopping cart interface
function removeShoppingCartItem(order_prod_id) {
order_product_cards = $(".order-product-card")
order_product_cards_id = $(".order-product-card").map(function () {
    return this.id
}).toArray();

for (var i = 0; i < order_product_cards.length; i++) {
    order_product_cards_id[i] = parseInt(order_product_cards_id[i])
    card_id = order_product_cards_id[i]

    if (card_id == order_prod_id) {
        order_product_cards[i].style.display = 'none' //Do not display
    }
}
}

function updateCart(order_info, order_prod_id) {
    qty_id = order_prod_id + "-quantity"
    qty_element = document.getElementById(qty_id)
    price_id = order_prod_id + "-price"
    price_element = document.getElementById(price_id)
    total_price = 0

    //Get information about qty and price of order products
    if (order_info.length !==0) {
        for (i = 0; i < order_info.length; i++) {
        order_product = order_info[i]
        total_price += order_product.price

            if (order_product.id == order_prod_id) {
                qty_element.innerHTML = "" + order_product.qty + "";
                price_element.innerHTML = "$" + order_product.price + "";
            }
        }
        total_price = total_price.toFixed(2);
        document.getElementById("sub-total").innerHTML = "Subtotal: " + "$" + total_price + " "
    }
    else {
        document.getElementById("sub-total").innerHTML = "Looks like your cart is empty. Feel free to go to the store to keep shopping."
    }
    //Update shopping cart qty in nav bar
    items_in_cart = order_info.length
    document.getElementById("shopping-cart-quantity").innerHTML = " " + items_in_cart + " "
}

//Change qty in shopping cart interface
function changeQuantityInCart(change_type, order_prod_id) {
qty_id = order_prod_id + "-quantity"
qty_element = document.getElementById(qty_id)

current_qty = parseInt(qty_element.innerHTML)
if (change_type === "add") {
    new_qty = current_qty + 1
} else {
    if (current_qty == 1) {
        return
    }
    new_qty = current_qty - 1
}
qty_element.innerHTML = "" + new_qty + ""
}

$('.change-qty').on('click', function (e) {
    e.preventDefault();

    const path = window.location.pathname

    //Get product id and type of change - add/subtract
    var order_prod_id = $(this).data('orderprod')
    change_type = $(this).attr('id')

    console.log(order_prod_id)
    console.log(change_type)

    $.ajax({
        url: path + '?change_qty=' + order_prod_id,
        type: 'GET',
        data: {
            order_prod_id: order_prod_id,
            change_type: change_type,
        },
        success: function (resp) {
            order_info = resp.data
            updateCart(order_info, order_prod_id)
            console.log("SUCCESS")
        }
        ,
        error: function (xhr, status, error) {
            M.toast({html: "Something went wrong on our end", classes: "red"})
            console.log("ERROR: " + status.message)
        }
    });
});

$('.remove-item').on('click', function (e) {
    e.preventDefault();
    var order_prod_id = $(this).data('orderprod')
    const path = window.location.pathname

    $.ajax({
        url: path + '?remove_from_cart=' + order_prod_id,
        type: 'GET',
        data: {
            order_prod_id: order_prod_id,
        },
        success: function (resp) {
            order_info = resp.data
            updateCart(order_info, order_prod_id)
            removeShoppingCartItem(order_prod_id)
            M.toast({html: "Product was removed from cart", classes: "green"})
        }
        ,
        error: function (xhr, status, error) {
            console.log("ERROR: " + status.message)
            M.toast({html: "Something went wrong on our end", classes: "red"})
        }
    });
})



