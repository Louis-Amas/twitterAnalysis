import tweepy

import json
import re
import datetime
from tweepy import Stream

from Gatherer import Gatherer
from StreamProcess import StreamProcess


class GathererStreamTweet(Gatherer):

    def __init__(self):

        super().__init__()
        self.list_of_hashtags = []
        self.list_of_tweets = []
        self.begining = 0
        self.end = 0

    def findHashtags(self, str):
        pat = re.compile(r"#(\w+)")
        list = pat.findall(str)
        for hashtag in list:
            self.list_of_hashtags.append(hashtag.lower())

    def gatherData(self, maxTweet):
        self.begining = datetime.datetime.now().timestamp()
        streamListener = StreamProcess(maxTweet, self.process)
        stream = Stream(self.auth, streamListener)
        stream.filter(locations=[-180, -90, 180, 90], languages=['en'])

    def getTweetFromId(self, id):
        return self.api.get_status(id=id, tweet_mode="extended")

    def process(self, status):
        status = json.loads(status)
        if 'text' in status:
            self.findHashtags(status['text'])
            self.list_of_tweets.append('"' + str(status['id']) + '";"' + status['user']['id_str'] + '";"' + str(
                status['user']['followers_count']) + '";"'
                                     + str(status['user']['statuses_count']) + '";"' + status['timestamp_ms'] + '"')

    def saveData(self, fileHashTags, FileTweets):

        self.end = datetime.datetime.now().timestamp()
        file = open(fileHashTags, 'w')
        hashtagsSet = set(self.list_of_hashtags)
        file.write(str(len(self.list_of_hashtags)) + '\n')
        for hashTag in hashtagsSet:
            file.write(hashTag + ';' + str(self.list_of_hashtags.count(hashTag)) + '\n')
        file.close()
        file = open(FileTweets, 'w')
        file.write(str(len(self.list_of_tweets)) + ';' + str(self.begining) + ';' + str(self.end) + '\n')
        file.write("tweetId;userId;followers;statuses_count;created_at\n")
        for tweet in self.list_of_tweets:
            file.write(tweet + '\n')
        file.close()

gt = GathererStreamTweet()
st = gt.getTweetFromId('934592567613603840')
print(st.retweet_count)