document.addEventListener('DOMContentLoaded', function () {
  const redHeader = document.getElementById('red_header');
  const header = document.querySelector('header');

  redHeader.addEventListener('click', function () {
    header.classList.add('red');
  });
});
