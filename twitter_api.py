# Currently uses python-twitter
# http://static.unto.net/python-twitter/0.6/doc/twitter.html
import twitter

class API:

	# private vars are blank to start
	_username = ""
	_password = ""

	def __init__(self, sUserName, sPassword):
		self.data = []
		self._username = sUserName
		self._password = sPassword

	def print_creds(self):
		print self._username
		print self._password


	def Post(self, sPost):
		if len(sPost) > 140:
			# can't post past 140 chars
			# TODO: handle this case in teh future
			return None
		else:
			# use the twitter.Api to post
			# can change this out in the future if need be
			api = twitter.Api(username=self._username, password=self._password)
			api.PostUpdate(sPost)
