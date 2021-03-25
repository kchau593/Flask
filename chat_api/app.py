from flask import Flask, render_template, request, url_for, redirect #flask library used to make web app
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

#sqlalchamey db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))


@app.route('/')
def index():
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
        return render_template(url_for('index')) #'render_template(url_for('index')) is the same as just redirect('/')

#just a main that will call you app and run it        
if __name__ == '__main__':
    app.run(debug=True)
