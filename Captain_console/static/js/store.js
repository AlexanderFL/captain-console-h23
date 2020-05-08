document.addEventListener('DOMContentLoaded', function() {
            var elems = document.querySelectorAll('select');
            var instances = M.FormSelect.init(elems);
        });

$(document).ready(function(){
    $('.orderby').change(function(){
        alert('Change detected')
    });
});

/*
var orderby = document.getElementById("orderby")

orderby.addEventListener('change', filter_by_genre);

function filter_by_genre() {
    console.log(orderby.innerText)
}*/