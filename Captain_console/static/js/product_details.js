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

    console.log("updating")
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
                    console.log("SUCCESS: " + status)
                },
                error: function(status){
                    console.log("ERROR: " + status.message)
                }
            })
            update_ratings();
            $('#give-review').prop('disabled', false)
            $('#give-review').removeClass('disabled')
            $('#rating-count').html("(" + count + ")")
        });
    });
}