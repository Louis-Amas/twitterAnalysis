from tweepy import StreamListener


class StreamProcess(StreamListener):
    '''
        Process a tweet when streamListener get one.

    '''
    def __init__(self, max_tweet, fct):
        '''
            max_tweet = nb of tweets to gather.
            fct = function for processing data.
        '''
        super().__init__()
        self.fct = fct
        self.max_tweet = max_tweet
        self.cpt = 0

    def on_data(self, data):
        if self.cpt >= self.max_tweet:
            return False
        self.cpt += 1
        self.fct(data)
        return True

    def on_error(self, status):
        print(status)
