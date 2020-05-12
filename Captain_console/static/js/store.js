//Initialize select elements
document.addEventListener('DOMContentLoaded', function() {
            var elems = document.querySelectorAll('select');
            var instances = M.FormSelect.init(elems);
        });

window.onload = function() {
    $(document).ready(function () {

        /**
         GET request for order by
         */
        $('#orderby').on('change', function (e) {
            e.preventDefault();
            var order_var = orderby.selectedIndex
            console.log(order_var)

            //Check what order variable was pressed
            if (order_var === 1) {
                var order_name = "price"
            } else if (order_var === 2) {
                var order_name = "name"
            } else if (order_var === 3) {
                var order_name = "rating"
            }

            //GET request with product ID's in new order
            $.ajax({
                url: '/store?sort_by=' + order_name,
                type: 'GET',

                success: function (resp) {
                    console.log(resp)
                    console.log(resp.data[0])
                    product_order = resp.data
                    order_products(product_order);
                },
                error: function (xhr, status, error) {
                    // TODO: Show TOASTR
                    console.log(error);
                }
            });
        });

        /**
         GET request for filter by
         */
        $('.filterby').on('change', function (e) {
            e.preventDefault();

            filter_by = $(this).attr("id")
            filter_var = $(this).find('option:selected').text();
            my_filt = $(".filterby").find('option:selected').toArray()

            //Check values of filters
            for (i = 0; i < my_filt.length; i++) {
                my_filt[i] = my_filt[i].innerText
            }

            developer = my_filt[0]
            genre = my_filt[1]
            category = my_filt[2]

            //GET request with product ID's in new order
            $.ajax({
                url: '/store?filter_by=' + filter_var,
                type: 'GET',
                data: {
                    filter_by: filter_by,
                    filter_var: filter_var,
                    developer: developer,
                    genre: genre,
                    category: category
                },
                success: function (resp) {
                    products_filtered = resp.data.map(d => d.id) //Map id's into array
                    filter_products(products_filtered);
                },
                error: function (xhr, status, error) {
                    // TODO: Show TOASTR
                    console.log(error);
                }
            });
        });

        $('#search_product').on('keyup', function (event) {
            // If keypress is 'Enter'
            val = $(this).val()

            $.ajax({
                url: '/store?search_by=' + val,
                type: 'GET',
                success: function (resp) {
                    products_filtered = resp.data.map(d => d.id) //Map id's into array
                    filter_products(products_filtered);
                },
                error: function (xhr, status, error) {
                    // TODO: Show TOASTR
                    console.log(error);
                }
            });
        });

                //Add to cart
        //TODO: Implement for add to cart in product details
        $('.add-to-cart').on('click', function (event) {
            console.log("add to cart")
            var prod_id = $(this).data('prod')
            console.log(prod_id)

             $.ajax({
                url: "/store?add_to_cart=" + prod_id,
                type: "POST",
                data: {prod_id: prod_id},
                success: function(status){
                    console.log("SUCCESS: " + status)
                },
                error: function(status){
                    console.log("ERROR: " + status.message)
                }
            })
        });
    });
}

/**
Orders products in store according to users choise
 */
function order_products(product_order) {
    all_products = document.getElementsByClassName("all_products")
    product_cards = []

    //Get cards in correct order
    for (var i = 0; i < product_order.length; i++) {
        index = product_order[i].id
        product_card = document.getElementById(index)
        product_cards[i] = product_card
    }

    //Empty parent div and append cards in the right order
    all_products[0].innerHTML = ""
    for (var i = 0; i < product_cards.length; i++) {
        all_products[0].appendChild(product_cards[i]);
    }
}

function filter_products(products_filtered) {
    product_cards = $(".product-card")
    product_cards_id = $(".product-card").map(function() { return this.id; }).toArray();
    var empty = 1

    for (var i = 0; i< product_cards_id.length; i++) {
        product_cards_id[i] = parseInt(product_cards_id[i])
    }

    for (var i = 0; i<product_cards.length; i++) {
        product_instance = product_cards_id[i]
        if (products_filtered.includes(product_instance)) { //If instance is in filtered list
            product_cards[i].style.display = 'block'    //Display
            empty = 0
        }
        else {
            product_cards[i].style.display = 'none' //Do not display
        }
    }
}