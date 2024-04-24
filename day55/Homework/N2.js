function printInputValues() {
    var inputs = document.querySelectorAll('input');
    inputs.forEach(function(input) {
        console.log(input.id + ": " + input.value);
    });
}