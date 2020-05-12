
window.onload = function() {
    $(document).ready(function () {

        //Add to cart
        //TODO: Implement for add to cart in product details
        $('.add-to-cart').on('click', function (event) {
            console.log("add to cart")

            var prod_id = $(this).data('prod')
            console.log(prod_id)
        });

    });
}