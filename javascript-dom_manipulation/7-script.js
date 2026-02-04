document.addEventListener('DOMContentLoaded', function () {
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
      const listMovies = document.getElementById('list_movies');

      data.results.forEach(movie => {
        const li = document.createElement('li');
        li.textContent = movie.title;
        listMovies.appendChild(li);
      });
    });
});
