import tweepy

class Twitter():
	#twiteer access data
	ckey = "app key"
	csecret = "app key"
	atoken = "app key"
	asecret = "app key"

	def __init__(self):

		self.auth = tweepy.OAuthHandler(self.ckey, self.csecret)
		self.auth.set_access_token(self.atoken, self.asecret)

		self.api = tweepy.API(self.auth)
	def send_tweet(self,message):
		try:
			self.api.update_status(message)
		except Exception as e:
			print(e.message)
