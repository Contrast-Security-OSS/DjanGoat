"use strict";

function submitForm(user_id) {
    var valuesToSubmit = $("form").serialize();
    $("#editAcct").modal('hide');

    $.ajax({
        url: "/admin/" + user_id + "/update_user/",
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

function deleteUser(user_id) {
    $.ajax({
        url: "/admin/" + user_id + "/delete_user/",
        type: "POST",
        success: function(response) {
            $('#success').show(500).delay(1500).fadeOut();
            loadTable()
        },
        error: function(event) {
            $('#failure').show(500).delay(1500).fadeOut();
        }
    });
}