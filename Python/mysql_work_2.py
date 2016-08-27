from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'z4ocqOT6gNeVeRiKh6ZfXJp3z'
csecret = 'qVYOdNi2aqtClePXOTBA0SXzvPWFXY1K71nqZR1hhY12I5ZNLb'
atoken = '250398113-GNL4sCF9ndaWxFrH57nvd5eoNohmgRmD3i9H1cG3'
asecret = 'UJzVQ0jB0Ry2BEEuLQC0hhHTvk6LHMwvcn5ljQhA3t4vv'

class listener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])
