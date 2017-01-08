import tweepy
from textblob import TextBlob

consumer_key ='jChj0ZaEioE20dvhPfwlMRn6O'
consumer_secret ='jHrqlXBXEKoKvwrxdxaewDj6F2rcYfwB8ZOXAZV7m7FFwUNwqC'

access_token ='564593624-qJ70UoyGa1QXxZP6RFeGA3B9TqYeWwGNo4Rb3pAX'
access_token_secret ='dvt2NYRhTWF9UMqtddc9TeMlW2aHTkWzKTY7CYHFaR3Tf'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('thyao',lang = "en", rpp = 1 )

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
