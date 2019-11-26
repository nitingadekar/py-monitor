#!/usr/bin/python3

import os
#from slackclient import SlackClient
import slack
#slack_token = os.environ["SLACK_API_TOKEN"]
slack_token = 'xoxb-840005619745-850142514902-pFaNzF6YH6Gx2NQCILvSqg8O'
#sc = SlackClient(slack_token)
sc = slack(slack_token)

sc.api_call(
  "chat.postMessage",
  channel="#monitoring",
  text="Hello from Python! :tada:"
)
