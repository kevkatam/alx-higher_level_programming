const $ = window.$;
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, textStatus) {
  const movies = data.results;
  for (let i =0; i < movies.length; i++) {
    $('UL#list_movies').append('<li>' + movies[i].title + '</li>');
  }
});
