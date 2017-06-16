function validation() {
    $("form").validate({
        rules: {
            "password": {
                required: false,
                minlength: 5
            },
            "password-confirmation": {
                required: false,
                minlength: 5,
                equalTo: "#user_password"
            }
        },
        messages: {
            "password": {
                minlength: "Your password must be at least 6 characters long"
            },
            "password_confirmation": {
                minlength: "Your password must be at least 6 characters long",
                equalTo: "Please enter the same password as above"
            }
        },
        highlight: function(label) {
            $("#submit_button").attr('disabled', 'disabled');
            $(label).closest('.control-group').addClass('error');
            $('.error').css({
                "color": "red"
            });
        },
        success: function(label) {
            label.closest('.control-group').addClass('success');
            $("#submit_button").removeAttr('disabled');
            $('.error').css({
                "color": "#333333"
            });
        }
    });
};

$(document).ready(validation());