document.addEventListener('DOMContentLoaded', function () {
  const addItem = document.getElementById('add_item');
  const list = document.querySelector('ul.my_list');

  addItem.addEventListener('click', function () {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    list.appendChild(newItem);
  });
});
