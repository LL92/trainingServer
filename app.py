#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
import requests

# serveur 1 : envoie PING

app = Flask(__name__)
'''
@app.route('/')
def hello_world():
	request = requests.get('http://127.0.0.1:8000/')
	print(request.text)
	return 'PING !'
'''

@app.route('/')
def request_ping():
	req = requests.get('http://127.0.0.1:8080/')
	print(requests.text)
	return 'PING'

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=4567)