document.addEventListener('DOMContentLoaded', () => {
  const socket = io('http://127.0.0.1:5000');
  const loginBtn = document.querySelector('.login-btn');

  loginBtn.addEventListener('click', () => {
    console.log('Login Button clicked!!!');
    const userInput = document.querySelector('.login-input');
    const userName = userInput.value.trim();

    if (userName === '') {
      warnUser();
      return;
    }

    socket.emit('welcome', userName);

    console.log(userName);
    userInput.value = '';
  });

  function warnUser() {
    const inputContainer = document.querySelector('.input-container');
    inputContainer.classList.add('active');

    setTimeout(() => {
      inputContainer.classList.remove('active');
    }, 2000);
  }

  socket.on('redirectToGame', (data) => {
    window.location.href = data.url;
  });

  // ----- test -----
  const testBtn = document.querySelector('.test-btn');
  testBtn.addEventListener('click', () => {
    socket.emit('testMsg', {
      message: '這是測試訊息~',
    });
  });

  socket.on('responseWelcome', (data) => {
    console.log(data);
  });

  socket.on('responseMsg', (data) => {
    console.log(typeof data);
    if (typeof data === 'string') {
      console.log(data);
    } else {
      console.log(data);
    }
  });
  // ----- test -----
});

// 數字滾動效果
// https://codepen.io/jieli/pen/grGoxJ
// https://inorganik.github.io/countUp.js/
