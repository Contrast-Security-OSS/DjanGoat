message = "For your safety your account number is stored encrypted \
as well as presented to you in an encrypted form\n\nFor your convenience \
, you can decrypt your bank account number at any time using our \
conveniently located decryption function"

function encryptedBankNum() {
    alert(message)
}

/**
 * Function taken from django's documentation
 * https://docs.djangoproject.com/en/1.11/ref/csrf/#ajax
 */
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function deleteDirectDeposit(deposit_id) {
    var tableRow = $(this).parents('tr');
    $.ajax({
        url: "" + deposit_id,
        type: 'delete',
        headers: {'X-CSRFToken': getCookie('csrftoken')},
        success: function () {
            $("#entry"+deposit_id).remove();
            console.log(tableRow)

        }
      });
}

function decryptDirectDeposit() {
    input = $('#decryptAccountInput').val()

    $.ajax({
        url: 'decrypt_bank_account_num',
        type: 'POST',
        data: {
            'account_number': input
        },
        headers: {'X-CSRFToken': getCookie('csrftoken')},
        success: function (response) {
            var td = $("#ddTable td:contains('" + input + "')")
            td.html(response);
            td.css("background-color", "green");
            td.css("color", "white");
        }
      });
}
