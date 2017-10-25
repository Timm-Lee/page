# -*- coding: utf-8 -*-
# @Author: mac
# @Date:   2017-10-25 11:03:35
# @Last Modified by:   mac
# @Last Modified time: 2017-10-25 12:19:42

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True 
    app.run()