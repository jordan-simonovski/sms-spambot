import requests
import os

base_url = "https://reddit.com/r/"
subreddit = os.environ.get('subreddit')
json_url = base_url+subreddit+"/.json"
recipient_name = os.environ.get('recipient')

headers={
    'User-Agent': 'NewsGetter 1.0',
    'From': 'jordan.simonovski@gmail.com'
}

def get_subreddit_post_data():
    response = requests.get(url=json_url, headers=headers)
    data = response.json()
    post_title = data['data']['children'][2]['data']['title']
    post_link = data['data']['children'][2]['data']['url']
    sms_message_text = "Hey {0}!\nCheck out today's post!\n {1} \n {2}".format(recipient_name, post_title, post_link)
    return sms_message_text
