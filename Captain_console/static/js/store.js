//Initialize select elements
document.addEventListener('DOMContentLoaded', function() {
            var elems = document.querySelectorAll('select');
            var instances = M.FormSelect.init(elems);
        });

// When user searches from navbar, checks the params sent and if
// it includes ?search=64, it will fill the search bar with the value
function fill_search_bar(){
    let params = window.location.search.substr(1);
    let params_s = params.split("=")
    if(params_s[0] === "search"){
        $("#search_product").val(decodeURI(params_s[1]))
        $("#search_product").keyup()
    }
    M.updateTextFields();
}

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
                    product_order = resp.data
                    order_products(product_order);
                },
                error: function (xhr, status, error) {
                    console.log(error);
                }
            });
        });

        /**
         GET request for filter by
         */
        $('.filterby').on('change', function (e) {
            e.preventDefault();

           // const csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value

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
               // headers: {"X-CSRFToken": csrf_token},
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
                    console.log(error);
                }
            });
        });

        let no_product_found = false
        $('#search_product').on('keyup', function (event) {
            // If keypress is 'Enter'
            val = $(this).val()

            $.ajax({
                url: '/store?search_by=' + val,
                type: 'GET',
                success: function (resp) {
                    products_filtered = resp.data.map(d => d.id) //Map id's into array

                    if (products_filtered.length === 0) {
                        if(!no_product_found){
                            M.toast({html: "No products found", classes: "red"})
                            no_product_found = true
                        }
                    }else{
                        no_product_found = false
                    }
                    filter_products(products_filtered);
                },
                error: function (xhr, status, error) {
                    console.log(error);
                }
            });
        });

        //Add to cart
        $('.add-to-cart').on('click', function (e) {
            e.preventDefault()
            console.log("add to cart")
            var prod_id = $(this).data('prod')
            console.log(prod_id)
            var csrftoken = getCookie('csrftoken');

            //No quantity set, only "add to cart"
            var quantity = 1

             $.ajax({
                url: "?add_to_cart=" + prod_id,
                type: "POST",
                data: {prod_id: prod_id, quantity: quantity},

                success: function(resp, status){
                    if (resp.status === 999){
                        window.location.replace(resp.message)
                    }
                    console.log(this.url)
                    console.log("SUCCESS: " + status)
                    M.toast({html: "Product was added to cart", classes: "green"})
                },
                error: function(status){
                    M.toast({html: "Something went wrong on our end", classes: "red"})
                    console.log("ERROR: " + status.message)
                }
            })
        });
        fill_search_bar();
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