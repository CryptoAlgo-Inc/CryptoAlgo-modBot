from flask import Flask
from threading import Thread
import time

app = Flask('CryptoAlgo Bot')

startTime = 0
profanitiesDeleted = 0
receivedMsgs = 0

@app.route('/')
def main():
    global profanitiesDeleted
    global startTime
    rawMS = (time.time() - startTime)*1000
    s, ms = divmod(rawMS, 1000)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    return '''
    <style> body {
        font-family: verdana
    }
    </style>
    <script>
    setTimeout(countDown, 1000);
    var timeLeft = 20;
    function countDown() {
        timeLeft --;
        if(timeLeft < 0) {
            window.location = window.location;
        }
        else {
            document.getElementById("reloadTime").innerHTML = 'Next reload in: ' + timeLeft + ' seconds';
            setTimeout(countDown, 1000);
        }
    }
    </script>
    <h1>I'm Alive!<br />CryptoAlgo Mod Bot</h1>
    <h2>Statistics</h2><hr>
    <p>Profanities Deleted: ''' + str(profanitiesDeleted) + '''</p>
    <p>Uptime: ''' + str(int(d)) + ' Days, ' + str(int(h)) + ' Hours, ' + str(int(m)) + ' Minutes, ' + str(int(s)) + ' Seconds, ' + str(ms) + ''' Milliseconds</p>
    <small>Please reload this page for the latest data<br />This page will refresh every 20 seconds</small>
    <p id="reloadTime">Next reload in: 20 seconds</p>
    '''

def addProfanitiesCounter():
    global profanitiesDeleted
    profanitiesDeleted += 1

def addReceivedMsgs():
    global receivedMsgs
    receivedMsgs += 1

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    global startTime
    startTime = time.time()
    server = Thread(target=run)
    server.start()