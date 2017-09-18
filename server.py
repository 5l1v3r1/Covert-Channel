import sys
from scapy.all import *


def sniffer(pkt):
	flag = pkt['TCP'].flags
	if flag == 0x80:
		letter = chr(pkt['TCP'].sport)
		print letter

sniff(filter="tcp", prn=sniffer)
