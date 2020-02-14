#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
import requests


# serveur 2 : envoie PONG
app = Flask(__name__)

'''
@app.route('/')
def hello_world():
	request = requests.get('http://127.0.0.1:5000/')
	print(request.text)
	return 'PONG !'

if __name__ == '__main__':
      app.run(host='127.0.0.1', port=8000)
'''

@app.route('/')
def pong_request():
	req = requests.get('http://127.0.0.1:8080/')
	print(requests.text)
	return 'PONG'

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5372)