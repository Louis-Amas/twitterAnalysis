import tweepy
import datetime
from tweepy import Stream
from Gatherer import Gatherer
import json
import re
from StreamProcessHashtagsOnly import StreamProcessHashtagsOnly
from sys import argv



class GatherTextAndHashtags(Gatherer):
    '''
        Get tweet from stream twitter and save in file.
        Save only text and hashtags
    '''
    def __init__(self, path_fic_out):
        super().__init__()
        self.path_fic_out = path_fic_out

    def __enter__(self):
        self.fic_out = open(self.path_fic_out, 'a+', encoding='utf8')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fic_out.close()

    def process(self, status):
        hashtags = status['entities']['hashtags']
        replaced = re.sub('#[^\ \t\n]+', '', status['text'])
        replaced = replaced.replace('\n', ' ')
        hashtags = [hashtag[key] for hashtag in hashtags for key in hashtag if key == 'text']
        dic = dict()
        dic['text'] = replaced
        dic['hashtags'] = hashtags
        self.fic_out.write(json.dumps(dic) + '\n')
        self.fic_out.flush()

    def gatherData(self, maxTweet):
        self.begining = datetime.datetime.now().timestamp()
        streamListener = StreamProcessHashtagsOnly(maxTweet, self.process)
        stream = Stream(self.auth, streamListener, tweet_mode='extended')
        stream.filter(locations=[-180, -90, 180, 90], languages=['fr'])


if __name__ == '__main__':
    if len(argv) < 3:
        print(argv[0], ' numberOfTweets output.json')
        exit(1)

    nb = int(argv[1])
    path = argv[2]
    for i in range(0, nb, 100):
        with GatherTextAndHashtags(path) as gt:
            gt.gatherData(i)
        print(i)    
