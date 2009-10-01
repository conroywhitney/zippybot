import twitter_api
import twitter_creds
import QOTD

# get the filename that contains our quotes
# we will inject this into our QOTD getter
sFileName = "zippybot.txt"

print "FileName: " + sFileName

# get the credentials we need to log into our twitter
creds = twitter_creds.Creds()
sUserName = creds.UserName
sPassword = creds.Password

print "UserName: " + sUserName
print "Password: " + sPassword

# get the Quote of the Day (QOTD) from the file we give it
# this object will do the logic to decide what quote to select
qotd = None
iFailCount = 0

# try 4 different quotes (in case they exceed 140 chars)
# do not try forever
while (qotd == None and iFailCount < 4):
	# get quote from file
	qotd = QOTD.GetQOTD(sFileName)

	if (len(qotd) > 140):
		# damn . try again .
		iFailCount += 1
		qotd = None
		print "too long; trying again (" + str(iFailCount) + ")"	

	if qotd != None:
		# create an instance of the twitter API using our creds
		# this will be what we use to actually post our info
		api = twitter_api.API(sUserName, sPassword)
		api.Post(qotd)

