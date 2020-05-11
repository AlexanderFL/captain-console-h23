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

            console.log("You are ordering by " + filter_by + " and you're selection is" + filter_var)

                //GET request with product ID's in new order
                $.ajax({
                    url: '/store?filter_by=' + filter_var,
                    type: 'GET',
                    data: {filter_by: filter_by, filter_var: filter_var},
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
    console.log("My filtered ID's")
    console.log(products_filtered)
    console.log("All product ID's");
    product_cards = $(".product-card")
    product_cards_id = $(".product-card").map(function() { return this.id; }).toArray();
    console.log(product_cards_id)

    for (var i = 0; i< product_cards_id.length; i++) {
        console.log(product_cards_id[0])
        console.log(typeof(product_cards_id[0]))
        product_cards_id[i] = parseInt(product_cards_id[i])
    }

    console.log(product_cards_id)

    for (var i = 0; i<product_cards.length; i++) {

        product_instance = product_cards_id[i]
        if (products_filtered.includes(product_instance)) { //If instance is in filtered list

            if (product_cards[i].style.display == 'none') {    //If instance is not filtered out already
            product_cards[i].style.display = 'block'    //Display
            }
        }
        else {
            product_cards[i].style.display = 'none' //Do not display
        }
    }
}

function show_all_products() {
        product_cards = $(".product-card")

        for (var i = 0; i< product_cards.length; i++) {
            product_cards[i].style.display = 'block';
        }
}
