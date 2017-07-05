from twython import TwythonStreamer

tweets = []
tweet_texts = []
tweet_timestamp = []
tweet_user_verified = []
tweet_created_at = []
tweet_user_mentions = []
tweet_place = []
tweet_hashtags = []

handle=csv.writer(open('twitter_feed.csv','wb'))

class ModiInIsrael_17(TwythonStreamer):
    def on_success(self,data):
        if data['lang']=='en':
            tweets.append(data)
            tweet_texts.append(data['text'])
            tweet_timestamp.append(data['timestamp_ms'])
            tweet_user_verified.append(data['user']['verified'])
            tweet_created_at.append(data['created_at'])
            tweet_place.append(data['place'])
            tweet_hashtags.append(data['entities']['hashtags'])
            length = len(data['entities']['user_mentions'])
            print "received tweet #", len(tweets)
            
            for user in range(length):
                tweet_user_mentions.append(data['entities']['user_mentions'][user]['screen_name'])
                print "user-mentions >> ", data['entities']['user_mentions'][user]['screen_name']
                        
            print "hashtags >> ", data['entities']['hashtags']
            
            print "============================================"

    
        if len(tweets)>=1000:
            self.disconnect()


one = 'CONSUMER_KEY'
two = 'CONSUMER_SECRET'
three = 'ACCESS_TOKEN'
four = 'ACCESS_TOKEN_SECRET'


stream = ModiInIsrael_17(one,two,three,four)

stream.statuses.filter(track='modi')
