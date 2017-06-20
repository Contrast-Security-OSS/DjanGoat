// Get the modal
var modal = document.getElementById('credentialModal');

// Get the button that opens the modal
var btn = document.getElementById("tutorialBtn");

    // Get the hidden credentials
var hidden = document.getElementById("creds_hidden")

// Get the <span> element that closes the modal with the x in the corner
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
function hideModal() {
    modal.style.display = "none";
    hidden.style.display = "none";
}

// When the user clicks on the button, open the modal
function showModal() {
    modal.style.display = "block";
}

// Get the <span> element that shows the credentials with the "I Understand" button
var btn2 = document.getElementsByClassName("btn btn-primary")[1];

// When the user clicks on <span> "I Understand", show modal that has credentials
function showHidden() {
    hidden.style.display = "block";
}

// When the user clicks anywhere outside of the modal, close it
//window.onclick = function(event) {
//    if (event.target == modal) {
//        modal.style.display = "none";
//        hidden.style.display = "none";
//    }
//}

//ScrollUp
 $(function () {
    $.scrollUp({
    scrollName: 'scrollUp', // Element ID
    topDistance: '300', // Distance from top before showing element (px)
    topSpeed: 300, // Speed back to top (ms)
    animation: 'fade', // Fade, slide, none
    animationInSpeed: 400, // Animation in speed (ms)
    animationOutSpeed: 400, // Animation out speed (ms)
    scrollText: 'Scroll to top', // Text for element
    activeOverlay: false, // Set CSS color to display scrollUp active point, e.g '#00FFFF'
  });
});

//Dropdown
$('.dropdown-toggle').dropdown();