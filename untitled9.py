from flask import Flask
from flask import request, escape
import sqlite3

import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "headers.db")
with sqlite3.connect(db_path) as db:

    c = db.cursor()

app = Flask(__name__)

@app.route('/')
def hello_world():
    headers = request.headers
    userAgentHeaders = request.user_agent.string

    print(headers)

    c.execute("INSERT INTO Allheaders (header) VALUES (?)", (str(userAgentHeaders),))
    db.commit()
    db.close()

    return escape(userAgentHeaders)

if __name__ == '__main__':
    app.run()
