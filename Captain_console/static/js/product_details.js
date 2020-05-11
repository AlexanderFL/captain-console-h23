//Initialize select elements
document.addEventListener('DOMContentLoaded', function() {
            var elems = document.querySelectorAll('select');
            var instances = M.FormSelect.init(elems);
        });


function update_ratings() {
    //Updates ratings
    $('.star').prop('disabled',true)
    stars = document.getElementsByClassName("star")

    console.log("updating")
    for (var i = 0; i < rounded_rating; i++) {
        star = stars[i];
        star.classList.add("fill")
    }
}

window.onload = function() {
    $(document).ready(function () {

        console.log(location.pathname.slice(-1))

        stars = document.getElementsByClassName("star")
        rating = $('#stars').data('average')
        rounded_rating = Math.round(rating)
        console.log(rating)
        console.log(rounded_rating)

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

            var prod_id = $(this).data('prod')
            var rating = $(this).data('rate')
            var count = $('#rating-count').data('current-count') + 1

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

/*function give_review () {
     console.log("hello")
            var id = $(this).data("prod")
            var rating = $(this).data("rating")

            console.log(id)
            console.log(typeof(id))

            $.ajax({
                url: "/get_product_by_id?review_product=" + toString(id),
                type: "POST",
                data: {product: id, rating: rating}
            })

            console.log("hello")
            console.log($(this).data("rate"))
            alert("Your values are: " + $(this).data("rate") + $(this).data("prod"))

}*/

   /*$.ajax({
                url: "/get_product_by_id?review_mode=" + product,
                data: {id: product},
                type: "GET",
                success: function (resp) {
                    var newHtml = resp.data.map(d => {
                        return `<button class="star" data-rate="1" data-prod="${d.id}"><i class="material-icons">star</i></button>
                                <button class="star" data-rate="2" data-prod="${d.id}"><i class="material-icons">star</i></button>
                                <button class="star" data-rate="3" data-prod="${d.id}"><i class="material-icons">star</i></button>
                                <button class="star" data-rate="4" data-prod="${d.id}"><i class="material-icons">star</i></button>
                                `
                    });
                    document.getElementById("stars").innerHTML = newHtml
                    give_review_btn = document.getElementById("give_review")
                    give_review_btn.disabled = true;   //Grey out button while in review mode
                    give_review_btn.classList.add("disabled")

                },
                error: function (xhr, status, error) {
                    // TODO: Show toastr
                    console.error(error);
                }
            });*/