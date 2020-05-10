
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