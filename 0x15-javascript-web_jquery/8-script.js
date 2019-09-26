$.getJSON('https://swapi.co/api/films/?format=json', function (body) {
  for (const film of body.results) {
    $('ul#list_movies').append('<li>' + film.title + '</li>');
  }
});
