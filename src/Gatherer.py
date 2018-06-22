import tweepy

class Gatherer():

    def __init__(self):
        self.token_access = '1854979992-vyTFAg3qwhbqfWk6d0OmAFKDXRd0cNo1H8f3iln'
        self.token_secret = 'jZd7uiLHxCSWuXJ4zXlJzA8DsNgLkITljmihMGfkuHZuR'
        self.consumer_key = 'V5wp5n8OVksr63cFoFMagaFAL'
        self.consumer_secret = 'Fjna0z4e7ptsiMkWZS4a0dYBbXg82IZdNYshBTnaYLXQ8Og7Fm'
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.token_access, self.token_secret)
        self.api = tweepy.API(self.auth)