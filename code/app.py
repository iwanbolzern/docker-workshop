from os import path

from flask import Flask
import os
import socket


FILE_PATH = 'data/count.txt'
app = Flask(__name__)


@app.route("/")
def hello():
    visits = 0
    if path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as count_file:
            visits = int(count_file.read())

    visits += 1
    with open(FILE_PATH, 'w') as count_file:
        count_file.write(str(visits))

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
