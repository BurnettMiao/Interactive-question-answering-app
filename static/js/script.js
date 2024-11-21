document.addEventListener('DOMContentLoaded', () => {
  const btn = document.querySelector('button');
  btn.addEventListener('click', clickBtn);

  function clickBtn() {
    console.log('Button clicked!!!!');
  }
});
