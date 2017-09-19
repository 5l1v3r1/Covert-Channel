#!/usr/bin/python
# -----------------------------------------------------------------------------
# FUNCTION:       Covert Channel
#
# DATE:           September 19, 2017
#
# DESIGNERS:      Paul Cabanez
#
# PROGRAMMERS:    Paul Cabanez
#
# NOTES: Using Scapy, sniff for packets with C flag, then extract the character
#		 from the source port.
#
# ----------------------------------------------------------------------------*/

import sys
from scapy.all import *

# snifs for packets with C flag, and extracts character from source port, prints
#------------------------------------------------------------------------------
def sniffer(pkt):
	flag = pkt['TCP'].flags
	if flag == 0x80:
		letter = chr(pkt['TCP'].sport)
		print letter

# scapy sniffer 
#------------------------------------------------------------------------------
sniff(filter="tcp", prn=sniffer)
