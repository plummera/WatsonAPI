import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights

def analyze(handle):
  #The Twitter API credentials
  twitter_consumer_key = 'A6yvzpyzrSMBCetadw48BWiUh'
  twitter_consumer_secret = 'ZeVZTuUuy8Fxkc8nY7QmrDXME5td95zNf75hv9mNJGjlEid6Le'
  twitter_access_token = '24148996-po48EiuLoPmfAotl0joGyfGh0TBiJilDPg7D6rpGb'
  twitter_access_secret = 'vgiJdK1CRsiFx7Fbc7prJZ6LziMwCaIQ7tWLmnevAnEcS'

  twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)

  statuses = twitter_api.GetUserTimeline(screen_name=handle, count=200, include_rts=False)

  text = ""

  for status in statuses:
    if (status.lang =='en'): #English tweets
        text += status.text.encode('utf-8')

  #IBM credentials
  pi_username = '3ac6f39c-9d8a-4185-9a46-a24308b813e0'
  pi_password = '885bn2fPmheY'

  personality_insights = PersonalityInsights(username=pi_username,password=pi_password)

  pi_result = personality_insights.profile(text)

  return pi_result

def flatten(orig):
  data = {}
  for c in orig['tree']['children']:
    if 'children' in c:
      for c2 in c['children']:
        if 'children' in c2:
          for c3 in c2['children']:
            if 'children' in c3:
              for c4 in c3['children']:
                if (c4['category'] == 'personality'):
                  data[c4['id']] = c4['percentage']
            if 'children' not in c3:
                if (c3['category'] == 'personality'):
                    data[c3['id']] = c3['percentage']
                    return data

def compare(dict1, dict2):
    compared_data = {}
    for keys in dict1:
        if dict1[keys] != dict2[keys]:
            compared_data[keys]=abs(dict1[keys] - dict2[keys])
    return compared_data

user_handle = "@AnthonyTPlummer"
celebrity_handle = "@IBM"

user_result = analyze(user_handle)
celebrity_result = analyze(celebrity_handle)

#Flatten results from Watson PI API
user = flatten(user_result)
celebrity = flatten(celebrity_result)

#Comapre the results of Watson API
compared_results = compare(user,celebrity)

sorted_result = sorted(compared_results.items(),key=operator.itemgetter(1))

for keys, value in sorted_result[:5]:
  print keys,
  print(user[keys]),
  print ('->'),
  print (celebrity[keys]),
  print ('->'),
  print (compred_results[keys])
