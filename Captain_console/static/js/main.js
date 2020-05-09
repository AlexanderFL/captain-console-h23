
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

/* These functions are kind whack, but they work*/
$('#search-bar-submit').on('click', function(){
    window.location.replace('http://localhost:8000/store/search/' + $('#search-bar')[0].value)
});

$('#search-bar').on('keyup', function(event){
    // If keypress is 'Enter'
    if(event.keyCode === 13){
        window.location.replace('http://localhost:8000/store/search/' + $('#search-bar')[0].value)
    }
});
