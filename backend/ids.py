from packet import Packet
from VirusTotalAPI import VTDetectionRatio

'''
Levenshtein edit distance
'''
def edit_distance(s1, s2):
    m=len(s1)+1
    n=len(s2)+1

    tbl = {}
    for i in range(m): tbl[i,0]=i
    for j in range(n): tbl[0,j]=j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)

    return tbl[i,j]

'''
IDS class
Where all the magic happens
'''
class IDS:
	'''
	Pass the resource file names (where the log and blacklist are going to be stored)
	'''
	self.VTRatioThreshold = 0.05 #!?!
	def __init__(self, logfile, blacklist, topdom):
		self.logfile = open(logfile, "r")
		self.loadBl(blacklist, "r+")
		self.loadTopDomains(topdom)
	
	def loadBl(self, f):
		d = []
		self.handle = open(f)
		for line in handle:
			d.append(line)
		self.blacklist = d
	
	def loadTopDomains(self, f):
		d = set()
		handle = open(f)
		for line in handle:
			d.add(line)
		self.topDomains = d
	
	def recordMalicious(self, pk, bl):
		pk.setFlag()
		self.logfile.write(pk.log() + " [MALICIOUS]")
		self.logfile.write("\n")
		if bl:
			self.blacklist(pk.dest_name)
	
	def blacklist(self, dom):
		self.handle.write(dom)
		self.handle.write("\n")
	
	def externalAnalysis(self, pk):
		url = packet.dest_name
		ratio = VTDetectionRatio(url)
		return ratio
	
	def compareToDomains(self, dom):
		res = map(lambda x: (1. - float(edit_distance(x, dom))/len(x), x), self.topDomains)
		return max(res)
	
	'''
	Main function to treat an incoming packet
	Should flag it if it's malicious
	Log the event if needed etc.
	'''
	def processIncomingPacket(packet):
		# Here the magic happens
		
		if packet.domain in self.blacklist or packet.dest_name in self.blacklist:
			self.recordMalicious(packet, False)
		else:
			dom = packet.domain
			m = self.compareToDomains(dom)
			if (m[0] > 0.5 and m[0] < 1.):
				self.recordMalicious(packet, True)
			else:
				detection_Rate = self.externalAnalysis(packet)
				tag = detection_Rate > self.VTRatioThreshold
				if tag: self.recordMalicious(packet, True)
		
		# Finally, mark the packet as processed
		packet.processed = True