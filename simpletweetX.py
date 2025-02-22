import tweepy

consumer_key = 'xxx'
consumer_secret = 'xxx'
access_token = 'xxx'
access_secret = 'xxx'

client = tweepy.Client(
    consumer_key = consumer_key, consumer_secret = consumer_secret,
    access_token=access_token, access_token_secret=access_secret)

response = client.create_tweet(
    text='Tweeting this message using python')

print("posted successfully")