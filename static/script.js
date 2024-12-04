document.addEventListener('DOMContentLoaded', () => {
  const socket = io('http://127.0.0.1:5000');
  let currentQuestion = null;
  let username = null;
  const loginBtn = document.querySelector('.login-btn');

  loginBtn.addEventListener('click', () => {
    console.log('Login Button clicked!!!');
  });

  // ----- test -----
  const testBtn = document.querySelector('.test-btn');
  testBtn.addEventListener('click', () => {
    socket.emit('testMsg', {
      message: '這是測試訊息~',
    });
  });

  socket.emit('welcome', '新用戶加入~');
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
