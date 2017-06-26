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
        success: function (response, status, xhr) {
            var success = xhr.getResponseHeader("success")
            if (success == "True") {
                var td = $(".accNum:contains('" + input + "')");
                td.html(response);
                td.css("background-color", "green");
                td.css("color", "white");
            } else {
                $('#decryptAccountInput').val("");
                alert("Error: you do not have the inputted encrypted account number associated with this accounts");
            }
        }
      });
}

var currentPage = 1;


/**
 * Populates the table based on the data passed in,
 * the page number being clicked, and the number of items on a page.
 */
function populateTable(page) {
    $("[class^='page-item-']").css("display", "none");
    $(".page-item-" + page).css("display", "table-row");
    currentPage = page;

}

function next() {
    populateTable(currentPage + 1);
}

function previous() {
    populateTable(currentPage - 1);
}

$( document ).ready(function() {
    populateTable(1);
});
