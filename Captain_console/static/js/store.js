document.addEventListener('DOMContentLoaded', function() {
            var elems = document.querySelectorAll('select');
            var instances = M.FormSelect.init(elems);
        });

$(document).ready(function() {
    // Select - Single
    $('select:not([multiple])').material_select();
});