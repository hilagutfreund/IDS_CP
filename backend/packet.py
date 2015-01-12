'''
Packets class

Flags are strings
'''

def trim(str, lst):
	for l in lst:
		n = len(l)
		if str[0:n] == l:
			str = str[n:]
	return str

class Packet:
	#flagsList = ["malicious"]

	def __init__(self, timestamp, src_ip, dest_ip, dest_name, port, payload):
		self.timestamp = timestamp
		self.src_ip = src_ip
		self.dest_ip = dest_ip
		self.dest_name = trim(dest_name, ["http://", "https://", "ftp://"])
		self.port = port
		self.payload = payload
		self.processed = False
		self.flag = self.initFlags()
		self.getDomain()
	
	def initFlags(self):
		#rt = dict([(f, False) for f in flagsList])
		#return rt
		return False
	
	def getDomain(self):
		dest = self.dest_name.split('/',1)
		if len(dest) > 1:
			self.domain = dest[0]
			self.file = dest[1]
		else:
			self.domain = dest[0]
			self.file = ""
		
	#def setFlag(self, f):
	#	self.flag[f] = True
	def setFlag(self):
		self.flag = True
		
	'''
	Returns the string of the capture event
	'''
	def log(self):
		#return self.timestamp + " " + self.src_ip + " -> " + self.dest_ip + "(" + self.dest_name + "), port " + self.port
		return  "%d: %s -> %s(%s), port %s" % (self.timestamp, self.src_ip, self.dest_ip , self.dest_name, self.port)
	
	'''
	Return the list of flags
	'''
	#def flags(self):
	#	return [key for (key, val) in self.flags.iteritems() if val]