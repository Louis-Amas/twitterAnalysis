from concurrent.futures import ThreadPoolExecutor
import tweepy
import time
from Gatherer import Gatherer


class Updater(Gatherer):
    '''
        Tool for updating number of retweet from a tweet.
    '''

    def __init__(self, dict_of_status):
        super().__init__()
        self.dict_of_status = dict_of_status
        self.dict_of_retweet = dict()

    def getTweetFromId(self, id):
        return self.api.get_status(id=id, tweet_mode="extended")

    def process(self, id, i):
        try:
            tweet = self.getTweetFromId(id)
            self.dict_of_retweet[id] = tweet.retweet_count
        except tweepy.TweepError as e:
            self.dict_of_retweet[id] = -1

    def find(self):
        pool = ThreadPoolExecutor(max_workers=10)
        for i, id in enumerate(self.dict_of_status):
            pool.submit(self.process, id, i)

        pool.shutdown()
