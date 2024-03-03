// JavaScript script that fetches from
// https://fourtonfish.com/hellosalut/?lang=fr and displays the value of
// hello from that fetch in the HTML tag DIV#hello.
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

// Wait for the document to be ready before executing the script
$(document).ready(function () {
  // Send a GET request to the specified URL
  $.getJSON(url, function (response) {
    // Update the text content of the <div> with ID 'hello' with the value of 'hello' from the response
    $('DIV#hello').text(response.hello);
  });
});

