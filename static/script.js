document.addEventListener('DOMContentLoaded', () => {
  const socket = io('http://127.0.0.1:5000');
  let currentQuestion = null;
  let username = null;
  const loginBtn = document.querySelector('.login-btn');

  loginBtn.addEventListener('click', login);

  // 登入函式
  function login() {
    username = document.getElementById('username').value;

    if (!username) {
      alert('請輸入用戶名!!');
      return;
    }

    fetch('/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username }),
    })
      .then((response) => response.json())
      .then((data) => {
        alert(data.message);
        document.getElementById('login').style.display = 'none';
        document.getElementById('game').style.display = 'block';

        const joinGameBtn = document.querySelector('join-game-btn');
        joinGameBtn.addEventListener('click', joinGame);
      })
      .catch((error) => console.error('登入失敗', error));
  }

  // 加入遊戲
  function joinGame() {
    if (!username) {
      alert('請先登入!!');
      return;
    }

    socket.emit('join', { username });
  }

  // 接收排行榜更新
  socket.on('update_leaderboard', (leaderboard) => {
    const leaderboardElement = document.getElementById('leaderboard');
    leaderboardElement.innerHTML = '';
    leaderboard.forEach(([user, data], index) => {
      const li = document.createElement('li');
      li.textContent = `${index + 1}. ${user} - ${data.score} 分`;
      leaderboardElement.appendChild(li);
    });
  });

  // 顯示題目
  function displayQuestion(question) {
    currentQuestion = question;
    document.getElementById('question').textContent = question.question;
    const optionsContainer = document.getElementById('options');
    optionsContainer.innerHTML = '';
    question.options.forEach((option) => {
      const button = document.createElement('button');
      button.textContent = option;
      button.onclick = () => submitAnswer(option);
      optionsContainer.appendChild(button);
    });
  }

  // 提交答案
  function submitAnswer(answer) {
    if (!currentQuestion) {
      alert('目前沒有題目');
      return;
    }

    socket.emit('answer', {
      username,
      question_id: currentQuestion.id,
      answer,
    });
  }

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

  // 測試: 顯示假題目
  displayQuestion({
    id: 1,
    question: '1 + 1 等於多少?',
    options: ['1', '2', '3', '4'],
  });
});

// 數字滾動效果
// https://codepen.io/jieli/pen/grGoxJ
// https://inorganik.github.io/countUp.js/
