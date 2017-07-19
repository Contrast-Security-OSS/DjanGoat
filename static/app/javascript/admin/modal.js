"use strict";

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});


function submitForm(user_id) {
    var valuesToSubmit = $("form").serialize();
    $("#editAcct").modal('hide');
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        url: "/admin/" + user_id + "/update_user/",
        headers: {csrfmiddlewaretoken: csrftoken},
        data: valuesToSubmit,
        type: "POST",
        success: function(response) {
            $('#success').show(500).delay(1500).fadeOut();
            loadTable();
        },
        error: function(event) {
            $('#failure').show(500).delay(1500).fadeOut();
        }
    });
}
