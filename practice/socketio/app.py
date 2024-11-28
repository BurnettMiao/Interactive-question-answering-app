from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')



# 模擬題目
questions = [
    {"id": 1, "question": "1 + 1 等於多少?", "options": ["1", "2", "3", "4"], "answer": "2", "isUsed": False},
    {"id": 2, "question": "Python 是什麼類型的語言", "options": ["低階語言", "中階語言", "高階語言", "機器語言"], "answer": "高階語言", "isUsed": False}
]

users = {}
leaderboard = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get('username')
    if username not in users:
        users[username] = {"score": 0}
    return jsonify({"message": "登入成功", "username": username})

def update_leaderboard():
    global leaderboard
    leaderboard = sorted(users.items(), key=lambda x: x[1]["score"], reverse=True)

@socketio.on("join")
def handle_join(data):
    username = data["username"]
    if not username or username not in users:
        emit("error", {"message": "請先登入後加入遊戲"}, to=request.sid)
        return 
    print(f"{username} 加入遊戲")
    emit("update_leaderboard", leaderboard, broadcast=True)

@socketio.on("answer")
def handle_answer(data):
    username = data.get("username")
    if not username or username not in users:
        emit("error", {"message": "請先登入後才能回答問題"}, to=request.sid)
        return
    
    question_id = data["question_id"]
    answer = data["answer"]
    question = next((q for q in questions if q["id"] == question_id), None)
    if not question:
        emit("error", {"message": "無效的問題 ID"}, to=request.sid)

    if question["answer"] == answer:
        users[username] += 10
        update_leaderboard()

    emit("update_leaderboard", leaderboard, broadcast=True)

# ----- test ----
@socketio.on("welcome")
def welcome(data):
    print(data)
    emit('responseWelcome', "你好, welcome 加入這個遊戲...")

@socketio.on("testMsg")
def forTest(data):
    print(data)
    response = {"message": "從後端回丟的訊息..."}

    newQuestion = filterObj()

    emit("responseMsg", newQuestion)
    
def filterObj():
    newList = []
    for obj in questions:
        if obj["isUsed"] == False:
            print(obj)
            newList.append(obj)
            obj["isUsed"] = True
        else:
            return "沒有可使用的題目..."
    
    return newList

# ----- test ----
    




if __name__ == "__main__":
    # socketio.run(app, debug=True)
    # debug_mode = True
    print("Starting server...")
    socketio.run(app, host="127.0.0.1", port=5000, debug=True)