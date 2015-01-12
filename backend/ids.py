'''
IDS class
Where all the magic happens
'''

class IDS:
	'''
	Pass the resource file names (where the log and blacklist are going to be stored)
	'''
	def __init__(self, logfile, blacklist):
		self.logfile = open(logfile, "r")
		self.loadBl(blacklist)
	
	def loadBl(self, f):
		d = []
		handle = open(f)
		for line in handle:
			d.append(line)
		self.blacklist = d
	
	def recordMalicious(self, pk):
		pk.setFlag()
		self.logfile.write(pk.log() + " [MALICIOUS]")
		self.logfile.write("\n")
	
	# VTotal...
	def externalAnalysis(self, pk):
		# TO DO... (by Michael)
		return False
	
	'''
	Main function to treat an incoming packet
	Should flag it if it's malicious
	Log the event if needed etc.
	'''
	def processIncomingPacket(packet):
		# Here the magic happens
		
		if packet.domain in self.blacklist:
			self.recordMalicious(packet)
		else:
			# Deeper tests...
			tag = self.externalAnalysis(packet)
			if tag: self.recordMalicious(packet)
		
		# Finally, mark the packet as processed
		packet.processed = True