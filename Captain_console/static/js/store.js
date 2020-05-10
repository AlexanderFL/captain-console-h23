//Initialize select elements
document.addEventListener('DOMContentLoaded', function() {
            var elems = document.querySelectorAll('select');
            var instances = M.FormSelect.init(elems);
        });

window.onload = function() {
    $(document).ready(function () {

        //Order by function
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

            console.log("filtering by " + order_name)

            //Send ajax request with variable to order by
            $.ajax({
                url: '/store?sort_by=' + order_name,
                type: 'GET',
                success: function (resp) {
                    console.log(resp)
                    console.log(resp.data[0].id)

                    product_order = resp.data
                    order_products(product_order);

                },
                error: function (xhr, status, error) {
                    // TODO: Show TOASTR
                    console.log(error);
                }
            });
        });
    });
}

function order_products(product_order) {

    all_products = document.getElementsByClassName("all_products")
    product_cards = []

    for (var i = 0; i < product_order.length; i++) {
        index = product_order[i].id
        product_card = document.getElementById(index)
        product_cards[i] = product_card
    }

    all_products[0].innerHTML = ""

    for (var i = 0; i < product_cards.length; i++) {
        all_products[0].appendChild(product_cards[i]);
    }
}




/*

<div class="col s2 m6 store-product" id="singleprod">
                                    <div class="card">
                                        <div class="card-image">
                                            <a href="/store/${d.id}"><img class="product-img" src="${d.path}" alt="${d.productphoto}" width="172rem" height="172rem"/></a>
                                            <a class="btn-floating halfway-fab waves-effect waves-light blue btn-large" ><i class="material-icons">add_shopping_cart</i></a>
                                        </div>
                                        <div class="card-stacked">
                                            <div class="card-content">
                                                <a href="/store/${d.id}"><div id="product-title"  >${d.name}</div></a>
                                                <div id="product-price">${d.price}</div>
                                            </div>
                                        </div>
                                    </div>
                                </div>*/
/*


`<a href=/store/${d.id}">
                                    <div class="card">
                                        <div class="card-image"> <!-- class never used -->
                                            {% if ${d.discount} > 0 %}
                                                <div class="tag">-${d.discounted_price}%</div>
                                            {% endif %}
                                            <img class="product-img" src="${d.path}" alt="${d.alt_val}">
                                            <a class="btn-floating halfway-fab waves-effect waves-light blue btn-large" ><i class="material-icons">add_shopping_cart</i></a>
                                        </div>

                                        <div class="card-stacked">
                                            <div class="card-content">
                                                <a href="href=/store/${d.id}">
                                                    <span class="card-title activator grey-text text-darken-4">${d.name} </span>
                                                </a>
                                                {% if product.discount <= 0 %}
                                                    <strong class="flow-text set-price">${d.price}</strong>
                                                {% else %}
                                                    <strong class="flow-text">
                                                        <span class="set-price">
                                                             ${d.discounted_price}
                                                        </span>
                                                        <span class="discount">
                                                            <sup>${ d.price }</sup>
                                                        </span>
                                                    </strong>
                                                {% endif %}
                                            </div>
                                        </div>
                                    </div>
                                </a>`*/


/*

                    var newHtml = resp.data.map(d => {
                        return `<a href=/store/${d.id}">
                                    <div class="card">
                                        <div class="card-image">
                                            {% if ${d.discount} > 0 %}
                                                <div class="tag">-${d.discounted_price}%</div>
                                            {% endif %}
                                            <img class="product-img" src="${d.path}" alt="${d.alt_val}">
                                            <a class="btn-floating halfway-fab waves-effect waves-light blue btn-large" ><i class="material-icons">add_shopping_cart</i></a>
                                        </div>

                                        <div class="card-stacked">
                                            <div class="card-content">
                                                <a href="href=/store/${d.id}">
                                                    <span class="card-title activator grey-text text-darken-4">${d.name} </span>
                                                </a>
                                                {% if product.discount <= 0 %}
                                                    <strong class="flow-text set-price">${d.price}</strong>
                                                {% else %}
                                                    <strong class="flow-text">
                                                        <span class="set-price">
                                                             ${d.discounted_price}
                                                        </span>
                                                        <span class="discount">
                                                            <sup>${ d.price }</sup>
                                                        </span>
                                                    </strong>
                                                {% endif %}
                                            </div>
                                        </div>
                                    </div>
                                </a>`
                                            console.log(newHtml)

                    });
                    //$('.all_products').html(newHtml.join(''));*/
