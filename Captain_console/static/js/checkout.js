// Initializing date picker
//  document.addEventListener('DOMContentLoaded', function() {
//     var elems = document.querySelectorAll('.datepicker');
//     var instances = M.Datepicker.init(elems, options);
//   });


window.onload = function() {
    $(document).ready(function () {
        $('#add-item').on('click', function (e) {
            e.preventDefault();
            var order_prod_id = $(this).data('prod')

            console.log("hello")
            //GET request with product ID's in new order
            $.ajax({

                url: '/?add_item=prod' + order_prod_id,
                type: 'GET',
                data: {
                    order_prod_id: order_prod_id,
                },
                success: function (status) {
                    console.log("SUCCESS: " + status)
                }
                ,
                error: function (xhr, status, error) {
                    console.log("ERROR: " + status.message)
                }
            });
        });

        $('.remove-item').on('click', function (e) {
            e.preventDefault();
            var order_prod_id = $(this).data('orderprod')
            const path = window.location.pathname
            console.log("The product that's not going to be visible is:")
            var order_prod_id = $(this).data('orderprod')
            console.log(order_prod_id)

            console.log("Deleting product")
            console.log(window.location.pathname)
               $.ajax({
                url: path + '?remove_from_cart=' + order_prod_id,
                type: 'GET',
                data: {
                    order_prod_id: order_prod_id,
                },
                success: function (resp, status) {
                    console.log("SUCCESS: " + status)
                    remove_shopping_cart_item(order_prod_id)
                    M.toast({html: "Product was removed from cart", classes: "green"})
                }
                ,
                error: function (xhr, status, error) {
                    console.log("ERROR: " + status.message)
                    M.toast({html: "Something went wrong on our end", classes: "red"})
                }
            });
        })
    });
}

function remove_shopping_cart_item(order_prod_id) {
    // order_products = document.getElementsByClassName("order-product-card")

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

