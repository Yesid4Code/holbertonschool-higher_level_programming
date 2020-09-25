/**
 * JS that fetch from a url and display the value of "hello" that fetch in
 * HTML's tag DIV#hello.
 */
const url = 'https://fourtonfish.com/hellosalut/?lang=fr'
$.get(url, function (data, textStatus) {
  $('DIV#hello').text(data.hello);
});
