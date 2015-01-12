#!/usr/bin/env python
# this is a simple example to sniff on port 80 for magic CAFEBABE.
# it has to run either sudo root on any Unix or with windows admin right.
# author email: pythonrocks@gmail.com.
import dpkt, pcap
import re
import sys

pattern=re.compile('.*')

def __my_handler(pktlen,pkt,timestamp):

    print 'working'
    tcpPkt=dpkt.tcp.TCP(pkt)
    data=tcpPkt.data

    # let's find any java class pass
    searched=pattern.search(data)

    if searched:
      d['hits']+=1
      print 'counters=',d['hits']

pc = pcap.pcap()
pc.setfilter('tcp and dst port 80')
print 'listening on %s: %s' % (pc.name, pc.filter)
#pc.loop(1, __my_handler)


# try-except block to catch keyboard interrupt.  Failure to shut
# down cleanly can result in the interface not being taken out of promisc.
# mode
#p.setnonblock(1)
try:
    # while 1:
    #     pc.dispatch(1, __my_handler)

    # specify 'None' to dump to dumpfile, assuming you have called
    # the dump_open method
    #  p.dispatch(0, None)

    # the loop method is another way of doing things
    #pc.loop(1, __my_handler)

    # as is the next() method
    # p.next() returns a (pktlen, data, timestamp) tuple
    apply(__my_handler,p.next())
except:
    print sys.exc_info()[0]
    print '%s' % sys.exc_type
    print 'shutting down'
    print '%d packets received, %d packets dropped, %d packets dropped by interface' % pc.stats()
