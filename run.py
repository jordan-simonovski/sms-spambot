import os
from flask import Flask, jsonify, json, request
from modules import *
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def lambda_handler(event=None, context=None):
    return ""

def spamVictim(req,res):
    sms_message = reddit.get_subreddit_post_data()
    sns.send_message(sms_message)
    return ('', 200)

def initialMessage(req,res):
    victim_name = os.environ.get('recipient')
    subject = os.environ.get('sms_subject')
    sms_message = "Hi, {0}! Thanks for signing up to {1}".format(victim_name, subject)
    sns.send_message(sms_message)

if __name__ == '__main__':
    app.run(debug=True)