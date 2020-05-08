document.addEventListener('DOMContentLoaded', function() {
            var elems = document.querySelectorAll('select');
            var instances = M.FormSelect.init(elems);
        });

//Order by function
window.onload = function(){
    $(document).ready(function() {
        $('#orderby').on('change', function (e) {
            e.preventDefault();
            var order_var = orderby.selectedIndex
            console.log(order_var)

            var order_name = "price"
            //Order by price
            console.log("filtering by " + order_name)

            $.ajax({
                url: '/store?sort_by=' + order_name,
                type: 'GET',
                success: function (resp) {
                    console.log(resp)
                    var newHtml = resp.data.map(d => {
                        return `<div>Hello</div>`
                    });
                    $('.all_products').html(newHtml.join(''));
                },
                error: function (xhr, status, error) {
                    // TODO: Show toastr
                    console.log(error);
                }
            });
        });
    });
};






/*
var orderby = document.getElementById("orderby")

orderby.addEventListener('change', filter_by_genre);

function filter_by_genre() {
    console.log(orderby.innerText)
    console.log(orderby.options.length)
    console.log(orderby.selectedIndex)
    console.log()
}*/