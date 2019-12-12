#!/usr/bin/python3



import json
import requests

def slack_msg(msg):
    webhook_url = 'https://hooks.slack.com/services/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'
    slack_data = {'text': msg}
    response = requests.post( webhook_url, data=json.dumps(slack_data), headers={'Content-Type': 'application/json'} )
    if response.status_code != 200:
        raise ValueError('Request to slack returned an error %s, the response is:\n%s'% (response.status_code, response.text) )
