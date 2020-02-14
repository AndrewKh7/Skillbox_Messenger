from flask import Flask, request

from datetime import datetime

app = Flask(__name__)

@app.route('/')
def main():
    return 'Welcome!'

@app.route('/status')
def status():
    return{
        'status': True,
        'time': datetime.now().strftime("%d %b %Y %H:%M:%S"),
    }

app.run()