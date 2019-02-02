$(document).ready(function () {
    function showResults(data) {
      var currentResponse;
      var sentiment;

      if (data == "")
      {
        currentResponse = "";
        sentiment = "";
      }
      else
      {
        var currentResponse = data.split(',', 2)[0].toString()
        var sentiment = data.split(',', 2)[1].toString()
      }

      $('#response').text('Response: ' + currentResponse);
      $('#sentiment').text('Sentiment: ' + sentiment); 
    }

    window.setInterval(function(){
        $.ajax({
            url: "/processResponse",
            type: 'POST',
            success: function(response) {
                showResults(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    }, 1000);   
});