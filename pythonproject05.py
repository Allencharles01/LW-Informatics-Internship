#Post on Twitter (X): Post a message on Twitter (X) using Python. 

import tweepy

# Replace with your Twitter Developer credentials
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Post your tweet
try:
    tweet = "🚀 Posting to Twitter using Python! #Python #Automation #TwitterAPI"
    api.update_status(tweet)
    print("✅ Tweet posted successfully!")
except Exception as e:
    print("❌ Failed to post tweet:", e)
