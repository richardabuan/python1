from flask import Flask
from datetime import datetime
import calendar

app = Flask(__name__)

def dayname(time):
    """Return the name of the day of the week for the given time."""
    return calendar.day_name[time.weekday()]
    
@app.route("/")
def hello_world():
    return f"<p>Hello, world! Happy {dayname(datetime.now())}.</p>"
