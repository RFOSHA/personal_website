# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:13:47 2019

@author: ryanm
"""
from flask_frozen import Freezer
from app import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()