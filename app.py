# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 14:45:31 2019

@author: ryanm
"""

import os
from flask import Flask, render_template

os.chdir('C:/Users/ryanm/Desktop/Python_Website')


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)