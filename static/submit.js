
$("#LocationField").prop("disabled", true);
function send_location() {
    $("#submit").prop("disabled", true);
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    }
}

function showPosition(position) {
    var input_field = document.getElementById("LocationField");
    var current_location = position.coords.latitude + "," + position.coords.longitude;
    input_field.value = current_location;
    $("#submit").prop("disabled", false);
}
