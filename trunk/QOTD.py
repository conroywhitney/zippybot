import random

def GetQOTD(sFileName):
	sResult = None
	oFile = None
	iNextIndex = getNextIndex()

	try:
		#"getting index: " + str(iNextIndex)
		oFile = open(sFileName, "r")
		arrLines = oFile.readlines()
		if (iNextIndex < len(arrLines)):
			# make sure we're not crazy and that our file is long enough
			sResult = arrLines[iNextIndex]
		else:
			# we are looking past the end of the file
			sResult = None
	except:
		sResult = None
	finally:
		if oFile != None:
			#print "closing"
			oFile.close()

	return sResult
	
def getNextIndex():
	# for now, get any random line
	# TODO: don't repeat lines within a certain timeperiod (or evarr?)
	return random.randrange(0, getFileLength())

def getFileLength():
	# hard-code the length of our file for now
	# TODO: get the length of the file so we can add more in the future
	return 762
		
		
