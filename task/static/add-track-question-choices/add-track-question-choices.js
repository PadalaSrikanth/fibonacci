
function addTrackQuestion(){
number = $('.number').val()
console.log(number)
$.ajax({
    type: 'POST',
    url: '/fibonacciseries/',
    data: JSON.stringify ({"number":number}), // or JSON.stringify ({name: 'jonas'}),
    contentType: "application/json",
    dataType: 'json',
    success: function(data) {
        alert('fibonacci_number: ' + data["fibonacci_number"]);
    }
});
}
