from flask import Flask
import socket

app1 = Flask(__name__)
Counter=0

@app1.route('/')
def home():
    global Counter
    Counter+=1
    return f"Container ID: {socket.gethostname()} Request {Counter}"

if __name__ == '__main__':
    Counter=0
    app1.run(debug=True, host='0.0.0.0')