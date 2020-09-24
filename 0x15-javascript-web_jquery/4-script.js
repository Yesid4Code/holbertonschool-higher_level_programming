/**
 * Toogles the class of the HTML tag Header to red.
 * When the user cliks on the tag DIV#toggle_header
 */
$('DIV#toggle_header').click(function () {
  $('header').toggleClass('red green');
});
