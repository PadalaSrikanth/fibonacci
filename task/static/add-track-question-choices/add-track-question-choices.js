fibonacci = $('#question-div');
function addTrackQuestion(){
    number = $('.number').val()


    $.ajax({
        type: 'POST',
        url: '/fibonacciseries/',
        data: JSON.stringify ({"number":number}), // or JSON.stringify ({name: 'jonas'}),
        contentType: "application/json",
        dataType: 'json',
        success: function(data) {
            var clone = "";
            clone = fibonacci.clone();
            fibonacci.empty()
            clone.css('visibility', 'visible');
            $('.fibanacci').append(clone);
            $('.fibanacci_number').html(data["fibonacci_number"])
            $('.fibanacci_time').html(data["excution_time"])

        }
    });
}


$('input[name="number"]').keyup(function(e)
                                {
  if (/\D/g.test(this.value))
  {
    // Filter non-digits from input value.
    this.value = this.value.replace(/\D/g, '');
  }
});
