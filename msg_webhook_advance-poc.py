#!/usr/bin/python3


import socket
import json
import requests

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

#def slack_msg(msg):
webhook_url = 'https://hooks.slack.com/services/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'
#    slack_data = {'text':  msg }
#    response = requests.post( webhook_url, data=json.dumps(slack_data), headers={'Content-Type': 'application/json'} )
#    if response.status_code != 200:
#        raise ValueError('Request to slack returned an error %s, the response is:\n%s'% (response.status_code, response.text) )

slack_data ={"attachments": [{"fallback": "Required plain-text summary of the attachment.","color": "#36a64f","pretext": "Pymonit sending alert notifications","author_name": "Basic Monitoring", "author_link": "https://github.com/nitingadekar/py-monitor", "author_icon": "http://flickr.com/icons/bobby.jpg", "title": "Tool Module Source Code", "title_link": "https://github.com/nitingadekar/py-monitor", "text": "CPU Critical", "fields": [ { "title": "Priority", "value": "High" }],"image_url": "https://qualidadeeti.files.wordpress.com/2015/11/burning-cpu.jpg","thumb_url": "https://qualidadeeti.files.wordpress.com/2015/11/burning-cpu.jpg","footer": "Slack API", "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png","ts": 123456789 }]}
response = requests.post( webhook_url, data=json.dumps(slack_data), headers={'Content-Type': 'application/json'} )
if response.status_code != 200:
    raise ValueError('Request to slack returned an error %s, the response is:\n%s'% (response.status_code, response.text) )
