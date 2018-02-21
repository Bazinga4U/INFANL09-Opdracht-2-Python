from flask import Flask
from flask import request, escape
import sqlite3

import os.path

# Joins path of Python and the DB

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "headers.db")


app = Flask(__name__)

@app.route('/')
def hello_world():

    # Make DB connection
    with sqlite3.connect(db_path) as db:
        c = db.cursor()

    # Request the headers

    headers = request.headers
    userAgentHeaders = request.user_agent.string


    # Print whole header in console log in pycharm

    print(headers)

    # Execute insert in DB

    c.execute("INSERT INTO Allheaders (header) VALUES (?)", (str(userAgentHeaders),))


    #loop to show the count on the screen from specific headers

    i = 0

    for x in c.execute("SELECT * FROM Allheaders"):
        if(x[1] == request.user_agent.string):
            i+=1


    # Commit to DB
    db.commit()

    # Close DB connection
    db.close()

    return escape(userAgentHeaders) + "_______ " + "count = " +str(i)

if __name__ == '__main__':
    app.run()
