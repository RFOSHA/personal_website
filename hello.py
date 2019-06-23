# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 20:04:08 2019

@author: ryanm
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"