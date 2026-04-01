document.addEventListener('DOMContentLoaded', function () {
  const list = document.querySelector('.my_list');

  document.querySelector('#add_item').addEventListener('click', function () {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    list.appendChild(newItem);
  });

  document.querySelector('#remove_item').addEventListener('click', function () {
    const lastItem = list.lastElementChild;
    if (lastItem) {
      list.removeChild(lastItem);
    }
  });

  document.querySelector('#clear_list').addEventListener('click', function () {
    list.innerHTML = '';
  });
});
