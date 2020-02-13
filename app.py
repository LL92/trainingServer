from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
	request = requests.get('http://127.0.0.1:4567/')
	print(request.text)
	return 'PING !'