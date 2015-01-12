'''
Packets class

Flags are strings
'''

class Packet:
	#flagsList = ["malicious"]

	def __init__(self, timestamp, src_ip, dest_ip, dest_name, port):
		self.timestamp = timestamp
		self.src_ip = src_ip
		self.dest_ip = dest_ip
		self.dest_name = dest_name
		self.port = port
		self.processed = False
		self.flag = self.initFlags()
		self.getDomain()
	
	def initFlags(self):
		#rt = dict([(f, False) for f in flagsList])
		#return rt
		return False
	
	def getDomain(self):
		dest = self.dest_name.rpartition('/')
		if dest[1] == '/':
			self.domain = dest[0]
			self.file = dest[2]
		else:
			self.domain = dest[2]
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