/**
 * JS that fetches and lists all movies title by using a url
 */
$.get('https://swapi.co/api/films/?format=json', function (data) {
  for (let index in data.results) {
    $('UL#list_movies').append('<li>' + data.results[index].title + '</li>');
  }
});
