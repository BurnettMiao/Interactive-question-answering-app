from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# 模擬題目
questions = [
    {"id": 1, "question": "1 + 1 等於多少?", "options": ["1", "2", "3", "4"], "answer": "2"},
    {"id": 2, "question": "Python 是什麼類型的語言", "options": ["低階語言", "中階語言", "高階語言", "機器語言"], "answer": "高階語言"}
]

users = {}
leaderboard = []

@app.route("/login", emthods=["POST"])
def login():
    data = request.json
    username = data.get('username')
    if username not in users:
        users[username] = {"score": 0}
    return jsonify({"message": "登入成功", "username": username})

@socketio.on("join")
def handle_join(data):
    username = data["username"]
    print(f"{username} 加入遊戲")
    emit("update_leaderboard", leaderboard, broadcast=True)

@socketio.on("answer")
def handle_answer(data):
    username = data["username"]
    question_id = data["question_id"]
    answer = data['answer']

    question = next(q for q in questions if q["id"] == question_id)
    if question["answer"] == answer:
        users[username]["score"] += 10

    # 更新排行榜
    leaderboard.clear()
    leaderboard.extend(sorted(users.items(), key=lambda x: x[1]["score"], reverse=True))

    emit("update_leaderboard", leaderboard, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, debug=True)