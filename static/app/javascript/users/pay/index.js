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

/* Tracks the page currently being viewed, default to 1*/
var currentPage = 1;
var MAX_PAGE_NUM = 1;


/**
 * Hides and displays the table based on the page number passed in
 */
function hideAndDisplayItems(page) {
    $("[class^='page-item-']").css("display", "none");
    $(".page-item-" + page).css("display", "table-row");
    currentPage = page;

    if (currentPage == MAX_PAGE_NUM) {
        $("#nextPageLink").css("display", "none")
    } else {
        $("#nextPageLink").css("display", "list-item")
    }

    if (currentPage == 1) {
        $("#previousPageLink").css("display", "none")
    } else {
        $("#previousPageLink").css("display", "list-item")
    }


}

/**
 * Takes user to next page
 */
function next() {
    if (currentPage < MAX_PAGE_NUM) {
        hideAndDisplayItems(currentPage + 1);
    }
}

/**
 * Takes user to previous page
 */
function previous() {
    if (currentPage > 1) {
        hideAndDisplayItems(currentPage - 1);
    }
}

/**
 * Applies classes to rows on the page depending on how many should be displayed on the page
 * Classes are used to hide/display appropriate items depending on page selected
 */
function applyPageClasses() {
    /* Get the number of items supposed to be on each page */
    numPerPage = $('#itemsPerPageSelect').val();

    var count = 0;
    var pageNum = 1

    /*Add the appropriate page-item-* class where * is the page the item should be on*/
    rows = $('#ddTableBody').children().each( function() {
        $(this).prop('class', "page-item-" + pageNum);
        /*Increase the count of numItems on pageNums page*/
        count = count + 1;

        /*If the number of items added to pageNum is the max it should be, go to next page. a*/
        if (count == numPerPage) {
            count = 0;
            pageNum = pageNum + 1;
        }

    });
}

/**
 * Builds the pagination links at the base of the table
 */
function buildPageLinks() {
    /* Get the number of items supposed to be on each page */
    var numPerPage = $('#itemsPerPageSelect').val();
    /*Get the total number of items in the table*/
    var numItems = $('#ddTableBody tr').length;
    /*Calculate the number of pages there should be*/
    var numPages = Math.ceil(numItems/numPerPage);
    MAX_PAGE_NUM = numPages;

    /*If there should be page links, build them*/
    if (numPages > 1) {
        /*Add previous page link*/
        $('.pagination').html("<li id='previousPageLink' class='page-item'><a class='page-link' onclick='previous()'>Previous</a></li>");

        /*Add a page link for each page that there should be*/
        for (i = 1; i <= numPages; i++) {
            pageLink = "<li class='page-item'><a class='page-link' onclick='hideAndDisplayItems(" + i + ")'>" + i + "</a></li>";
            $('.pagination').append(pageLink);
        }

        /*Add next page link*/
        $('.pagination').append("<li id='nextPageLink' class='page-item'><a class='page-link' onclick='next()'>Next</a></li>");
    } else {
        $('.pagination').html("");
    }
}

function searchFunction() {
    var input, filter, table, tr;
    input = document.getElementById("searchInput");
    filter = input.value;

    table = document.getElementById("ddTableBody");
    tr = table.getElementsByTagName("tr");

    if (filter.length > 0) {
        /* Hide all the table rows. */
        $("[class^='page-item-']").css("display", "none")

        /* Hide the pagination. */
        $(".pagination").css("display", "none");

        /* Loop through all table rows, and hide those who don't match the search query */
        for (var i = 0; i < tr.length; i++) {
            encryptedBankNumTd = tr[i].getElementsByTagName("td")[0];
            routingNumTd = tr[i].getElementsByTagName("td")[1];
            percentDepositTd = tr[i].getElementsByTagName("td")[2];

            var shouldDisplay = false;

            if (encryptedBankNumTd) {
                if (encryptedBankNumTd.innerHTML.trim().startsWith(filter)) {
                    shouldDisplay = true;
                }
            }

            if (routingNumTd) {
                if (routingNumTd.innerHTML.startsWith(filter)) {
                    shouldDisplay = true;
                }
            }

            if (percentDepositTd) {
                if (percentDepositTd.innerHTML.startsWith(filter)) {
                    shouldDisplay = true;
                }
            }

            if (shouldDisplay) {
                $("#" + tr[i].id).css("display", "table-row");
            }
        }
    } else {
        /* Show all rows */
        hideAndDisplayItems(currentPage);
        /* Show pagination */
        $(".pagination").css("display", "flex");
    }

}

function populateTable() {
    applyPageClasses();
    buildPageLinks();
    hideAndDisplayItems(1);
}

$( document ).ready(function() {
    populateTable();
});


