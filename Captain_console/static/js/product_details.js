//Initialize select elements
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);
});

function update_ratings() {
    //Updates ratings
    $('.star').prop('disabled',true)
    stars = document.getElementsByClassName("star")
    rating = $('#stars').data('average')
    rounded_rating = Math.round(rating)

    for (var i = 0; i < rounded_rating; i++) {
        star = stars[i];
        star.classList.add("fill")
    }
}

// Appends the nr of copies sold to the element with the id #copies-sold-nr
function get_copies_sold(){
    $.ajax({
        url: '?copies_sold=true',
        type: 'GET',
        success : function(response){
            $("#copies-sold-nr").append(response.message)
        }
    })
}

window.onload = function() {
    $(document).ready(function () {
        get_copies_sold();
        update_ratings();

        //Turn stars into rating buttons
        $('#give-review').on("click", function (e) {
            e.preventDefault();

            $('#give-review').prop('disabled', true)
            $('#give-review').addClass('disabled', true)
            $('.star').prop('disabled',false)
            $('.star').removeClass('fill')
            $('.star').addClass('rate')
        });

        //Give review
        $('.star').on('click', function (e) {
            e.preventDefault();

            let prod_id = $(this).data('prod')
            let rating = $(this).data('rate')
            let count = $('#rating-count').data('current-count') + 1

            console.log(count)

            $.ajax({
                url: "/store/" + prod_id + "?review_product=" + prod_id,
                type: "POST",
                data: {prod_id: prod_id, rating: rating},
                success: function(status){
                    M.toast({html: "Rating was submitted, thank you.", classes: "green"})
                    console.log("SUCCESS: " + status)
                },
                error: function(status){
                    M.toast({html: "Something went wrong on our end", classes: "red"})
                    console.log("ERROR: " + status.message)
                }
            })
            update_ratings();
            $('#give-review').prop('disabled', false)
            $('#give-review').removeClass('disabled')
            $('#rating-count').html("(" + count + ")")
        });


        //Add to cart
        //TODO: Implement for add to cart in product details
        $('.add-to-cart').on('click', function (e) {
            e.preventDefault()
            console.log("add to cart")
            var prod_id = $(this).data('prod')
            console.log(prod_id)
            var csrftoken = getCookie('csrftoken');

            //No quantity set, only "add to cart"
            var quantity = 1

             $.ajax({
                url: "/store/?add_to_cart=" + prod_id,
                type: "POST",
                data: {prod_id: prod_id, quantity: quantity},

                success: function(response){
                    if (response.status === 999){
                        window.location.replace(response.message)
                    }
                    console.log(this.url)
                    console.log("SUCCESS: " + response)
                    M.toast({html: "Product was added to cart", classes: "green"})

                },
                error: function(status){
                    console.log("ERROR: " + status.message)
                    M.toast({html: "Something went wrong on our end", classes: "red"})

                }
            })
        });
    });
}