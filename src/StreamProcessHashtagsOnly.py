from tweepy import StreamListener
import json

class StreamProcessHashtagsOnly(StreamListener):
    '''
        Gather only tweets with hashtags
    '''

    def __init__(self, max_tweet, fct):
        super().__init__()
        self.fct = fct
        self.max_tweet = max_tweet
        self.cpt = 0

    def on_data(self, data):
        if self.cpt >= self.max_tweet:
            return False
        status = json.loads(data)
        if 'entities' in status.keys() and len(status['entities']['hashtags']) > 0:
            self.cpt += 1
            self.fct(status)
        return True

    def on_error(self, status):
        print(status)
