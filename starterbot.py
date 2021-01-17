import os
import time
import re
import slack
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], '/slack/events', app)
print(os.environ['SIGNING_SECRET'])

client = slack.WebClient(os.environ['SLACK_BOT_TOKEN'])
bot_id = client.api_call("auth.test")['user_id']


@app.route('/ticket-create', methods=['POST'])
def create_ticket():
    text = request.form.get('text')
    print(text)
    return Response(), 200


if __name__ == "__main__":
    app.run(debug=True)
