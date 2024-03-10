from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def delayed_response():
    time.sleep(2)  # Simulate a 2-second delay.
    return 'This response is delayed, but not when cached by NGINX!'