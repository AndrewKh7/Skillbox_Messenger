import time

from flask import Flask, request

from datetime import datetime

app = Flask(__name__)
messeges = [
    {
        'username': "Jack",
        'text': "SomeText",
        'time': time.time(),
    },
    {
        'username': "Dan",
        'text': "DenSomeText",
        'time': time.time(),
    },
]


@app.route('/')
def main():
    return 'Welcome!'


@app.route('/status')
def status():
    return {
        'status': True,
        'time': datetime.now().strftime("%d %b %Y %H:%M:%S"),
    }


@app.route('/send', methods=['POST'])
def send():
    """
    request: {" username": "str", "text": "str", "time": time.}
    response: {'ok':true}
    """
    data = request.json
    username = data['username']
    text = data['text']
    messeges.append({
        'username': username,
        'text': text,
        'time': time.time(),
    })
    return {'ok': True}


@app.route('/history', methods=['GET'])
def history():
    """
    request: -  last time on client history
    response: {'messeges':{"username": "str", "text": "str", "time": time } ... }
    """
    last_msg_time = float(request.args.get('time'))
    return {'messeges': list(filter(lambda m: m['time'] > last_msg_time, messeges))}


app.run()
