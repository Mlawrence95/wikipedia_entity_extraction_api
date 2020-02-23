# -*- coding: utf-8 -*-
import requests

payload = {
    'data': "https://en.wikipedia.org/wiki/Manhattan_Project"
}

address = "http://127.0.0.1"
port    = '5000'
r = requests.get(f'{address}:{port}/wiki-entities', params=payload)
print(r.text)
