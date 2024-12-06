from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')


# 模擬題目
questions = [
    {"id": 1, "question": "1 + 1 等於多少?", "options": ["1", "2", "3", "4"], "answer": "2", "isUsed": False},
    {"id": 2, "question": "Python 是什麼類型的語言", "options": ["低階語言", "中階語言", "高階語言", "機器語言"], "answer": "高階語言", "isUsed": False},
    {"id": 3, "question": "下列哪個不是國旗的顏色", "options": ["黑色", "白色", "藍色", "紅色"], "answer": "黑色", "isUsed": False},
    {"id": 4, "question": "中華隊拿一年拿下棒球12強冠軍", "options": ["2021", "2023", "2024", "2025"], "answer": "2024", "isUsed": False},
    {"id": 5, "question": "12月25日是什麼重要的節日", "options": ["清明節", "中秋節", "兒童節", "聖誕節"], "answer": "聖誕節", "isUsed": False},
]

# 模擬分數
person_scores = [
    {"name": "小名", "score": 838393},
    {"name": "小黑", "score": 4349993},
    {"name": "小歪", "score": 430013},
    {"name": "小洪", "score": 9393933},
    {"name": "小光", "score": 6582728},
]

users = [
]

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/game')
def game():
    return render_template('game.html')


# ----- test ----
@socketio.on("welcome")
def welcome(data):
    # users.append({"id": request.sid, "name": "小明"})
    print('----------')
    print(data)
    print(f'User connected with ID: {request.sid}')
    users.append({"id": request.sid, "name": data, "score": 0})
    print(users)
    print('----------')
    emit('responseWelcome', f"你好, {data} welcome 加入這個遊戲...")
    emit('redirectToGame', {"url": "/game"})
    print(f'轉跳到 game 頁面 User connected with ID: {request.sid}')


@socketio.on("testMsg")
def forTest(data):
    print('----------')
    print(data)
    newQuestion = filterObj()
    print(f'User connected with ID: {request.sid}')
    print('----------')
    emit("responseMsg", newQuestion)


def filterObj():
    not_in_use = []
    
    for obj in questions:
        if obj["isUsed"] == False:
            not_in_use.append(obj)

    if not not_in_use:
        return "沒有可使用的題目..."
    
    selectedObj = random.choice(not_in_use)
    print('----------')
    print(f'隨機挑選: {selectedObj}')
    print('----------')
    update_questions(selectedObj)
    return selectedObj


def update_questions(obj):
    question_id = obj["id"]
    for obj in questions:
        if obj["id"] == question_id:
            obj["isUsed"] = True
    print('----------')
    print(questions)
    print('----------')

# ----- test ----
    


if __name__ == "__main__":
    # socketio.run(app, debug=True)
    # debug_mode = True
    print("Starting server...")
    socketio.run(app, host="127.0.0.1", port=5000, debug=True)