#!/usr/bin/python
# -*- coding: utf-8 -*-
# File name: run.py
'''
Main file that gets run and handles the routing to index and api calls
'''
from flask import Flask, render_template, jsonify
from api.tools import get_everything

# TODO remove static_url_path
app = Flask(__name__, template_folder='static/', static_url_path='')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/alles', methods=['GET'])
def alles():
    return jsonify(get_everything())


if __name__ == '__main__':
    app.run(debug=True)
