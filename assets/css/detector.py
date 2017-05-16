import dpkt, scapy
import sys

def main():
	f = open(sys.argv[1])
	pcap = dpkt.pcap.Reader(f)
	frame_counter = 0
	for ts, buf in pcap:
	    frame_counter += 1
	    if frame_counter > 1 :
	        print "%d: %f %f" % ( frame_counter, ts, ts - last_time )
	    last_time = ts
	f.close()

if __name__ == '__main__':
	main()