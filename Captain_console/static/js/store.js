document.addEventListener('DOMContentLoaded', function() {
            var elems = document.querySelectorAll('select');
            var instances = M.FormSelect.init(elems);
        });

//Order by function
window.onload = function(){
    $(document).ready(function(){
        $('#orderby').on('change', function(){
            order_var = orderby.selectedIndex
            console.log(order_var)

            //Order by price
            if (order_var === 1) {


            }



        });
    });
}




/*
var orderby = document.getElementById("orderby")

orderby.addEventListener('change', filter_by_genre);

function filter_by_genre() {
    console.log(orderby.innerText)
    console.log(orderby.options.length)
    console.log(orderby.selectedIndex)
    console.log()
}*/