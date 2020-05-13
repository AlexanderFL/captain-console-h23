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

                url: '/?add_item=prod_id/',
                type: 'POST',
                data: {
                    prod_id: order_prod_id,
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


 });
}