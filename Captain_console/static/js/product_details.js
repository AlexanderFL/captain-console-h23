//Initialize select elements
document.addEventListener('DOMContentLoaded', function() {
            var elems = document.querySelectorAll('select');
            var instances = M.FormSelect.init(elems);
        });

window.onload = function() {
    $(document).ready(function () {
        //Turn stars into rating buttons
        $('#give-review').on("click", function (e) {
            e.preventDefault();

            var product = $(this).data("prod")

            give_review_btn = document.getElementById("give-review")
            give_review_btn.disabled = true;   //Grey out button while in review mode
            give_review_btn.classList.add("disabled")
        });

        //Give review
        $('.star').on('click', function (e) {
            e.preventDefault();

            var prod_id = $(this).data("prod")
            var rating = $(this).data("rating")

            alert("Your values are: " + $(this).data("rate") + $(this).data("prod"))

            $.ajax({
                url: "/store/" + prod_id + "?review_product=" + prod_id,
                type: "POST",
                data: {product: prod_id, rating: rating},
                success: function(status){
                    console.log("SUCCESS: " + status)
                },
                error: function(status){
                    console.log("ERROR: " + status.message)
                }
            })
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