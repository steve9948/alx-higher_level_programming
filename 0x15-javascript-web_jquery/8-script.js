// JavaScript script that fetches and lists the title for all movies by using
// this URL: https://swapi-api.alx-tools.com/api/films/?format=json
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.getJSON(url, function (response) {
  // Iterate over each movie in the response
  $.each(response.results, function (i, item) {
    // Append a list item with the movie title to the unordered list
    $('UL#list_movies').append('<li>' + item.title + '</li>');
  });
});

