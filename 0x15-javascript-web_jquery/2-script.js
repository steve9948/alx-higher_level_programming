// JavaScript script that updates the text color of the <header> element to red 
// when the user clicks on the tag DIV#red_header
$('DIV#red_header').click(function () {
  $('header').css('color', 'red');
});
