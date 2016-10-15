import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights

#The Twitter API credentials
twitter_consumer_key = 'A6yvzpyzrSMBCetadw48BWiUh'
twitter_consumer_secret = 'ZeVZTuUuy8Fxkc8nY7QmrDXME5td95zNf75hv9mNJGjlEid6Le'
twitter_access_token = '24148996-po48EiuLoPmfAotl0joGyfGh0TBiJilDPg7D6rpGb'
twitter_access_secret = 'vgiJdK1CRsiFx7Fbc7prJZ6LziMwCaIQ7tWLmnevAnEcS'

twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)

handle = "@AnthonyTPlummer"

statuses = twitter_api.GetUserTimeline(screen_name=handle, count=200, include_rts=False)

for status in statuses:
  print status.text
