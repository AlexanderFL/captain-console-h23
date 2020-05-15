$("#write-review").on("click", function() {
    input_box = document.getElementById("review-input")
    write_review = document.getElementById("write-review")
    if (input_box.style.display == "block") {
            input_box.style.display = "none";
            write_review.innerHTML = `<i class="material-icons left">mode_edit</i>Write review`
    }
    else {
        input_box.style.display = "block";
        write_review.innerHTML = `<i class="material-icons left">close</i>Cancel`
    }
})

$("#submit-review").on("click", function() {
    prod_id = $(this).data("prod")
    comment = document.getElementById("comment").value
    stars = document.getElementById("select-stars").selectedIndex

    if (comment == "") {
        M.toast({html: "Please write your review", classes: "red"})
        return
    }
    if (stars == "") {
        M.toast({html: "Please choose your rating", classes: "red"})
        return
    }

      $.ajax({
        url:'?review_product=' + prod_id,
        type: 'GET',
        data: {
            prod_id: prod_id,
            comment: comment,
            stars: stars,
        },
        success: function (status, resp) {
            message = status.message
            console.log(message)
            if (message == "Updated") {
            M.toast({html: "Your review and rating for this product has been updated.", classes: "green"})
            }
            else if (message == "Created") {
                M.toast({html: "Thank you for your review", classes: "green"})
            }
        }
        ,
        error: function (xhr, status, error) {
            console.log("ERROR: " + status.message)
            M.toast({html: "There is something wrong on our end.", classes: "red"})
        }
    });
    console.log(comment)
})
