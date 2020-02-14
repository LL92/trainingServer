#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
import requests


# serveur 3 : le mandataire
app = Flask(__name__)

@app.route('/')
def mandataire_requests():
	return 'Ce que je reçois : \n'


if __name__ == '__main__':
      app.run(host='127.0.0.1', port=8080)