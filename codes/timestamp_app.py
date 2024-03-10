from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def current_time():
    return f"Current time is: {datetime.datetime.now()}"