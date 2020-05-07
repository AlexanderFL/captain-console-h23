
//Allow dropdown in store
var store_dropdown = document.getElementsByClassName(store_dropdown);

store_dropdown.onclick = function(event) {

}


document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.dropdown-trigger');
    var instances = M.Dropdown.init(elems, options);

    instance.open()
  });

$('.dropdown-trigger').dropdown();
