from flask import Flask, render_template
import time
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/pucsd')
def pucsd():
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)

    hostname = socket.gethostname()

    return render_template('about.html',gettime=curr_clock, hname=hostname)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')