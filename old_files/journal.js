$(document).ready(function() {
    $("#run-python").click(function() {
        $.ajax({
            url: 'book_journal.py',
            type: 'GET',
            success: function(data) {
                $("#output").html(data);
            },
            error: function(error) {
                $("#output").html('Error: ' + error.responseText);
            }
        });
    });
});