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

        $('#remove-item').on('click', function (e) {
            e.preventDefault();
            var order_prod_id = $(this).data('orderprod')
            const path = window.location.pathname

            console.log("Deleting product")
            console.log(window.location.pathname)
               $.ajax({
                url: path + '?remove_from_cart=' + order_prod_id,
                type: 'GET',
                data: {
                    order_prod_id: order_prod_id,
                },
                success: function (status) {
                    console.log("SUCCESS: " + status)
                    var order_prod_id = $(this).data('orderprod')
                    console.log($(this).outerHTML)
                    remove_shopping_cart_item(order_prod_id)
                }
                ,
                error: function (xhr, status, error) {
                    console.log("ERROR: " + status.message)
                }
            });
        })
    });
}

function remove_shopping_cart_item(order_prod_id) {
    order_products = document.getElementsByClassName("order-product-card")

    for (i = 0; i < order_products.length; i++) {
        order_product = order_products[i]
        console.log(order_product)
        card_id = order_product.data('product')

        console.log(order_product)

        if (card_id == order_prod_id) {
            order_products[i].style.display = 'none' //Do not display
            console.log("I'm removing shopping cart item from view")
        }
    }
}
