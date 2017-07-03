import tweepy

#set consumer key & secret
consumer_key="DcViIeGPgwtatMIyuo3IA5RIi"
consumer_secret="2pvBoRayPAUXSudX10qrD46JTm9D8RQuVu1Q47M9EqRGuEdPDc"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)


#set access tokens
access_token="281874855-swKpjpblIv7aiuT5HQ6kqHyGDLMNuiKQprFEHeU2"
access_token_secret ="eizLktgWxmQsJKA4GxF159hLBf5rF5sBHWYvnsfKQnrGd"
auth.set_access_token(access_token, access_token_secret)


#get api obj
api = tweepy.API(auth)

#get public tweets object
public_tweets =api.home_timeline()
for tweet in public_tweets:
    #print (tweet.text)
    pass
#get user object

user = api.get_user('twitter')
print (user.screen_name)
print (user.followers_count)

for friend in user.friends():
    print (friend.screen_name)
