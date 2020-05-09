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
                    var newHtml = resp.data.map(d => {
                        return `<div class="col s2 m6 store-product" id="singleprod">
                                    <div class="card">
                                        <div class="card-image">
                                            <a href="/store/${d.id}"><img class="product-img" src="${d.firstPath}" alt="${d.firstAlt}" width="172rem" height="172rem"/></a>
                                            <a class="btn-floating halfway-fab waves-effect waves-light blue btn-large" ><i class="material-icons">add_shopping_cart</i></a>
                                        </div>
                                        <div class="card-stacked">
                                            <div class="card-content">
                                                <a href="/store/${d.id}"><div id="product-title"  >${d.name}</div></a>
                                                <div id="product-price">${d.price}$</div>
                                            </div>
                                        </div>
                                    </div>
                                </div>`
                    });
                    $('.all_products').html(newHtml.join(''));
                },
                error: function (xhr, status, error) {
                    // TODO: Show TOASTR
                    console.log(error);
                }
            });
        });
    });
}



