from flask import Flask, render_template, request, url_for, redirect #flask library used to make web app
# from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, join_room


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# db = SQLAlchemy(app)
socketio = SocketIO(app)

#sqlalchamey db
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=True, nullable=False)
#     description = db.Column(db.String(120))


@app.route('/')
def home():
    '''
    This is the index/home page when the web page is first opened.
    '''
    return render_template('index.html')

@app.route('/chat')
def chat():
    '''
    This will handle the username and roomid infor and move you into the correct room
    '''

    #pull the username and roomid that is entered, you can find it in the index.html 
    username = request.args.get('username')
    roomid = request.args.get('roomid')

    if username and roomid:
        return render_template('chat.html',username=username, roomid=roomid) #passed into it username and roomid
    else:
        return redirect(url_for('home')) #'render_template(url_for('index')) is the same as just redirect('/')


#handles the join_room event that is created from the chat.html file 
@socketio.on('join_room')
def handle_join_room_event(data):
    app.logger.info("{} has joined the room {}".format(data['username'], data['roomid']))
    join_room(data['roomid']) # method from flask_socketio that creates a room with id
    
    # Creates an event and announces it, will catch it in the chat.html file
    socketio.emit('join_room_announcement', data)
    

#just a main that will call you app and run it        
if __name__ == '__main__':
    # app.run(debug=True) #instead of just running the app
    socketio.run(app,debug=True,port = 5001) #make sure to pass app into it as well.
