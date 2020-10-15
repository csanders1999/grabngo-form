#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, os

from flask import Flask, request, Response
from slack import WebClient

from message import create_message

app = Flask(__name__, template_folder='')

client = WebClient(token=os.environ.get('TOKEN'))

@app.route('/', methods=['GET'])
def main():
  return Response("Welcome")

@app.route('/interactive', methods=['POST'])
def interactive():
    payload = json.loads(request.form["payload"])
    grabngo_channel = "C01CC1YL36J"
    message = create_message(payload["view"]["state"]["values"])
    client.chat_postMessage(channel=grabngo_channel, attachments=message)
    return Response()
  
@app.route('/slashcommand', methods=['GET', 'POST'])
def slashcommand():
    with open("modal.txt") as modalfile:
        client.views_open(trigger_id=request.form["trigger_id"], view=json.load(modalfile))
    return Response()

if __name__ == '__main__':
    app.run()