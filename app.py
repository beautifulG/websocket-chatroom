#!/usr/bin/env python3
# coding=utf-8

import os

from flask import Flask, render_template, request, current_app
from flask_socketio import SocketIO, emit, send


app = Flask(
    __name__,
    static_folder="./dist/static",
    template_folder = "./dist",
)
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY", "haha")
socketio = SocketIO(app)


@app.before_first_request
def init_users():
    """初始化 users 对象"""
    current_app.users = {}


@app.route("/")
def index():
    """render html"""
    return render_template("index.html")


@socketio.on("register")
def handle_register_event(nickname):
    """处理注册事件，广播注册消息"""
    current_app.users[request.sid] = nickname
    emit("register", {"nickname": nickname, "id": request.sid}, broadcast=True)


@socketio.on("disconnect")
def handle_disconnect():
    """处理断开连接消息"""
    nickname = current_app.users.get(request.sid)
    if nickname:
        send("quit", {"nickname": nickname, "id": request.sid}, broadcast=True)
    else:
        print("[disconnect]", request.sid)


@socketio.on("quit")
def handle_quit_event():
    """处理退出消息"""
    nickname = current_app.users.get(request.sid)
    if nickname:
        current_app.users.pop(request.sid)
        emit("quit", {"nickname": nickname, "id": request.sid}, broadcast=True)
    else:
        print("[quit]", request.sid)


@socketio.on("msg")
def handle_msg_event(msg):
    """处理消息事件"""
    nickname = current_app.users.get(request.sid)
    data = {
        "nickname": nickname,
        "id": request.sid,
        "msg": msg,
    }
    if nickname:
        emit("msg", data, broadcast=True)
    else:
        print("[msg]", request.sid, msg)

