/**
 * JS that fetch and replaces the name of a url.
 */
$.get('https://swapi.co/api/people/5/?format=json', function (data) {
  $('DIV#character').text(data.name);
});
