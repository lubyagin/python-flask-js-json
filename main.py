# -*- coding: windows-1251 -*-
# C:\Python27\python.exe main.py

from flask import Flask
from flask import render_template
from flask import jsonify

import json

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
  return render_template("index.html")

# 404 Not Found, if type(n) = string
@app.route('/get/<int:n>', methods=["GET"])
def get(n):
  # отправить результат обратно
  s = json.dumps({"n":n})
  return s

if __name__ == '__main__':
  app.run(debug = True)
