# save this as app.py
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    DAYNAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    dayname = DAYNAMES[datetime.now().weekday()]
    return "<p>hello, world!</p>"
