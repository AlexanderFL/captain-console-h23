
// Initializing sidenav-trigger that makes the mobile menu droppable
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, '');
});

// Initializing parallax
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.parallax');
    var instances = M.Parallax.init(elems, '');
});

function locationReplace(val){
    window.location.replace('http://localhost:8000/store/search/' + val)
}

/* These functions are kind whack, but they work*/
$('#search-bar-submit').on('click', function(){
    locationReplace($('#search-bar')[0].value)
});

$('#search-bar').on('keyup', function(event){
    // If keypress is 'Enter'
    if(event.keyCode === 13){
        locationReplace($('#search-bar')[0].value)
    }
});

$('#mobile-search-bar').on('keyup', function(event){
    if(event.keyCode === 13){
        locationReplace($('#mobile-search-bar')[0].value)
    }
});

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