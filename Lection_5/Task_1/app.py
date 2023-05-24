from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, send, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)

users = {}
chat_rooms = set()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        users[username] = session.get('flask_session_id')
        return render_template('chat.html', username=username)
    return render_template('login.html')

@socketio.on('message')
def handle_message(message):
    username = session['username']
    send(username + ': ' + message, room=session['room'])

@socketio.on('join')
def join(data):
    username = session['username']
    room = data['room']
    session['room'] = room
    join_room(room)
    send(username + ' joined the room ' + room, room=room)

@socketio.on('leave')
def leave(data):
    username = session['username']
    room = session['room']
    leave_room(room)
    send(username + ' left the room ' + room, room=room)

if __name__ == '__main__':
    socketio.run(app)
